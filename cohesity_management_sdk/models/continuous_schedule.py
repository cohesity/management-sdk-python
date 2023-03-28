# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ContinuousSchedule(object):

    """Implementation of the 'ContinuousSchedule' model.

    Specifies the time interval between two Job Runs of a continuous backup
    schedule and any QuietTime periods when new Job Runs should NOT be started.


    Attributes:

        backup_interval_mins (long|int): If specified, this field defines the
            time interval in minutes when new Job Runs are started.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "backup_interval_mins":'backupIntervalMins',
    }
    def __init__(self,
                 backup_interval_mins=None,
            ):

        """Constructor for the ContinuousSchedule class"""

        # Initialize members of the class
        self.backup_interval_mins = backup_interval_mins

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
        backup_interval_mins = dictionary.get('backupIntervalMins')

        # Return an object of this model
        return cls(
            backup_interval_mins
)