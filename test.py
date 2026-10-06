import pytest
from toolkit.calc import calculate
from toolkit.values import translate


def test_plus():
    assert calculate('2+2') == 4


def test_pizdec():
    assert calculate('(12+8)*3-40/5+2') == 54
    assert calculate('3*(4+5*(6-2))-10') == 62
    assert calculate('10*(2+3)-(4*5)+6/2') == 33


def test_trans():
    assert translate('1kg', 'g') == 1000


def test_trans2():
    assert translate('100cm', 'm') == 1
    assert translate('100K', 'C') == 100-273.15
    assert translate('10km', 'mm') == 10*1000*1000