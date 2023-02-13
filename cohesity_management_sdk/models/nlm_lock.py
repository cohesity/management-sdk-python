# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.lock_range

class NlmLock(object):

    """Implementation of the 'NlmLock' model.

    Response <clientID-Locks> map as received from view-keeper is converted
    into
    this structure. These Locks belong to one file-path.

    Attributes:
        client_id (string): Specifies the client ID
        lock_ranges (list of LockRange): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "client_id":'clientId',
        "lock_ranges":'lockRanges'
    }

    def __init__(self,
                 client_id=None,
                 lock_ranges=None):
        """Constructor for the NlmLock class"""

        # Initialize members of the class
        self.client_id = client_id
        self.lock_ranges = lock_ranges


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
        client_id = dictionary.get('clientId')
        lock_ranges = None
        if dictionary.get('lockRanges') != None:
            lock_ranges = list()
            for structure in dictionary.get('lockRanges'):
                lock_ranges.append(cohesity_management_sdk.models.lock_range.LockRange.from_dictionary(structure))

        # Return an object of this model
        return cls(client_id,
                   lock_ranges)


