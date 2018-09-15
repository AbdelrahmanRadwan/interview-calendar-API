from datetime import (datetime, timedelta, )
from dateutil.parser import parse


def next_hour(current_date):
    """
    Get the hour next to the current one
    :param current_date: datetime object of the current moment
    :return: datetime object of one hour far from the current datetime
    """
    return current_date + timedelta(hours=1)


def get_datetime_slot_info(date_time):
    """
    get a well formatted string to represent specific datetime object
    :param date_time: datetime formatted object
    :return: well formatted string represents the day
    """
    datetime(2009, 10, 5, 18, 00)
    day_name = date_time.strftime("%A")
    date = date_time.date()
    start_time = date_time.strftime('%H:%M:%S')
    return "{} {} from {}.".format(day_name, date, start_time)


def string_to_datetime(date_time_string):
    """
    transform the datetime string to object
    :param date_time_string: datetime in string format
    :return: datetime in datetime format
    """
    return parse(date_time_string)


def datetime_to_string(date_time):
    """
    convert datetime object to a string
    :param date_time: datetime in datetime format
    :return: datetime in string format
    """
    return date_time.strftime("%Y-%m-%d %H:%M:%S")
