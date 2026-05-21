import pandas as pd
import re
import nltk

# import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from transformers import pipeline

from sklearn.feature_extraction.text import TfidfVectorizer

# -----------------------------------
# Load Dataset
# -----------------------------------

df = pd.read_csv("data/raw/fintech_reviews_cleaned.csv")

# Create review_id
df["review_id"] = range(1, len(df) + 1)

# -----------------------------------
# Text Preprocessing
# -----------------------------------

stop_words = set(stopwords.words("english"))

def preprocess_text(text):
    text = str(text).lower()

    # remove special characters
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    # tokenize
    tokens = word_tokenize(text)

    # remove stopwords
    tokens = [word for word in tokens if word not in stop_words]

    return " ".join(tokens)

df["cleaned_review"] = df["review"].apply(preprocess_text)

# -----------------------------------
# Sentiment Analysis
# -----------------------------------

classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def get_sentiment(text):
    try:
        result = classifier(text[:512])[0]

        label = result["label"]
        score = result["score"]

        # convert transformer labels
        if label == "POSITIVE":
            sentiment = "positive"
        else:
            sentiment = "negative"

        return pd.Series([sentiment, score])

    except:
        return pd.Series(["neutral", 0.0])

df[["sentiment_label", "sentiment_score"]] = (
    df["cleaned_review"]
    .apply(get_sentiment)
)

# -----------------------------------
# TF-IDF Keyword Extraction
# -----------------------------------

vectorizer = TfidfVectorizer(
    max_features=30,
    ngram_range=(1, 2)
)

X = vectorizer.fit_transform(df["cleaned_review"])

keywords = vectorizer.get_feature_names_out()

print("\nTop Keywords:")
print(keywords)

# -----------------------------------
# Theme Identification
# -----------------------------------

def identify_theme(text):

    text = text.lower()

    if any(word in text for word in [
        "login", "password", "access", "account"
    ]):
        return "Account Access Issues"

    elif any(word in text for word in [
        "slow", "transfer", "transaction", "loading"
    ]):
        return "Transaction Performance"

    elif any(word in text for word in [
        "ui", "design", "interface", "easy"
    ]):
        return "UI & User Experience"

    elif any(word in text for word in [
        "support", "help", "service"
    ]):
        return "Customer Support"

    else:
        return "General Feedback"

df["identified_theme"] = (
    df["cleaned_review"]
    .apply(identify_theme)
)

# -----------------------------------
# Final Dataset
# -----------------------------------

final_df = df[[
    "review_id",
    "review",
    "rating",
    "date",
    "bank",
    "sentiment_label",
    "sentiment_score",
    "identified_theme",
    "source"
]] 

# Save results
output_path = "data/raw/sentiment_analysis_results.csv"

final_df.to_csv(output_path, index=False)

print("\nAnalysis completed successfully.")
print(final_df.head())

# -----------------------------------
# Aggregation
# -----------------------------------

print("\nSentiment by Bank:")
print(
    df.groupby("bank")["sentiment_score"]
    .mean()
)

print("\nSentiment by Rating:")
print(
    df.groupby("rating")["sentiment_score"]
    .mean()
)