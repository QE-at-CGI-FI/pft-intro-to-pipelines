from model.eprimer import EPrimerPage
from helper.functions import Sample
import pytest
from playwright.sync_api import Page

class TestEPrimer:

    data = [
        ("to be or not be", "5", "2", "0"), 
        ("maaret's", 1, 0, 1), 
        ("to be " *1000, 2000, 1000, 0), 
        (Sample.this_is_sample(), 2, 0, 0),
        #bug: too many words
        #("to be or not to be - hamlet's dilemma", 8, 2, 1)
    ]
    ids=["hamlet", "maaret", "long text", "file"]

    @pytest.mark.parametrize("input_text, expect_1, expect_2, expect_3", data, ids=ids)
    def test_playwright(self, page_to_url, input_text, expect_1, expect_2, expect_3):
        EPrimerPage(page_to_url).fill_text_and_verify(input_text, expect_1, expect_2, expect_3)


