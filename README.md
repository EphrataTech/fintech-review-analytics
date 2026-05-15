# Fintech Review Analytics

## Project Overview

This project collects and preprocesses Google Play Store reviews
from Ethiopian banking applications for sentiment analysis and analytics.

---

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