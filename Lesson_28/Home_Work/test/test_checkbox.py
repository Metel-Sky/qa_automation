import pytest
from Lesson_28.Home_Work.CheckBoxPage import CheckboxPage


@pytest.mark.usefixtures("chrome_class")
class TestCheckboxPage:
    def setup(self):
        self.page = CheckboxPage(self.driver)

    def test_commands_folder_check(self):
        self.page.open()
        self.page.expand_folder('home')
        self.page.expand_folder('desktop')
        self.page.mark_folder('commands')
        result = self.page.get_result_check_folder()
        assert result == 'commands'

    def test_general_folder_check(self):
        self.page.open()
        self.page.expand_folder('home')
        self.page.expand_folder('documents')
        self.page.expand_folder('office')
        self.page.mark_folder('general')
        result = self.page.get_result_check_folder()
        assert result == 'general'