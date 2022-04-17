import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:\Webdrivers\chromedriver.exe')
driver.get("https://xemphim.club/")
# driver.get("https://xemphim.club/type/movie")

print(driver.title)

# element = driver.find_element(By.LINK_TEXT, 'Phim Bộ')
# driver.get(element.get_attribute('href'))
# element.click()
# time.sleep(1000)

element = driver.find_element(By.CLASS_NAME, 'button' and 'is-primary')
driver.get(element.get_attribute('href'))

email = driver.find_element(By.NAME, 'email')
email.send_keys('nguyenhoangn023@gmail.com')

pwd = driver.find_element(By.NAME, 'password')
pwd.send_keys('HoangNam32')
pwd.submit()

print("\nVI\n")
driver.implicitly_wait(3)
name_vi = driver.find_elements(By.CSS_SELECTOR, 'h3.vi > a')
for vi in name_vi:
    print(vi.text)

print("\nEN\n")
driver.implicitly_wait(3)
name_en = driver.find_elements(By.CSS_SELECTOR, 'h3.en > a')
for en in name_en:
    print(en.text)

# time.sleep(5)
driver.quit()
