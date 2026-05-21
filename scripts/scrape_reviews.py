from google_play_scraper import reviews, Sort
import pandas as pd

# Bank applications
apps = {
    "Commercial Bank of Ethiopia": "com.combanketh.mobilebanking",
    "Bank of Abyssinia": "com.boa.boaMobileBanking",
    "Dashen Bank": "com.dashen.dashensuperapp"
}

all_reviews = []

for bank_name, app_id in apps.items():
    print(f"Scraping reviews for {bank_name}...")

    result, _ = reviews(
        app_id,
        lang='en',
        country='et',
        sort=Sort.NEWEST,
        count=500
    )

    for review in result:
        all_reviews.append({
            "review": review["content"],
            "rating": review["score"],
            "date": review["at"].strftime("%Y-%m-%d"),
            "bank": bank_name,
            "source": "Google Play"
        })

# Convert to DataFrame
df = pd.DataFrame(all_reviews)

# Remove duplicates
before_duplicates = len(df)
df = df.drop_duplicates()
after_duplicates = len(df)

# Remove missing values
before_missing = len(df)
df = df.dropna(subset=["review", "rating"])
after_missing = len(df)

print(f"Duplicates removed: {before_duplicates - after_duplicates}")
print(f"Missing rows removed: {before_missing - after_missing}")

# Save cleaned data
output_path = "data/raw/fintech_reviews_cleaned.csv"
df.to_csv(output_path, index=False)

print(f"Saved cleaned dataset to {output_path}")
print(df.head())