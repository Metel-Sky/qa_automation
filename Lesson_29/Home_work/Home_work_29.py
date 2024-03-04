# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def parse_olx():
    # Ініціалізація веб-драйвера (завантажте відповідний веб-драйвер для свого браузера)
    driver = webdriver.Chrome()

    try:
        # Відкриваємо сторінку ОЛХ
        driver.get("https://www.olx.ua/elektronika/telefony-i-aksesuary/mobilnye-telefony-smartfony/")

        # Чекаємо, поки сторінка повністю завантажиться
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "offer-wrapper")))

        # Отримуємо оголошення
        offers = driver.find_elements(By.CLASS_NAME, "offer-wrapper")

        # Записуємо назву та ціну кожного оголошення у файл
        with open("olx_results.txt", "w", encoding="utf-8") as file:
            for offer in offers:
                title = offer.find_element(By.CLASS_NAME, "linkWithHash").text
                price = offer.find_element(By.CLASS_NAME, "price").text
                file.write(f"Назва: {title}, Ціна: {price}\n")

        # Знаходимо і клікаємо на сторінку 2
        next_page_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/form/div[5]/div/section[1]/div/ul/li[2]")
        next_page_button.click()

        # Почекаємо, щоб сторінка 2 повністю завантажилася
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "offer-wrapper")))

        # Отримуємо оголошення на сторінці 2
        offers_page2 = driver.find_elements(By.CLASS_NAME, "offer-wrapper")

        # Записуємо назву та ціну кожного оголошення на сторінці 2 у файл
        for offer_page2 in offers_page2:
            title_page2 = offer_page2.find_element(By.CLASS_NAME, "linkWithHash").text
            price_page2 = offer_page2.find_element(By.CLASS_NAME, "price").text
            file.write(f"Назва: {title_page2}, Ціна: {price_page2}\n")

    finally:
        # Закриваємо вікно браузера
        driver.quit()


if __name__ == "__main__":
    parse_olx()
