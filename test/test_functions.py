from pytest import approx
from modules.user_functions import *

# Functions to test user defined functions.

def test_total():
    assert total([5,5,4,3,1,5,6]) == 29
    
def test_mean():
    assert mean([5,5,4,3,1,5,6]) == 4.14

def test_median():
    assert median([5,5,4,3,1,5,6]) == 5

def test_mode():
    assert mode([5,5,4,3,1,5,6]) == 5

def test_maximum():
    assert maximum([5,5,4,3,1,5,6]) == 6

def test_minimum():
    assert minimum([5,5,4,3,1,5,6]) == 1

def test_ranges():
    assert ranges([5,5,4,3,1,5,6]) == 5

def test_iqr():
    assert iqr([5,5,4,3,1,5,6]) == 2

def test_standard_deviation():
    assert standard_deviation([5,5,4,3,1,5,6]) == 1.68

def test_squared_deviations():
    assert squared_deviations([5,5,4,3,1,5,6]) == [0.7396000000000006,
    0.7396000000000006,
    0.01959999999999991,
    1.2995999999999992,
    9.859599999999999,
    0.7396000000000006,
    3.4596000000000013]

def test_median_skewness():
    assert median_skewness([5,5,4,3,1,5,6]) == approx(-1.54, 0.01)

def test_mode_skewness():
    assert mode_skewness([5,5,4,3,1,5,6]) == approx(-0.51, 0.01)

def test_correlation_coefficient():
    assert correlation_coefficient([5,5,4,3,1,5,6], [1,3,2,1,1,2,1]) == 0.3




