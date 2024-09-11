
from flask import Flask, request, jsonify
from flask_cors import CORS
from sentiment_analysis import analyze_sentiment
from scraper import scrape_reviews


app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Welcome to the Google Reviews Scraper API"

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.json
    business_name_or_url = data.get('businessName')
    reviews = scrape_reviews(business_name_or_url)
    categorized_reviews = analyze_sentiment(reviews)
    return jsonify(categorized_reviews)

if __name__ == '__main__':
    app.run(debug=True)
