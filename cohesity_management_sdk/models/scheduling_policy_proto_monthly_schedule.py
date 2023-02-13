# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class SchedulingPolicyProtoMonthlySchedule(object):

    """Implementation of the 'SchedulingPolicyProto_MonthlySchedule' model.

    TODO: type model description here.

    Attributes:
        count (int): Count of the day on which to perform the backup (look
            above for a more detailed description).
        day (int): The day of the month the backup is to be performed.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "count":'count',
        "day":'day'
    }

    def __init__(self,
                 count=None,
                 day=None):
        """Constructor for the SchedulingPolicyProtoMonthlySchedule class"""

        # Initialize members of the class
        self.count = count
        self.day = day


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
        count = dictionary.get('count')
        day = dictionary.get('day')

        # Return an object of this model
        return cls(count,
                   day)


