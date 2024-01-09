from Lesson_18.TextBoxPage import TextBoxPage
import time


class TestTextBox:

    def test_username_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_full_name_field("Pavlo")
        page.scroll_down()
        page.click_submit()
        name_field = page.get_result_fullname()
        assert name_field.replace("Name:", "") == "Pavlo"
        time.sleep(5)

    def test_email_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_email_field("djkif1212@gmail.com")
        page.scroll_down()
        page.click_submit()
        email_field = page.get_result_email()
        assert email_field.replace("Email:", "") == "djkif1212@gmail.com"
        time.sleep(5)

    def test_curr_addr_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_current_address_field("Якийсь адрес))")
        page.scroll_down()
        page.click_submit()
        curr_field = page.get_result_current_address()
        assert curr_field.replace("Current Address :", "") == "Якийсь адрес))"
        time.sleep(5)

    def test_perm_addr_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_permanent_address_field("Якийсь текст про море))")
        page.scroll_down()
        page.click_submit()
        perm_field = page.get_result_permanent_address()
        assert perm_field.replace("Permananet Address :", "") == "Якийсь текст про море))"
        time.sleep(5)
