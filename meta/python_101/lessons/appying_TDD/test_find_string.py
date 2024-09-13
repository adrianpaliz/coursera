from curses.ascii import isdigit
import find_string
import pytest

def test_is_present():
    assert find_string.is_present('Alfred')

def test_no_digit():
    assert find_string.no_digit('N7')


