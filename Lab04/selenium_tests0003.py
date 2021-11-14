from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
#
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex

options = Options()
options.add_argument('--disable-notifications')
service = Service('C:/Users/Konrad/PycharmProjects/Metody_Numeryczne/PwZN/Lab04/chromedriver.exe')
driver = webdriver.Chrome(service = service, options = options)

driver.get('https://www.reddit.com/r/ChuckNorris/')

#button = driver.find_element(By.XPATH, '//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div[3]/button')
#button.click()

button = WebDriverWait(driver, 10).until(ex.presence_of_element_located((By.XPATH, '//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div[3]/button')))
button.click()