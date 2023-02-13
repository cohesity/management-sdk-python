# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class LockFileParams(object):

    """Implementation of the 'LockFileParams' model.

    Specifies the parameters to lock a file in a view.

    Attributes:
        expiry_timestamp_msecs (int): Specifies a definite timestamp in
            milliseconds for retaining the file, or to extend it's expiry
            timestamp.
        path (string): Specifies the file path that needs to be locked.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "expiry_timestamp_msecs":'expiryTimestampMsecs',
        "path":'path'
    }

    def __init__(self,
                 expiry_timestamp_msecs=None,
                 path=None):
        """Constructor for the LockFileParams class"""

        # Initialize members of the class
        self.expiry_timestamp_msecs = expiry_timestamp_msecs
        self.path = path


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
        expiry_timestamp_msecs = dictionary.get('expiryTimestampMsecs')
        path = dictionary.get('path')

        # Return an object of this model
        return cls(expiry_timestamp_msecs,
                   path)


