from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_reviews(business_name_or_url):
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
      
        driver.get("https://www.google.com/maps")
        
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "searchboxinput")))
        search_box = driver.find_element(By.ID, "searchboxinput")
        search_box.send_keys(business_name_or_url)
        search_box.submit()

        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "section-review-content")))

        
        for _ in range(5): 
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  
        
        
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
