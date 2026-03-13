import pytest
from project import *

def test_day():
    assert day("2026-02-24") == 24
    assert day("2026-02-25") == 25

def test_month():
    assert month("2026-02-24") == 2
    assert month("2026-06-25") == 6

def test_year():
    assert year("2002-10-24") == 2002
    assert year("2026-10-25") == 2026

def test_week():
    assert week("2026-10-24") == 43
    assert week("1990-07-24") == 30

def test_week_day():
    assert week_day("2026-10-24") == 5
    assert week_day("1990-07-24") == 1

def test_quarter():
    assert quarter("2026-10-24") == 4
    assert quarter("1990-07-24") == 3

def test_day_of_week():
    assert day_of_week("2026-10-24") == 'Saturday'
    assert day_of_week("1990-07-24") == 'Tuesday'

def test_day_of_year():
    assert day_of_year("2026-02-24") == 55
    assert day_of_year("1990-07-24") == 205
    assert day_of_year("2026-12-30") == 364

def test_is_date():
    assert is_date("2026-10-24") == True
    assert is_date("2026-02-31") == False
    assert is_date("2020-02-29") == True
    assert is_date("2026-13-24") == False

def test_date_part():
    assert date_part("2026-10-24") == 2026
    assert date_part("2026-10-25", 'month') == 10
    assert date_part("2026-10-25", 'day') == 25
    assert date_part("2026-10-24", 'week') == 43
    assert date_part("2026-10-25", 'quarter') == 4
    assert date_part("2026-10-24", 'week_day') == 5
    assert date_part("1969-10-25", 'year') == 1969

def test_date_name():
    assert date_name("2026-10-24") == 'October'
    assert date_name("2026-10-25", 'month') == 'October'
    assert date_name("2026-10-25", 'day') == '25'
    assert date_name("2026-10-24", 'day_of_week') == 'Saturday'
    assert date_name("2026-10-25", 'year') == '2026'


def test_date_trunc():
    assert date_trunc("2026-10-24") == '2026-01-01'
    assert date_trunc("2026-10-24", 'year') == '2026-01-01'
    assert date_trunc("2026-10-24", 'month') == '2026-10-01'
    assert date_trunc("2026-10-24", 'day') == '2026-10-24'

def test_end_of_month():
    assert end_of_month("2026-10-24") == '2026-10-31'
    assert end_of_month("2026-02-02") == '2026-02-28'

def test_start_of_month():
    assert start_of_month("2026-10-24") == '2026-10-01'
    assert start_of_month("2026-02-20") == '2026-02-01'

def test_date_format():
    assert date_format("2026-10-30", 'dd') == '30'
    assert date_format("2026-10-30", 'ddd') == 'Fri'
    assert date_format("2026-10-30", 'dddd') == 'Friday'
    assert date_format("2026-10-30", 'mm') == '10'
    assert date_format("2026-10-30", 'mmm') == 'Oct'
    assert date_format("2026-10-30", 'mmmm') == 'October'
    assert date_format("2026-10-30", 'yyyy-mm-dd') == '2026-10-30'
    assert date_format("2026-10-30", 'dd-mmm-yyyy') == '30 Oct, 2026'
    assert date_format("2026-10-30", 'dd-mmmm-yyyy') == '30 October, 2026'

def test_date_add():
    assert date_add("2026-03-12", 10, 'days') == '2026-03-22'
    assert date_add("2026-02-12", 10, 'months') == '2026-12-12'
    assert date_add("2026-03-12", 10, 'years') == '2036-03-12'

def test_date_diff():
    assert date_diff("2026-10-30", '2026-10-30', 'days') == 0
    assert date_diff("2026-10-30", '2026-10-10', 'days') == 20
    assert date_diff("2026-10-30", '2027-10-30', 'months') == 12
    assert date_diff("2026-10-30", '2025-10-30', 'months') == 12
    assert date_diff("2026-10-30", '2016-10-30', 'years') == 10


def test_errors():
    with pytest.raises(TypeError):
        day("2026-02-30"),
        month("2026-02-30"),
        year("2026-02-30"),
        week_day("2026-02-30"),
        is_date("2026-10-40"),
        date_part("2026-10-40"),
        date_part("2026-10-21", 'weekday'),
        date_name("2026-10-21", 'weekday')
