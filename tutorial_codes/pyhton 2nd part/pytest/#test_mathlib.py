import mathlib
import pytest
import sys

def test_calc_subtract():
    result = mathlib.calc_subtract(4,3)
    assert result == 1

# just skip test

@pytest.mark.skip(reason="skip this")
def test_calc_total():
    total = mathlib.calc_total(4,5)
    assert total == 9

# skip if

@pytest.mark.skipif(sys.version_info > (3,5),reason="skip this too" )
def test_calc_multiply():
    result = mathlib.calc_multiply(10,2)
    assert result == 20

def test_calc_divide():
    result = mathlib.calc_divide(4,2)
    assert result == 2

@pytest.mark.windows
def test_windows_1():
    assert True

@pytest.mark.windows
def test_windows_2():
    assert True

@pytest.mark.mac
def test_mac_1():
    assert True

@pytest.mark.mac
def test_mac_2():
    assert True


# run  python -m pytest or python -m pytest -v  in cmd pytest -v
# python -m pytest -rxs to get skipped reason
# pytest -k word_you_want  (test a func that has a selected word) 
# pytest -m mac -v to run selected marker


