import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import json

file_open = open("abc.json")
json_dict = json.load(file_open)
chrome_driver = webdriver.Chrome()
chrome_driver.maximize_window()
chrome_driver.implicitly_wait(20)
chrome_driver.get("https://www.zenclass.in")
chrome_driver.find_element(By.NAME, "email").send_keys(json_dict.get("likhithaemailid"))
chrome_driver.find_element(By.NAME, "password").send_keys(json_dict.get("likhithapasswd"))
time.sleep(30)