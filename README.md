

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