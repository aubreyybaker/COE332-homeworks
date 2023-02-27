from analyze_water import turbitityCalculation, turbThreshold
import pytest

def test_turbitityCalculation():
    assert turbitityCalculation(2, 3) == 6

def test_turbThreshold():
    assert turbThreshold(2, 1.96) == 1
