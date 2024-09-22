from flask import Flask, request, jsonify
from flask_cors import CORS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

app = Flask(__name__)
CORS(app) 

def scrape_reviews(business_name_or_url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    reviews = []
    
    try:
        
        driver.get("https://www.google.com/maps")
        time.sleep(3)

       
        search_box = driver.find_element(By.ID, "searchboxinput")
        search_box.send_keys(business_name_or_url)
        search_box.submit()

        time.sleep(5)  

       
        review_elements = driver.find_elements(By.CLASS_NAME, "jftiEf")  

        if not review_elements:
            return {"error": "No reviews found for the given business."}

        for element in review_elements:
            review_text = element.text
            reviews.append({"text": review_text, "sentiment": "positive"})  # Placeholder sentiment
        
    except Exception as e:
        return {"error": str(e)}
    
    finally:
        driver.quit()

    return {"reviews": reviews}

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.get_json()
    business_name = data.get("businessName")
    
    if not business_name:
        return jsonify({"error": "Business name is required"}), 400

    print(f"Scraping reviews for: {business_name}")
    
    reviews = scrape_reviews(business_name)
    
    print(f"Scraped Reviews: {reviews}")
    return jsonify(reviews)

if __name__ == '__main__':
    app.run(debug=True)
