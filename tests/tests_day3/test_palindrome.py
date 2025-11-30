from programs.day3.palindrome import palindrome

def test_palindrome_string():
    assert palindrome("Madam") is True
    assert palindrome("hello") is False

def test_palindrome_number():
    assert palindrome("123321") is True
    assert palindrome("12345") is False
