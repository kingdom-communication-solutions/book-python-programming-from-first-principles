"""Tests for century(). Run them with:  python -m pytest test_museum.py"""
import pytest
from museum import century


@pytest.mark.parametrize("year, expected", [
    (1, 1),
    (100, 1),
    (101, 2),
    (1765, 18),
    (1800, 18),
    (1801, 19),
    (1900, 19),
    (1901, 20),
    (2025, 21),
])
def test_century_common_era(year, expected):
    assert century(year) == expected


@pytest.mark.parametrize("year, expected", [
    (-1, -1),
    (-100, -1),
    (-101, -2),
    (-202, -3),
    (-300, -3),
])
def test_century_before_common_era(year, expected):
    assert century(year) == expected
