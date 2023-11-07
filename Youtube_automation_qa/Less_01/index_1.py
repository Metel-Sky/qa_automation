from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()

browser.get("https://www.qa-practice.com/elements/button/simple")
# click_button = browser.find_element(By.ID, "submit-id-submit") # знаходить кнопку по айді
# sleep(2)
# click_button.click()
# sleep(3)

# click_button2 = browser.find_element(By.CLASS_NAME, "btn") # знаходить кнопку по класу
# sleep(2)
# click_button2.click()
# sleep(3)

# link = browser.find_element(By.LINK_TEXT, "Contact") # знаходить ссилку по тексту
# sleep(1)
# link.click()
#
# sleep(3)


sleep(1)
browser.find_element(By.LINK_TEXT, "Contact").click() # знаходить ссилку по тексту, але
                                                            #  без збереження у змінну
sleep(3)