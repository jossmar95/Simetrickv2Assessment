import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#  Implement a configuration to launch a test with Google Chrome and Firefox

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://www.amazon.com/")
time.sleep(3)
driver.quit()

driver = webdriver.Firefox()

driver.get("https://www.amazon.com/")
time.sleep(3)
driver.quit()
