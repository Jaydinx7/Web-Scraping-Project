from re import search

import pandas
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("|======================|")
print("| WELCOME TO GITSCRAPE |")
print("|======================|\n\n")

search = input("What are you searching on GitHub?: ").lower().strip()

driver = webdriver.Chrome()

driver.get("https://github.com/search?q="+search+"&type=repositories")

time.sleep(5)

repo_elements = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='results-list'] div.search-title a")

scraped_data = []

for repo in repo_elements:
    try:
        # Get the Repo name
        repo_name = repo.text

        # Gets Repo Url
        repo_url = repo.get_attribute('href')

        if repo_name:
            scraped_data.append({
                "Repository": repo_name,
                "URL": repo_url
            })

    except Exception as e:
        continue

for s in scraped_data:
    print(s)

df = pandas.DataFrame(scraped_data)

df.to_csv('REPO.csv', index=False)
driver.quit()
