# import time
# from selenium import webdriver
# # from selenium.webdriver import ActionChains, Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(20)
# driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
# my_action = ActionChains(driver)
# source1 = driver.find_element(By.XPATH, "//div[text()='Oslo'][2]")
# target1 = driver.find_element(By.XPATH, "//div[text()='Norway']")
# my_action.drag_and_drop(source1, target1).perform()
# time.sleep(5)

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(20)
# driver.get("https://jqueryui.com/selectable/")
# my_action = ActionChains(driver)
# driver.switch_to.frame(0)
# item1 = driver.find_element(By.XPATH, "//*[text()='Item 1']//parent::li")
# item2 = driver.find_element(By.XPATH, "//*[text()='Item 2']//parent::li")
# my_action.key_down(Keys.CONTROL).click(item1).click(item2).perform()
# time.sleep(5)

#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(20)
# driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
#
# my_dropdown = Select(driver.find_element(By.ID, "RESULT_RadioButton-9"))
# result = my_dropdown.options
# my_dropdown.select_by_index(1)
# driver.get_screenshot_as_file("MorningSS.png")
# time.sleep(6)

# for x in result:
# print(x.text)


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver = webdriver.Chrome()
chrome_driver.maximize_window()
chrome_driver.implicitly_wait(20)
chrome_driver.get("https://demo.automationtesting.in/Windows.html")
chrome_driver.find_element(By.XPATH, "//button[text()='    click   ']").click()
print(chrome_driver.title)
time.sleep(5)
list_of_tabs = chrome_driver.window_handles
print(list_of_tabs)
window_one = list_of_tabs[0]
window_two = list_of_tabs[1]
chrome_driver.switch_to.window(window_one)
print(chrome_driver.title)
time.sleep(5)
chrome_driver.switch_to.window(window_two)
print(chrome_driver.title)
time.sleep(5)
