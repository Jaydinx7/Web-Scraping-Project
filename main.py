from re import search

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
print("|======================|")
print("| WELCOME TO GITSCRAPE |")
print("|======================|\n\n")

search = input("What are you searching on GitHub?: ").lower().strip()

driver.get("https://github.com/search?q="+search+"&type=repositories")

time.sleep(5)

driver.quit()