import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new WebDriver instance
driver = webdriver.Chrome()

# Navigate to Amazon.com
driver.get("https://www.amazon.com/")

# Find the search box element
search_box = driver.find_element(By.ID, "twotabsearchtextbox")

# Enter a search query
search_box.send_keys("laptops")

time.sleep(3)
# Find the search button element and click it
search_button = driver.find_element(By.XPATH, "//input[@value='Go']")
search_button.click()

# Close the WebDriver instance
driver.quit()