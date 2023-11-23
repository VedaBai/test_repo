import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver = webdriver.Chrome()
chrome_driver.maximize_window()
chrome_driver.implicitly_wait(20)
chrome_driver.get("https://www.zenclass.in/login")
chrome_driver.find_element(By.NAME, "email").send_keys("vedagsvl@gmail.com")
chrome_driver.find_element(By.NAME, "password").send_keys("Vedaganesh@24")
chrome_driver.find_element(By.XPATH, "//*[@type='submit']").click()
time.sleep(20)