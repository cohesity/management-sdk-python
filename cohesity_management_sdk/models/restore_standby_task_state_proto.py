# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class RestoreStandbyTaskStateProto(object):

    """Implementation of the 'RestoreStandbyTaskStateProto' model.

    Specifies an Object containing information about a Universal Data Adapter
    cluster.

    Attributes:
        standby_restore_complete (bool):This indicates if standby restore task
            to update standby resource state is completed or not.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "standby_restore_complete":'standbyRestoreComplete'
    }

    def __init__(self,
                 standby_restore_complete=None):
        """Constructor for the RestoreStandbyTaskStateProto class"""

        # Initialize members of the class
        self.standby_restore_complete = standby_restore_complete


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
        standby_restore_complete = dictionary.get('standbyRestoreComplete')

        # Return an object of this model
        return cls(standby_restore_complete)


