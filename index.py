import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://oxylabs.io/blog")

results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content,features="html.parser")
driver.quit()

for i in soup.findAll(attrs = 'css-t5qeix enfzvtl0'):
    name = i.find('p')

    if name not in results:
        results.append(name.text)


print(results)