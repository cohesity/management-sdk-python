# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class NoncurrentVersionExpirationAction(object):

    """Implementation of the 'NoncurrentVersionExpirationAction' model.

    Attributes:
        noncurrent_days (long|int): Specifies the number of days an object
            is noncurrent before performing the associated action.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "noncurrent_days":'noncurrentDays'
    }

    def __init__(self,
                 noncurrent_days=None):
        """Constructor for the NoncurrentVersionExpirationAction class"""

        # Initialize members of the class
        self.noncurrent_days = noncurrent_days


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
        noncurrent_days = dictionary.get('noncurrentDays')

        # Return an object of this model
        return cls(noncurrent_days)


