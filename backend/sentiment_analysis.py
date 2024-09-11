
from textblob import TextBlob

def analyze_sentiment(reviews):
    categorized_reviews = {
        'positive': [],
        'negative': [],
        'neutral': []
    }

    for review in reviews:
        analysis = TextBlob(review).sentiment.polarity
        if analysis > 0:
            categorized_reviews['positive'].append(review)
        elif analysis < 0:
            categorized_reviews['negative'].append(review)
        else:
            categorized_reviews['neutral'].append(review)

    return categorized_reviews
