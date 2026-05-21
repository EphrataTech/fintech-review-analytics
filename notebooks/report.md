# Final Submission Summary

## Scraping methodology

- The current analysis pipeline uses the dataset at data/raw/fintech_reviews_cleaned.csv.
- The repository contains a placeholder scripts/scrape_reviews.py file, but it is not implemented yet.
- Sentiment processing is performed in scripts/sentiment_analysis.py, which:
  - loads the cleaned review file,
  - preprocesses text by lowercasing, removing non-letter characters, tokenizing, and removing stopwords,
  - computes sentiment with the distilbert-base-uncased-finetuned-sst-2-english transformer,
  - saves results to data/raw/sentiment_analysis_results.csv.
- Visualization is produced by scripts/visualize_insights.py and saves charts such as sentiment_distribution.png.

## Data quality summary

- Total review records: 1477
- Missing values: none in review, rating, date, bank, or source
- Duplicate review texts: 343 duplicates found in the raw dataset
- Bank distribution:
  - Bank of Abyssinia: 498 reviews
  - Dashen Bank: 498 reviews
  - Commercial Bank of Ethiopia: 481 reviews
- Data quality concerns:
  - the dataset contains a substantial number of duplicate reviews,
  - there is no implemented scraper audit trail in the repository,
  - sentiment model confidence is high, raising the possibility of model bias.

## Early sentiment findings

- Sentiment counts from data/raw/sentiment_analysis_results.csv:
  - positive: 1040 reviews
  - negative: 437 reviews
- Average sentiment score: 0.966
- Average sentiment score by bank:
  - Bank of Abyssinia: 0.962
  - Dashen Bank: 0.967
  - Commercial Bank of Ethiopia: 0.968
- Average sentiment score by rating:
  - Rating 1: 0.971
  - Rating 2: 0.952
  - Rating 3: 0.954
  - Rating 4: 0.942
  - Rating 5: 0.968
- Key observation: the dataset is strongly skewed positive, and sentiment labels are highly confident.
- Visualization included: sentiment_distribution.png produced by scripts/visualize_insights.py.

## Blockers encountered

- scripts/scrape_reviews.py is currently empty, so the scraper implementation and its methodology are not defined in code.
- The submission report file notebooks/report.md was empty before this update.
- The current pipeline relies on an existing cleaned dataset rather than a complete end-to-end scraping pipeline.

## Plan for final submission

- Implement or document the scraping process in scripts/scrape_reviews.py so the methodology is reproducible.
- Add a short data audit step to deduplicate reviews and confirm review-source provenance.
- Expand visualizations with rating vs sentiment and theme frequency charts.
- Attach the completed report and referenced image files as part of the final upload.
