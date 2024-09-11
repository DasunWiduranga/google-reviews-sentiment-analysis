
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def scrape_reviews(business_name_or_url):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    driver.get("https://www.google.com/maps")
    search_box = driver.find_element(By.ID, "searchboxinput")
    search_box.send_keys(business_name_or_url)
    search_box.submit()

    time.sleep(5)

    reviews = []
    try:
        review_elements = driver.find_elements(By.CLASS_NAME, "review-text")
        for review in review_elements:
            reviews.append(review.text)
    except Exception as e:
        print("Error:", e)

    driver.quit()
    return reviews
