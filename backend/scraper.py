from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_reviews(business_name_or_url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
     
        driver.get("https://www.google.com/maps")
        time.sleep(3)

       
        search_box = driver.find_element(By.ID, "searchboxinput")
        search_box.send_keys(business_name_or_url)
        search_box.submit()

        time.sleep(5)  

        reviews = []
        

        review_elements = driver.find_elements(By.CLASS_NAME, "jftiEf")  
        
        if not review_elements:
            return {"error": "No reviews found for the given business."}

        for element in review_elements:
            review_text = element.text
            reviews.append(review_text)

    except Exception as e:
        return {"error": str(e)}
    
    finally:
        driver.quit()

    return {"reviews": reviews}
