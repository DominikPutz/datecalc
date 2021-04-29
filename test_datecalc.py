import datetime

# unit_tests of datecalc functions
from datecalc import convert_string2datetime
from datecalc import convert_datetime2string
from datecalc import calc_time_difference


def test_convert_string2datetime():
    # Check if convert_string2datetime works as expected
    format = '%Y-%m-%d %H:%M:%S'
    datetime_string = '2021-03-05 12:44:22'
    # datetime(year, month, day, hour, minute, second)
    date_time_obj = datetime.datetime(2021, 3, 5, 12, 44, 22)
    assert convert_string2datetime(datetime_string, format) == date_time_obj


def test_convert_datetime2string():
    # Check if convert_datetime2string works as expected
    format = '%Y-%m-%d %H:%M:%S'
    # datetime(year, month, day, hour, minute, second)
    date_time_obj = datetime.datetime(2021, 3, 5, 12, 44, 22)
    datetime_string = '2021-03-05 12:44:22'
    assert convert_datetime2string(date_time_obj, format) == datetime_string


def test_calc_time_difference():
    # Check if calc_time_difference works as expected
    date_time_obj1 = datetime.datetime(2021, 3, 5, 12, 44, 22)
    date_time_obj2 = datetime.datetime(2021, 3, 25, 14, 23, 11)
    date_time_difference = datetime.timedelta(
        days=20, hours=1, minutes=38, seconds=50)
    assert calc_time_difference(
        date_time_obj1, date_time_obj2) == date_time_difference
