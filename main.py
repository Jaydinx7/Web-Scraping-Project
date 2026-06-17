from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://github.com/search?q=python&type=repositories")

time.sleep(5)

driver.quit()