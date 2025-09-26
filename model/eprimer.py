import allure
from playwright.sync_api import Page, expect

class EPrimerPage:

    def __init__(self, p: Page):
        self.p = p

    _text_input = "#test_field"
    _test_button = "#test_button"
    _number_1 = "#test_number_1"
    _number_2 = "#test_number_2"
    _number_3 = "#test_number_3"

    @allure.step("Fill text input and verify outputs")
    def fill_text_and_verify(self, input_text, expect_1, expect_2, expect_3):
        self.p.fill(self._text_input, input_text)
        self.p.click(self._test_button)
        expect(self.p.locator(self._number_1)).to_have_text(str(expect_1))
        expect(self.p.locator(self._number_2)).to_have_text(str(expect_2))
        expect(self.p.locator(self._number_3)).to_have_text(str(expect_3))
