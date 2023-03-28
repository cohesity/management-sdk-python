# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.time


class BackupPolicyProto_OneOffSchedule(object):

    """Implementation of the 'BackupPolicyProto_OneOffSchedule' model.

    TODO: type description here.


    Attributes:

        time (Time): The time when the one-off backup should be performed.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "time":'time',
    }
    def __init__(self,
                 time=None,
            ):

        """Constructor for the BackupPolicyProto_OneOffSchedule class"""

        # Initialize members of the class
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
        time = cohesity_management_sdk.models.time.Time.from_dictionary(dictionary.get('time')) if dictionary.get('time') else None

        # Return an object of this model
        return cls(
            time
)