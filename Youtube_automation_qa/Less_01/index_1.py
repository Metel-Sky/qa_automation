from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://www.qa-practice.com/elements/button/simple")

browser.find_element(By.ID, "submit-id-submit")



# sleep(5)