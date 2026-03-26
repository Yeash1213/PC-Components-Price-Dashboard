from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

columns = ["Component","Product Name","Brand", "Current Price","Old Price","Discount Amount","Stock Status"]

def item_details(item):
    details = item.text.split('\n')
    contents = {}
    contents["Component"] = "Graphics Card"
    contents["Product Name"] = details[1] if len(details) > 1 else ""
    contents["Brand"] = details[1].split(' ')[0] if len(details) > 1 else ""
    contents["Current Price"] = details[2] if len(details) > 2 else ""
    contents["Old Price"] = details[3] if len(details) > 3 else ""
    contents["Discount Amount"] = details[0].replace('Save : ','') if len(details) > 0 else ""
    contents["Stock Status"] = details[4] if len(details) > 4 else "Out of Stock"
    return contents
    
def main():

    data_item =[]
    driver = webdriver.Chrome()

    for page_id in range(1,22):

        url = f"https://www.techlandbd.com/pc-components/graphics-card?page={page_id}"
        driver = webdriver.Chrome()
        driver.get(url)
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='product-container']/article"))
            )
        except:
            print(f"Page {page_id}: Timed out or no products found, skipping...")
            continue
        items = driver.find_elements(By.XPATH, "//div[@id='product-container']/article")
        
    
        for item in items:
          data_item.append(item_details(item))
          time.sleep(1)   

        driver.quit()

    df = pd.DataFrame(data=data_item, columns=columns)
    df.to_csv("gpu_details2.csv", index=False)
        
    return

if __name__ == "__main__":
    main() 