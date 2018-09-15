from datetime import (datetime)
from helper_functions.helper_functions import next_hour


class CalendarSlot:
    """
    Each allocated slot of the Calender
    """
    def __init__(self, interviewers: list(), start_time: datetime, interviewee: str = ""):
        self.interviewers = interviewers
        self.interviewee = interviewee
        self.start_time = start_time
        self.end_time = next_hour(start_time)


class Calendar:
    """
    All the allocated slots in the interviews calender
    """
    def __init__(self):
        self.slots = list()

    def get_slots(self):
        return self.slots

    def add_slot(self, interviewers: list(), start_time: datetime, interviewee: str = ""):
        new_slot = CalendarSlot(interviewers=interviewers,
                                start_time=start_time,
                                interviewee=interviewee)
        self.slots.append(new_slot)

