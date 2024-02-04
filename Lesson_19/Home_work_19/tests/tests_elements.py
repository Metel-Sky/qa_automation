from Lesson_19.ElementsPage import ElementsPage
import pytest


class TestElementsPage:

    @pytest.mark.parametrize("index, expected_element", [
        (0, 'Text Box'),
        (1, 'Check Box'),
        (2, 'Radio Button'),
        (3, 'Web Tables'),
        (4, 'Buttons'),
        (5, 'Links'),
        (6, 'Broken Links - Images'),
        (7, 'Upload and Download'),
        (8, 'Dynamic Properties'),
        (9, ''),
        (10, ''),
        (11, ''),
        (12, ''),
        (13, ''),
        (14, ''),
        (15, ''),
        (16, ''),
        (17, ''),
        (18, ''),
        (19, ''),
        (20, ''),
        (21, ''),
        (22, ''),
        (23, ''),
        (24, ''),
        (25, ''),
        (26, ''),
        (27, ''),
        (28, ''),
        (29, ''),
        (30, ''),
        (31, ''),
        (32, '')
    ])
    def test_page(self, chrome, index, expected_element):
        page = ElementsPage(chrome)
        page.open()
        elements = page.get_elements_page_categories()
        assert elements[index] == expected_element

    #  todo перевірити відповіді всіх 33 елементів в елементс за допомогою parametrise