from datetime import (datetime)

from helper_functions.helper_functions import (next_hour, string_to_datetime, datetime_to_string)


class CalendarSlot:
    """
    Each allocated slot of the Calender
    """
    def __init__(self, interviewers: list(), start_time: datetime, interviewee: str = ""):
        self.interviewers = interviewers
        self.interviewee = interviewee
        self.start_time = start_time
        self.end_time = next_hour(start_time)

    def serialize(self):
        response = dict()
        response["interviewers"] = self.interviewers
        response["interviewee"] = self.interviewee
        response["start_time"] = datetime_to_string(self.start_time)
        response["end_time"] = datetime_to_string(self.end_time)

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
        return new_slot.serialize()

    def add_slots(self, interviewers: list(), start_times: list(), interviewee: str = ""):
        added_slots = []
        for time in start_times:
            time = string_to_datetime(time)
            new_slot = self.add_slot(interviewers=interviewers,
                                     start_time=time,
                                     interviewee=interviewee)
            added_slots.append(new_slot)

        return added_slots

    def get_available_slots(self):
        available_slots = list()
        for slot_index in range(len(self.slots)):
            if self.slots[slot_index].is_available():
                available_slots.append(self.slots[slot_index].serialize())
        print(available_slots)
        return available_slots

    def set_interview(self, slot_id: int, interviewee: str):
        self.slots[slot_id].set_interviewee(interviewee)
        return self.slots[slot_id].serialize()
