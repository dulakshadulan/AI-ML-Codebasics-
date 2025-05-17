import mathlib
import pytest

@pytest.mark.parametrize("a,b,expected_output",
                        [
                            (2,3,5),
                            (5,7,12)
                        ])
def test_calc_total_1(a,b,expected_output):
    result = mathlib.calc_total(a,b)
    assert result == expected_output 
    