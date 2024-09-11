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
    try:
     
        data = request.json
        print(f"Received request data: {data}")

        business_name_or_url = data.get('businessName')

        # Validate input
        if not business_name_or_url:
            return jsonify({"error": "Business name or URL is required"}), 400
        
        
        reviews = scrape_reviews(business_name_or_url)
        
        
        if not reviews:
            return jsonify({"error": "No reviews found"}), 404
        
        
        categorized_reviews = analyze_sentiment(reviews)
        
       
        print(f"Sending response: {categorized_reviews}")

        return jsonify({"reviews": categorized_reviews}), 200
    except Exception as e:
     
        print(f"Error occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
