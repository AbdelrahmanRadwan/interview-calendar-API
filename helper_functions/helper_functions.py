from datetime import (datetime, timedelta, )
from dateutil.parser import parse


def next_hour(current_date):
    return current_date + timedelta(hours=1)


def print_datetime_slot_info(date_time):
    datetime(2009, 10, 5, 18, 00)
    day_name = date_time.strftime("%A")
    date = date_time.date()
    start_time = date_time.strftime('%H:%M:%S')
    print("{} {} from {}.".format(day_name, date, start_time))


def string_to_datetime(date_time_string):
    return parse(date_time_string)


def datetime_to_string(date_time_string):
    return date_time_string.strftime("%Y-%m-%d %H:%M:%S")
