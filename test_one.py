def test_example(page):
    page.goto("https://exploratorytestingacademy.com/app")
    assert page.title() != None