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

    def is_available(self):
        """
        :return: Boolean value; if the interviewee name is "", this means that this slot was not allocated yet
        """
        return not self.interviewee


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
        return new_slot

    def add_slots(self, interviewers: list(), start_times: list(), interviewee: str = ""):
        for time in start_times:
            self.add_slot(interviewers=interviewers,
                          start_time=time,
                          interviewee=interviewee)

    def get_available_slots(self):
        available_slots = list()
        for slot in self.slots:
            if slot.is_available():
                available_slots.append(slot)
        return available_slots

