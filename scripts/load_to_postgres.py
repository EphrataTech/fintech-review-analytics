import pandas as pd
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="bank_reviews",
    user="postgres",
    password="1234"
)

cur = conn.cursor()

# Load CSV
df = pd.read_csv("data/raw/sentiment_analysis_results.csv")

# -----------------------------------
# Insert Banks
# -----------------------------------

banks = {
    "Commercial Bank of Ethiopia": 1,
    "Bank of Abyssinia": 2,
    "Dashen Bank": 3
}

for bank_name, bank_id in banks.items():
    cur.execute(
        "INSERT INTO banks (bank_id, bank_name, app_name) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING",
        (bank_id, bank_name, bank_name)
    )

# -----------------------------------
# Insert Reviews
# -----------------------------------

for _, row in df.iterrows():

    bank_id = banks.get(row.get("bank", ""), None)

    cur.execute(
        """
        INSERT INTO reviews (
            review_id,
            bank_id,
            review_text,
            rating,
            review_date,
            sentiment_label,
            sentiment_score,
            identified_theme,
            source
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (review_id) DO NOTHING
        """,
        (
            int(row["review_id"]),
            bank_id,
            row["review"],
            int(row.get("rating", 0)),
            None,  # optional if not included
            row["sentiment_label"],
            float(row["sentiment_score"]),
            row["identified_theme"],
            "Google Play"
        )
    )

conn.commit()
cur.close()
conn.close()

print("Data inserted successfully!")