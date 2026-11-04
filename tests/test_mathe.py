import foxtools.mathe as mathe
import pytest

def test_is_even():
    assert mathe.is_even(2)
    assert not mathe.is_even(3)
    assert mathe.is_even(0)
    assert mathe.is_even(-2)
    assert not mathe.is_even(-3)
    assert mathe.is_even(-4)

def test_percent():
    assert mathe.percent(50, 100) == 50
    assert mathe.percent(25, 100) == 25
    assert mathe.percent(0, 100) == 0
    assert mathe.percent(1, 4) == 25
    with pytest.raises(ValueError, match="Der Gesamtwert darf nicht 0 sein."):
        mathe.percent(1, 0)

def test_is_prime():
    assert mathe.is_prime(2)
    assert mathe.is_prime(3)
    assert not mathe.is_prime(4)
    assert mathe.is_prime(5)
    assert not mathe.is_prime(1)
    assert not mathe.is_prime(0)
    assert not mathe.is_prime(-1)
    assert not mathe.is_prime(-2)
    assert not mathe.is_prime(-3)

def test_clamp():
    c = mathe.Clamp(5, 0, 10)
    assert c.zahl == 5
    c.zahl = 7
    assert c.zahl == 7
    with pytest.raises(ValueError, match="Zahl ist nicht innerhalb der Begrenzungen."):
        c.zahl = 11
    with pytest.raises(ValueError, match="Zahl ist nicht innerhalb der Begrenzungen."):
        c.zahl = -1
    with pytest.raises(ValueError, match="Zahl ist nicht innerhalb der Begrenzungen."):
        mathe.Clamp(11, 0, 10)
    with pytest.raises(ValueError, match="Zahl ist nicht innerhalb der Begrenzungen."):
        mathe.Clamp(-1, 0, 10)