from selenium.webdriver.common.by import By

URL = "https://demoqa.com/checkbox"


class CheckboxPage:

    def open(self):
        self.driver.get(URL)
        return self

    def expand_folder(self, name):
        expand = self.driver.find_element(By.XPATH, f"//label[contains(@for, 'tree-node-{name}')]//ancestor::span/button")
        expand.click()

    def mark_folder(self, name):
        mark = self.driver.find_element(By.XPATH,f"//label[contains(@for, 'tree-node-{name}')]//*[contains(@class, 'rct-icon-uncheck')]")
        mark.click()

    def get_result_check_folder(self):
        result = self.driver.find_element(By.CSS_SELECTOR, 'span.text-success').text
        return result
