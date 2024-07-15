
from twttr import shorten

def main():
    test_upper_lc()
    test_no()
    test_punct()

def test_upper_lc():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("TwiTteR") == "TwTtR"

def test_no():
    assert shorten("1234") == "1234"

def test_punct():
    assert shorten("?!.,") == "?!.,"


