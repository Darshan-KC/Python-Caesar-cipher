import pytest
from caeser import Caeser

@pytest.fixture
def caeser():
    return Caeser(3)  # Use shift=3 for testing

def test_encrypt(caeser):
    assert caeser.encrypt("abc") == "def"
    assert caeser.encrypt("xyz") == "abc"
    assert caeser.encrypt("Hello") == "Khoor"
    assert caeser.encrypt("Python 3.11!") == "Sbwkrq 3.11!"

def test_decrypt(caeser):
    assert caeser.decrypt("def") == "abc"
    assert caeser.decrypt("abc") == "xyz"
    assert caeser.decrypt("Khoor") == "Hello"
    assert caeser.decrypt("Sbwkrq 3.11!") == "Python 3.11!"

def test_no_change_for_non_alphabetic(caeser):
    assert caeser.encrypt("1234567890") == "1234567890"
    assert caeser.decrypt("1234567890") == "1234567890"
    assert caeser.encrypt("!@#$%^&*()") == "!@#$%^&*()"
    assert caeser.decrypt("!@#$%^&*()") == "!@#$%^&*()"