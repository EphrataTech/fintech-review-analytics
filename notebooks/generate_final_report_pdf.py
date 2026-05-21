from pathlib import Path
import re
from fpdf import FPDF

ROOT = Path(__file__).resolve().parent
MARKDOWN_PATH = ROOT / "final_report.md"
PDF_PATH = ROOT / "final_report.pdf"

class PDFReport(FPDF):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_unicode_font()

    def add_unicode_font(self):
        font_path = Path("C:/Windows/Fonts/arial.ttf")
        if font_path.exists():
            self.add_font("ArialUnicode", "", str(font_path), uni=True)
            self.add_font("ArialUnicode", "B", str(font_path), uni=True)
            self.add_font("ArialUnicode", "I", str(font_path), uni=True)
            self.add_font("ArialUnicode", "BI", str(font_path), uni=True)
        else:
            self.add_font("Helvetica", "B", uni=True)
            self.add_font("Helvetica", "", uni=True)
            self.add_font("Helvetica", "I", uni=True)
            self.add_font("Helvetica", "BI", uni=True)

    def header(self):
        self.set_font("ArialUnicode", "B", 14)
        self.cell(0, 10, "Fintech Review Analytics", ln=True, align="C")
        self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("ArialUnicode", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def add_markdown_paragraph(self, text, style="normal"):
        if style == "title":
            self.set_font("ArialUnicode", "B", 16)
            self.multi_cell(0, 10, text)
        elif style == "heading":
            self.set_font("ArialUnicode", "B", 14)
            self.multi_cell(0, 9, text)
        elif style == "subheading":
            self.set_font("ArialUnicode", "B", 12)
            self.multi_cell(0, 8, text)
        else:
            self.set_font("ArialUnicode", "", 11)
            self.multi_cell(0, 6.5, text)
        self.ln(1)

    def add_image(self, image_path, caption=None):
        if not image_path.exists():
            return
        max_width = 170
        x = (210 - max_width) / 2
        self.image(str(image_path), x=x, w=max_width)
        if caption:
            self.set_font("ArialUnicode", "I", 10)
            self.cell(0, 5, caption, ln=True, align="C")
        self.ln(4)


def parse_markdown(markdown_text):
    lines = markdown_text.splitlines()
    blocks = []
    current = []
    for line in lines:
        if line.startswith("#") or line.startswith("![") or line.strip() == "":
            if current:
                blocks.append("\n".join(current).strip())
                current = []
            blocks.append(line)
        else:
            current.append(line)
    if current:
        blocks.append("\n".join(current).strip())
    return blocks


def render_pdf():
    pdf = PDFReport(format="A4")
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    markdown_text = MARKDOWN_PATH.read_text(encoding="utf-8")
    blocks = parse_markdown(markdown_text)

    for block in blocks:
        if block.startswith("# "):
            pdf.add_markdown_paragraph(block[2:].strip(), style="title")
        elif block.startswith("## "):
            pdf.add_markdown_paragraph(block[3:].strip(), style="heading")
        elif block.startswith("### "):
            pdf.add_markdown_paragraph(block[4:].strip(), style="subheading")
        elif block.startswith("!["):
            match = re.match(r"!\[(.*?)\]\((.*?)\)", block)
            if match:
                caption = match.group(1).strip()
                path = ROOT / match.group(2).strip()
                if pdf.get_y() > 200:
                    pdf.add_page()
                pdf.add_image(path, caption=caption)
        else:
            for paragraph in block.split("\n\n"):
                paragraph = paragraph.strip()
                if not paragraph:
                    continue
                pdf.add_markdown_paragraph(paragraph.replace("`", ""), style="normal")

    pdf.output(str(PDF_PATH))
    print(f"Generated PDF: {PDF_PATH}")


if __name__ == "__main__":
    render_pdf()
