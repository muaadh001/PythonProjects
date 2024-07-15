from jar import Jar


def test_in():
    jar = Jar()
    assert jar.capacity == 12
    jar_2 = Jar(3)
    assert jar2.capacity == 3


def test_str():
    jar = Jar()
    assert str(Jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(6)
    assert jar.size == 6
    jar.deposit(3)
    assert jar.size == 9


def test_withdraw():
    jar = Jar()
    jar.deposit(6)
    jar.withdraw(3)
    assert jar.size == 3
    jar.withdraw(1)
    assert jar.size == 2
