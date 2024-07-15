from fuel import convert, gauge
import pytest

def main():
    test_input()
    test_zerodivisionerror()
    test_valueerror()

def test_input():
    assert convert("1/4") == 25 and gauge(25) == "25%"
    assert convert("99/100") == 99 and gauge(99) == "F"
    assert convert("1/100") == 1 and gauge(1) == "E"

def test_zerodivisionerror():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_valueerror():
    with pytest.raises(ValueError):
        convert("dog/cat")

if __name__ == "__main__":
    main()
