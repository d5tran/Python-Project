from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://next.qa.bidsandtenders.ca")
driver.maximize_window()
current_url = driver.current_url

username = driver.find_element_by_id("username")
username.clear()
username.send_keys("testaccount@esolutionsgroup.ca")

password = driver.find_element_by_id("password")
password.clear()
password.send_keys("PassWord!")

domain = driver.find_element_by_id("domain")
domain.clear()
domain.send_keys("esolutions")


driver.find_element_by_id("loginButton").click()

driver.implicitly_wait(15)

elem = driver.find_element_by_xpath("//h4[@class='app-title-heading is-size-3']")



if elem.text.strip() == 'Welcome, Test Account':
     print("Successfully Logged in")
else:
    print("Unsuccessfully logged in")