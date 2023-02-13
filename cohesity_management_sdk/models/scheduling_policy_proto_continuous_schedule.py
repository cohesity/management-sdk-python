# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class SchedulingPolicyProtoContinuousSchedule(object):

    """Implementation of the 'SchedulingPolicyProto_ContinuousSchedule' model.

    TODO: type model description here.

    Attributes:
        backup_interval_mins (long|int): If this field is set, backups will be
            performed periodically every 'interval_mins' number of minutes.
            NOTE: This is the interval between the start time of two
            successive backups.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "backup_interval_mins":'backupIntervalMins'
    }

    def __init__(self,
                 backup_interval_mins=None):
        """Constructor for the SchedulingPolicyProtoContinuousSchedule class"""

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
        return cls(backup_interval_mins)


