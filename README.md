

## Scraping Methodology

Reviews were collected using the `google-play-scraper` Python package.

Targeted Applications:
- Commercial Bank of Ethiopia
- Bank of Abyssinia
- Dashen Bank

Collected Fields:
- Review text
- Rating
- Review date
- Bank name
- Source

Source:
- Google Play Store

---

## Data Preprocessing

The following preprocessing steps were applied:

- Removed duplicate reviews
- Removed missing values
- Normalized dates to YYYY-MM-DD format

Final dataset columns:
- review
- rating
- date
- bank
- source

---

## Limitations

The number of reviews available depends on Google Play Store availability.
Some applications may provide fewer reviews than requested.




## Database Setup (Task 3)

A PostgreSQL database named `bank_reviews` was created.

Tables:
- banks
- reviews

Data insertion was performed using a Python script with psycopg2.

Verification queries confirmed:
- 1000+ records inserted
- correct distribution across banks
- no missing values in key columns

## Ethical Considerations

- Review data may suffer from negativity bias, as users are more likely to leave reviews after bad experiences.
- The dataset may not fully represent all users due to limited sampling from Google Play.
- Language and cultural differences may affect sentiment classification accuracy.
# Fintech Review Analytics

## Project Overview

This project collects and preprocesses Google Play Store reviews
from Ethiopian banking applications for sentiment analysis and analytics.

---
