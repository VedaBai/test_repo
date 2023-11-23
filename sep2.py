# from selenium import webdriver
#
# my_driver = webdriver.Chrome()
# my_driver.get("https://www.google.com")

# from selenium import webdriver
# import time
#
# chrome_driver = webdriver.Chrome()
# chrome_driver.get("https://www.google.com")
# time.sleep(3)
# edge_driver = webdriver.Edge()
# edge_driver.get("https://www.google.com")
# time.sleep(3)

# from selenium import webdriver
# import time
#
# from selenium.webdriver.common.by import By
#
# chrome_driver = webdriver.Chrome()
# chrome_driver.get("https://www.w3schools.com/")
# time.sleep(5)
# menu_btn_container = chrome_driver.find_elements(By.ID, "footer")
# print(menu_btn_container)
#

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

chrome_driver = webdriver.Chrome()
chrome_driver.get("https://www.guvi.in")
time.sleep(10)
locator_element_click = chrome_driver.find_elements(By.ID, "HTML")
locator_element_click.click()
time.sleep(5)