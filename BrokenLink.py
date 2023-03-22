from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

driver = webdriver.Chrome()
# provide website url here
driver.get("http://demo.guru99.com/test/newtours/")

# get all links
all_links = driver.find_elements(By.CSS_SELECTOR, "a")

for link in all_links:

    url = link.get_attribute('href')

    result = requests.head(url)

    if result.status_code != 200:
        print(url, result.status_code)

