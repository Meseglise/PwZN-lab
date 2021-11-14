from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex
import time
import argparse
import json

def scroll():
    for i in range(40):
        driver.execute_script('window.scrollTo(0, window.scrollY + 300)')
        time.sleep(2)
    driver.execute_script('window.scrollTo(0, 0)')

def catalog():
    time.sleep(1)
    button1.click()
    time.sleep(1)

def readt():
    threads = driver.find_elements(By.CLASS_NAME, 'thread')
    for thread in threads:
        # print(driver.find_element(By.CLASS_NAME, 'teaser'))
        x.append(f"Thread Topic: {driver.find_element(By.CLASS_NAME, 'teaser')}")
        # print(x)

def savet():
    with open(args.j1, 'w') as f:
        json.dump(x, f)

x = []
parser = argparse.ArgumentParser(description = "Arguments description")
parser.add_argument('-url', '--u1', help = 'page url', default = 'https://boards.4channel.org/x/')
parser.add_argument('-path', '--p1', help = 'exe path', default = 'C:/Users/Konrad/PycharmProjects/Metody_Numeryczne/PwZN/Lab04/chromedriver.exe')
parser.add_argument('-file', '--j1', help = 'json file', default = 'lab04.json')
args = parser.parse_args()

service = Service(args.p1)
driver = webdriver.Chrome(service = service)
driver.get(args.u1)

button1 = driver.find_element(By.XPATH, '//*[@id="ctrl-top"]/a[1]')
#button2 = driver.find_element(By.CSS_SELECTOR, '#refresh-btn')


catalog()
scroll()
readt()
savet()

