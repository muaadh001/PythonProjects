from bank import value
import pytest

def main():
    test_0()
    test_20()
    test_100()

def test_0():
    assert value("hello friend") == 0
    assert value("Hello") == 0
    assert value("Hello Friend") == 0
    assert value("HELLO FRIEND") == 0

def test_20():
    assert value("hi friend") == 20
    assert value("Hi") == 20
    assert value("heyyy") == 20
    assert value("hey") == 20
    assert value("Hey Friend!") == 20

def test_100():
    assert value("What's up?") == 100
    assert value("good morning") == 100







if __name__ == "__main__":
    main()
