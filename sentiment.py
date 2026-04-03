import pandas as pd

data = pd.read_csv("reviews.csv")

# Simple sentiment classification
data['sentiment'] = data['rating'].apply(lambda x: "Positive" if x >= 3 else "Negative")

print(data[['cleaned_review_text', 'sentiment']].head())
