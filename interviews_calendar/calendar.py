import sys
import os

from datetime import (datetime)

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from helper_functions.helper_functions import (next_hour, string_to_datetime,
                                               get_datetime_slot_info)


class CalendarSlot:
    """
    Each allocated slot of the Calender
    """
    def __init__(self, interviewers: list(), start_time: datetime, interviewee: str = ""):
        """

        :param interviewers:
        :param start_time:
        :param interviewee:
        """
        self.interviewers = interviewers
        self.interviewee = interviewee
        self.start_time = start_time
        self.end_time = next_hour(start_time)

    def serialize(self):
        """

        :return:
        """
        response = dict()
        response["interviewers"] = self.interviewers
        response["interviewee"] = self.interviewee
        response["start_time"] = get_datetime_slot_info(self.start_time)
        response["end_time"] = get_datetime_slot_info(self.end_time)

        return response

    def is_available(self):
        """

        :return: Boolean value; if the interviewee name is "", this means that this slot was not allocated yet
        """
        return not self.interviewee

    def set_interviewee(self, interviewee: str):
        """

        :return: Boolean value; if the interviewee name is "", this means that this slot was not allocated yet
        """
        self.interviewee = interviewee

    def in_time_range(self, start_time: datetime, end_time: datetime):
        """

        :param start_time:
        :param end_time:
        :return:
        """
        return end_time >= self.start_time >= start_time


class Calendar:
    """
    All the allocated slots in the interviews calender
    """
    def __init__(self):
        """

        """
        self.slots = list()

    def get_slots(self):
        """

        :return:
        """
        slots = []
        for slot in self.slots:
            slots.append(slot.serialize())
        return slots

    def add_slot(self, interviewers: list(), start_time: datetime, interviewee: str = ""):
        """

        :param interviewers:
        :param start_time:
        :param interviewee:
        :return:
        """
        new_slot = CalendarSlot(interviewers=interviewers,
                                start_time=start_time,
                                interviewee=interviewee)
        self.slots.append(new_slot)
        return new_slot.serialize()

    def add_slots(self, interviewers: list(), start_times: list(), interviewee: str = ""):
        """

        :param interviewers:
        :param start_times:
        :param interviewee:
        :return:
        """
        added_slots = []
        for time in start_times:
            time = string_to_datetime(time)
            new_slot = self.add_slot(interviewers=interviewers,
                                     start_time=time,
                                     interviewee=interviewee)
            added_slots.append(new_slot)

        return added_slots

    def get_available_slots(self):
        """

        :return:
        """
        available_slots = list()
        for slot_index in range(len(self.slots)):
            if self.slots[slot_index].is_available():
                available_slots.append(self.slots[slot_index].serialize())
        return available_slots

    def set_interview(self, slot_id: int, interviewee: str):
        """

        :param slot_id:
        :param interviewee:
        :return:
        """
        self.slots[slot_id].set_interviewee(interviewee)
        return self.slots[slot_id].serialize()

    def search(self, start_date: str, end_date: str):
        """

        :param start_date:
        :param end_date:
        :return:
        """
        valid_slots = []
        start_date = string_to_datetime(start_date)
        end_date = string_to_datetime(end_date)

        for slot_index in range(len(self.slots)):
            if self.slots[slot_index].in_time_range(start_date, end_date):
                valid_slots.append(self.slots[slot_index].serialize())

        return valid_slots
