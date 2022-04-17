import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:\Webdrivers\chromedriver.exe')
driver.get("https://hasaki.vn/")

print(driver.title)

input_search = driver.find_element(By.ID, 'search')
input_search.send_keys('merzy')
input_search.submit()

time.sleep(10)

driver.implicitly_wait(5)
products = driver.find_elements(By.CSS_SELECTOR, 'div.txt_color_1 > strong')
for p in products:
    print(p.text)

driver.quit()
