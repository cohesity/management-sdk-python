
# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class GroupBackupEnvParams(object):

    """Implementation of the 'GroupBackupEnvParams' model.

    Message to capture any additional backup params for Group within the
    Office365 environment.

    """

    # Create a mapping from Model property names to API property names
    _names = {}

    def __init__(self):
        """Constructor for the GroupBackupEnvParams class"""

        # Initialize members of the class
        pass


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

        # Return an object of this model
        return cls()

