import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://testautomationpractice.blogspot.com/")
alert = Alert(driver)
driver.find_element(By.XPATH, "//button[text()='Alert']").click()
print(alert.text)
alert.accept()
driver.find_element(By.XPATH, "//button[text()='Confirm Box']").click()
print(alert.text)
alert.dismiss()
driver.find_element(By.XPATH, "//button[text()='Prompt']").click()
print(alert.text)
alert.send_keys("my name is veda")
time.sleep(20)
alert.accept()
alert = driver.switch_to.alert
