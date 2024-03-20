from Lesson_28.TextBoxPage import TextBoxPage


class TestTextBox:

    def test_username_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_full_name_field('Artem')
        page.scroll_down()
        page.click_submit()
        name_field = page.get_result_fullname()
        assert name_field.replace('Name:', '') == 'Artem'

    def test_email_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_email_field('kh11tko@gmail.com')
        page.scroll_down()
        page.click_submit()
        result_email = page.get_result_email()
        assert result_email.replace('Email:', '') == "kh11tko@gmail.com"

    def test_curr_addr_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_current_address_field('First avenue')
        page.scroll_down()
        page.click_submit()
        result_curr_addr = page.get_result_current_address()
        assert result_curr_addr.replace('Current Address :', '') == 'First avenue'

    def test_perm_addr_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_permanent_address_field('Five avenue')
        page.scroll_down()
        page.click_submit()
        result_perm_addr = page.get_result_permanent_address()
        assert result_perm_addr.replace('Permananet Address :', '') == 'Five avenue'
