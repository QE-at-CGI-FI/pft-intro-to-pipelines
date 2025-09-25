from model.eprimer import EPrimerPage
from helper.functions import Sample
import pytest
class TestEPrimer:

    data = [
        ("I went to work.", 4, 0, 0),
        ("I want to be at work.", 6, 1, 0),
        ("I am at work. You are at work. He is at work.", 12, 3, 0),
        ("to be or not be", "5", "2", "0"), 
        ("maaret's", 1, 0, 1), 
        ("to be " *1000, 2000, 1000, 0), 
        (Sample.this_is_sample(), 2, 0, 0),
        ("<script>alert(0)</script>", 1, 0, 0),
        ("", 0, 0, 0),
        ("be, being, been, am, is, isn't, are, aren't, was, wasn't, were, and weren't.", 13, 12, 0),
        ("The cat is my only pet.", 6, 1, 0), 
        ("Garfield is a cat.", 4, 1, 0), 
        ("A cat is an animal.", 5, 1, 0), 
        ("The cat is furry.", 4, 1, 0), 
        ("The cat is theirs.", 4, 1, 0), 
        ("The cat is sleeping.", 4, 1, 0),
        ("The cat is being bitten by the dog.", 8, 2, 0),
        ("There is a cat.", 4, 1, 0),
        ("The cat is nowhere to be found.", 7, 2, 0), 
        ("typewriter's", 1, 0, 1),
        ('"be"', 1, 1, 0),
        ("<div>be</div>", 1, 1, 0), 

    ]
    ids=["past tense", "close spelling", "basic grammar", "hamlet", 
         "possessive maaret", "long text", "file", "html", "empty", "various", 
         "identity", "class membership", "class inclusion", "predication", "ownership", "auxiliary progressive", 
         "auxiliary passive", "existence", "location", "typewriter apostrophe", "doublequoted be", "html be"]

    data_revealing_bugs = [
        ("To be or not to be – Hamlet’s dilemma", 8, 2, 1),
        (Sample.this_is_bible(), 31172, 18, 1),
        ("'s", 1, 0, 0),
        ("maaret's friends' house", 3, 0, 2), 
        ("I'm, we're, you're, he's, she's, it's, they're, there's, here's, where's, when's, why's, how's, who's, what's, and that's", 17, 4, 12),
        ("The electron functions as a particle.", 6, 1, 0),
        ("being", 1, 1, 0),
        ("typesetter’s", 1, 0, 1),
        ("I'm", 2, 1, 0), 
        ("'Be'", 1, 1, 0),
        ("\n", 1, 0, 0),
        ("first\nsecond", 1, 0, 0),
        ("ain't, amn't", 2, 2, 0),
        ("Hanna's Esa's Meera's Süëss-O'Reggio's or Okechukwu's", 6, 0, 4),

    ]
    ids_revealing_bugs=["bug_incorrect_word_count", "bug bible incorrect word count", "bug possessive ending", 
                        "bug plural possessive ending", "bug all contractions", "whats a word", "dual meaning", 
                        "typesetter apostrophe", "counting words", "singlequoted be", "newline", "newline with text", 
                        "nonstandard contractions", "two part names" ]

    @pytest.mark.parametrize("input_text, expect_1, expect_2, expect_3", data, ids=ids)
    def test_ones_that_work(self, page_to_url, input_text, expect_1, expect_2, expect_3):
        EPrimerPage(page_to_url).fill_text_and_verify(input_text, expect_1, expect_2, expect_3)

    @pytest.mark.parametrize("input_text, expect_1, expect_2, expect_3", data_revealing_bugs, ids=ids_revealing_bugs)
    def test_ones_with_bugs(self, page_to_url, input_text, expect_1, expect_2, expect_3):
        EPrimerPage(page_to_url).fill_text_and_verify(input_text, expect_1, expect_2, expect_3)
