import functions
import pytest

def test_add():
    assert functions.add(4, 5) == 9

def test_subtraction():
    assert functions.subtraction(4, 5) == -1
