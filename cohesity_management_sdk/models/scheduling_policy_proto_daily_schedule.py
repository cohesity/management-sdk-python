# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class SchedulingPolicyProtoDailySchedule(object):

    """Implementation of the 'SchedulingPolicyProto_DailySchedule' model.

    The daily schedule encompasses weekly schedules as well. This has been
    done so there is only one way of specifying a schedule (backing up daily
    is the same as backing up weekly, but on all days of the week).

    Attributes:
        days (list of int): The days of the week backup must be performed. If
            no days are specified, then the backup will be performed on all
            days.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "days":'days'
    }

    def __init__(self,
                 days=None):
        """Constructor for the SchedulingPolicyProtoDailySchedule class"""

        # Initialize members of the class
        self.days = days


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
        days = dictionary.get('days')

        # Return an object of this model
        return cls(days)


