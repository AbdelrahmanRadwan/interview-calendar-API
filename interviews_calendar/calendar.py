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

        :param interviewers: list of the names of the interviewers
        :param start_time: datetime object represents the start period at the calender
        :param interviewee: string represents the interviewee name (optional)
        """
        self.interviewers = interviewers
        self.interviewee = interviewee
        self.start_time = start_time
        self.end_time = next_hour(start_time)

    def serialize(self):
        """
        convert the class to serializable object
        :return: dictionary contains the class info in as a json serializable object
        """
        response = dict()
        response["interviewers"] = self.interviewers
        response["interviewee"] = self.interviewee
        response["start_time"] = get_datetime_slot_info(self.start_time)
        response["end_time"] = get_datetime_slot_info(self.end_time)

        return response

    def is_available(self):
        """
        check if the current slot is available for an interviewee or not
        :return: Boolean value; if the interviewee name is "", this means that this slot was not allocated yet
        """
        return not self.interviewee

    def set_interviewee(self, interviewee: str):
        """
        assign the current slot to a specific interviewee
        :param interviewee: string represents the interviewee name
        """
        self.interviewee = interviewee

    def in_time_range(self, start_time: datetime, end_time: datetime):
        """
        checks if the current slot is within the given time range or not
        :param start_time: start period of the given range
        :param end_time: end period of the given range
        :return: Boolean value; represents if the current slot is within the current range or not
        """
        return end_time >= self.start_time >= start_time


class Calendar:
    """
    All the allocated slots in the interviews calender
    """
    def __init__(self):
        """
        initialize the assigned slots so far with an empty array
        """
        self.slots = list()

    def get_slots(self):
        """
        get all the slots in the calendar so far
        :return: slots in the calendar
        """
        slots = []
        for slot in self.slots:
            slots.append(slot.serialize())
        return slots

    def add_slot(self, interviewers: list(), start_time: datetime, interviewee: str = ""):
        """
        add a slot to the calendar
        :param interviewers: names of the interviewers
        :param start_time: time in datetime format
        :param interviewee: interviewee name if available
        :return: the recently added slot
        """
        new_slot = CalendarSlot(interviewers=interviewers,
                                start_time=start_time,
                                interviewee=interviewee)
        self.slots.append(new_slot)
        return new_slot.serialize()

    def add_slots(self, interviewers: list(), start_times: list(), interviewee: str = ""):
        """
        add slots to the calendar
        :param interviewers: names of interviewers
        :param start_times: list of start datetimes
        :param interviewee: name of the interviewee
        :return: list of recently added slots
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
        get the allocated slots which don't have appointments with interviewees yet, so the interviewee can choose one of them!
        :return: slots which are not allocated so far
        """
        available_slots = list()
        for slot_index in range(len(self.slots)):
            if self.slots[slot_index].is_available():
                available_slots.append(self.slots[slot_index].serialize())
        return available_slots

    def set_interview(self, slot_id: int, interviewee: str):
        """
        Pair the interviewer with the interviewee, based on the slot which the interviewee will choose
        :param slot_id: array index of the available slots (it should be replaced with real ID)
        :param interviewee: interviewee name
        :return: chosen slot
        """
        # TODO: instead of using the self.slots, we must use the unassigned slots yet (current logic is wrong).
        self.slots[slot_id].set_interviewee(interviewee)
        return self.slots[slot_id].serialize()

    def search(self, start_date: str, end_date: str):
        """
        get the slots that were added to the calendar within a specific time range
        :param start_date: start date in the search query
        :param end_date: end date in the search query
        :return: valid search results
        """
        valid_slots = []
        start_date = string_to_datetime(start_date)
        end_date = string_to_datetime(end_date)

        for slot_index in range(len(self.slots)):
            if self.slots[slot_index].in_time_range(start_date, end_date):
                valid_slots.append(self.slots[slot_index].serialize())

        return valid_slots
