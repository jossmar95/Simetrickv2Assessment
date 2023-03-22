# Exercise Number 5 Get text

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(options=options)

# URL goes here
driver.get("")

# CSS Selector
# driver.find_element(By.CSS_SELECTOR, ".container.mx-auto.max-w-4xl h2:nth-of-type(2)").text
# driver.find_element(By.CSS_SELECTOR, ".container.mx-auto.max-w-4xl p:nth-of-type(2)").text

