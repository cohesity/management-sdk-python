# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class TaskEvent(object):

    """Implementation of the 'TaskEvent' model.

    Specifies events that clients can attach to a task.

    Attributes:
        event_message (string): Specifies the message associated with an
            event.
        percent_finished (float): Specifies the completion percentage of the
            task attached to this event.
        remaining_work_count (long|int): Specifies the amount of work
            remaining for the task attached to this event.
        timestamp_seconds (long|int): Specifies the Unix timestamp that the
            event occurred.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "event_message":'eventMessage',
        "percent_finished":'percentFinished',
        "remaining_work_count":'remainingWorkCount',
        "timestamp_seconds":'timestampSeconds'
    }

    def __init__(self,
                 event_message=None,
                 percent_finished=None,
                 remaining_work_count=None,
                 timestamp_seconds=None):
        """Constructor for the TaskEvent class"""

        # Initialize members of the class
        self.event_message = event_message
        self.percent_finished = percent_finished
        self.remaining_work_count = remaining_work_count
        self.timestamp_seconds = timestamp_seconds


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        event_message = dictionary.get('eventMessage')
        percent_finished = dictionary.get('percentFinished')
        remaining_work_count = dictionary.get('remainingWorkCount')
        timestamp_seconds = dictionary.get('timestampSeconds')

        # Return an object of this model
        return cls(event_message,
                   percent_finished,
                   remaining_work_count,
                   timestamp_seconds)


