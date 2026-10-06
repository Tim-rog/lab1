import pytest
from toolkit.calc import calculate


def test_plus():
    assert calculate('2+2') == 4


def test_pizdec():
    assert  calculate('(12+8)*3-40/5+2') == 54