# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.time

class BackupPolicyProtoDailySchedule(object):

    """Implementation of the 'BackupPolicyProto_DailySchedule' model.

    The daily schedule encompasses weekly schedules as well. This has been
    done so there is only one way of specifying a schedule (backing up daily
    is the same as backing up weekly, but on all days of the week).

    Attributes:
        days (list of int): The days of the week backup must be performed. If
            no days are specified, then the backup will be performed on all
            days.
        time (Time): A message to encapusulate time of a day. Users of this
            proto will have to store the timezone information separately. For
            example, when this proto is part of a backup job, timezone of the
            backup job is applied to get the absolute time.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "days":'days',
        "time":'time'
    }

    def __init__(self,
                 days=None,
                 time=None):
        """Constructor for the BackupPolicyProtoDailySchedule class"""

        # Initialize members of the class
        self.days = days
        self.time = time


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
        time = cohesity_management_sdk.models.time.Time.from_dictionary(dictionary.get('time')) if dictionary.get('time') else None

        # Return an object of this model
        return cls(days,
                   time)


