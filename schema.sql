
CREATE TABLE banks (
    bank_id SERIAL PRIMARY KEY,
    bank_name VARCHAR(255),
    app_name VARCHAR(255)
);

CREATE TABLE reviews (
    review_id INT PRIMARY KEY,
    bank_id INT REFERENCES banks(bank_id),
    review_text TEXT,
    rating INT,
    review_date DATE,
    sentiment_label VARCHAR(50),
    sentiment_score FLOAT,
    identified_theme VARCHAR(255),
    source VARCHAR(50)
);