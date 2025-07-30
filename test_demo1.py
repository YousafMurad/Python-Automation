import pytest

def test_m1():
    a = 3
    b = 5
    assert a+1 == b, "test failed"
    assert a == b, "test failed, as a =! b"

def test_m2():
    name = "selenium"
    assert name.upper() == "Selenium"

def test_m3():
    assert True

def test_m4():
    assert False

def test_m5():
    assert 100 == 100

def test_m6():
    assert "naveen" == "NAVEEN"

def test_login():
    assert "admin"=="admin123"