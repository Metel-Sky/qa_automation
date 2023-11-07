from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()

browser.get("https://www.qa-practice.com/elements/button/simple")
click_button = browser.find_element(By.ID, "submit-id-submit")
sleep(3)
click_button.click()

sleep(5)