from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

columns = ["Component","Product Name","Brand", "Current Price","Old Price","Discount Amount","Stock Status"]

def item_details(item):
    details = item.text.split('\n')
    contents = {}
    contents["Component"] = "Processor"
    contents["Product Name"] = details[1] if len(details) > 1 else ""
    contents["Brand"] = details[1].split(' ')[0] if len(details) > 1 else ""
    contents["Current Price"] = details[2] if len(details) > 2 else ""
    contents["Old Price"] = details[3] if len(details) > 3 else ""
    contents["Discount Amount"] = details[0].replace('Save : ','') if len(details) > 0 else ""
    contents["Stock Status"] = details[4] if len(details) > 4 else "Out of Stock"
    return contents
    
def main():

    data_item =[]
    for page_id in range(1,5):

        url = f"https://www.techlandbd.com/pc-components/processor?page={page_id}"
        driver = webdriver.Chrome()
        driver.get(url)
        items = driver.find_elements(By.XPATH, "//div[@id='product-container']/article")
        
    
        for item in items:
          data_item.append(item_details(item))
          time.sleep(5)    
        driver.close()

    df = pd.DataFrame(data=data_item, columns=columns)
    df.to_csv("processor_details.csv", index=False)
        
    return

if __name__ == "__main__":
    main() 