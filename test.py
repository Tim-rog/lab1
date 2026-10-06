from toolkit.calc import calculate
from toolkit.values import translate


def test_plus():
    assert calculate('2+2') == 4
    assert calculate('5+5+13342+53') == 13405


def test_minus():
    assert calculate(' -2 + -3 + -56') == -61
    assert calculate('-23--46-5') == 18
    assert calculate('-435*-0.5') == 217.5


def test_piz():
    assert calculate('(12+8)*3-40/5+2') == 54
    assert calculate('3*(4+5*(6-2))-10') == 62
    assert calculate('10*(2+3)-(4*5)+6/2') == 33


def test_trans():
    assert float(translate('1kg', 'g')) == 1000
    assert calculate('100g + 2.2kg') == 2300


def test_mass():
    assert float(translate('1kg', 'g')) == 1000
    assert float(translate('100g', 'kg')) == 0.1
    assert float(translate('1000mg', 'g')) == 1
    assert float(translate('2.5kg', 'g')) == 2500
    assert float(translate('500g', 'kg')) == 0.5
    assert float(translate('0kg', 'g')) == 0
    assert float(translate('100kg', 'kg')) == 100


def test_length():
    assert float(translate('100cm', 'm')) == 1
    assert float(translate('1m', 'cm')) == 100
    assert float(translate('10km', 'm')) == 10000
    assert float(translate('10km', 'mm')) == 10_000_000
    assert float(translate('1m', 'mm')) == 1000
    assert float(translate('250cm', 'm')) == 2.5
    assert float(translate('1.5km', 'm')) == 1500
    assert float(translate('50m', 'm')) == 50


def test_temp_k_c():
    assert float(translate('0K', 'C')) == -273.15
    assert float(translate('273.15K', 'C')) == 0
    assert float(translate('373.15K', 'C')) == 100
    assert float(translate('100K', 'C')) == 100 - 273.15
    assert float(translate('0C', 'K')) == 273.15
    assert float(translate('100C', 'K')) == 373.15


def test_temp_f_c():
    assert float(translate('32F', 'C')) == 0
    assert float(translate('212F', 'C')) == 100
    assert float(translate('0C', 'F')) == 32
    assert float(translate('100C', 'F')) == 212
    assert float(translate('-40F', 'C')) == -40
    assert float(translate('-40C', 'F')) == -40


def test_temp_same():
    assert float(translate('100C', 'C')) == 100
    assert float(translate('300K', 'K')) == 300
    assert float(translate('77F', 'F')) == 77


def test_temp_cross():
    assert float(translate('32F', 'K')) == 273.15
    assert float(translate('273.15K', 'F')) == 32
    assert float(translate('100C', 'F')) == 212
    assert float(translate('212F', 'K')) == 373.15


def test_floats_mixed():
    assert float(translate('0.5kg', 'g')) == 500
    assert float(translate('3.25m', 'cm')) == 325
    assert float(translate('2.5C', 'K')) == 2.5 + 273.15


def test_calc_units():
    assert calculate('100g + 2.2kg') == 2300
    assert calculate('1kg - 200g') == 800
    assert calculate('2m + 50cm') == 2.5