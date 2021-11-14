from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service('C:/Users/Konrad/PycharmProjects/Metody_Numeryczne/PwZN/Lab04/chromedriver.exe')
driver = webdriver.Chrome(service = service)

driver.get('https://www.fizyka.pw.edu.pl/Pracownicy/Lista-pracownikow/Pracownicy-badawczo-dydaktyczni')

elements = driver.find_elements(By.CSS_SELECTOR, 'h2, h2+div')
for element in elements:
    print(element.text)
#time.sleep(5)
#driver.close()