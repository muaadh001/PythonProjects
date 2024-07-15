from um import count
import pytest

def main():
    test_ulc()
    test_wwu()
    test_sbs()


def test_ulc():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2


def test_wwu():
    assert count("yummi") == 0


def test_sbs():
    assert count("Hello um world") == 1
    assert count("um?") == 1

if __name__ == "__main__":
    main()
