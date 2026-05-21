import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/raw/sentiment_analysis_results.csv")

# -----------------------------------
# 1. Sentiment distribution by bank
# -----------------------------------

sentiment_counts = df.groupby(["bank", "sentiment_label"]).size().unstack()

sentiment_counts.plot(kind="bar", stacked=True)
plt.title("Sentiment Distribution by Bank")
plt.xlabel("Bank")
plt.ylabel("Number of Reviews")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sentiment_distribution.png")
plt.show()

# -----------------------------------
# 2. Rating distribution
# -----------------------------------

df.boxplot(column="rating", by="bank")
plt.title("Rating Distribution per Bank")
plt.suptitle("")
plt.xlabel("Bank")
plt.ylabel("Rating")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("rating_distribution.png")
plt.show()

# -----------------------------------
# 3. Theme frequency
# -----------------------------------

theme_counts = df.groupby(["bank", "identified_theme"]).size().unstack().fillna(0)

theme_counts.plot(kind="bar", stacked=True)
plt.title("Theme Frequency by Bank")
plt.xlabel("Bank")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("theme_frequency.png")
plt.show()