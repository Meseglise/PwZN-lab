from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service('C:/Users/Konrad/PycharmProjects/Metody_Numeryczne/PwZN/Lab04/chromedriver.exe')
driver = webdriver.Chrome(service = service)

driver.get('http://www.fizyka.pw.edu.pl')

time.sleep(5)
driver.close()