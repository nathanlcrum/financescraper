from selenium import webdriver
import time
from bs4 import BeautifulSoup


driver = webdriver.Chrome()
url = 'https://finance.yahoo.com/quote/HOG?p=HOG'
driver.maximize_window()
driver.get(url)

time.sleep(5)
content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content,"html.parser")
officials = soup.findAll("span",{"data-reactid":"34"})

for entry in officials:
    print(str(entry))


driver.quit()
