from plates import is_valid
import pytest

def main():
    test_minmax()
    test_start2()
    test_mid()
    test_0()

def test_minmax():
    assert is_valid("AA") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFGH") == False

def test_start2():
    assert is_valid("AA") == True
    assert is_valid("B2") == False
    assert is_valid("2C") == False
    assert is_valid("69") == False

def test_mid():
    assert is_valid("BCD369") == True
    assert is_valid("BGD39A") == False

def test_0():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False


if __name__ == "__main__":
    main()
