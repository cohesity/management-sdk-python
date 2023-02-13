# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class CreateApiKeyParams(object):

    """Implementation of the 'CreateApiKeyParams' model.

    Specifies the parameters to create an API key.

    Attributes:
        expiring_time_msecs (int|long): Specifies a time stamp when the API
            key will expire in milli seconds.
        is_active (bool): Specifies if the API key is active. Only an active
            and not expired API key can be used for authentication.
        name (string, required): Specifies the name of API key.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "expiring_time_msecs":'expiringTimeMsecs',
        "is_active":'isActive',
        "name":'name'
    }

    def __init__(self,
                 expiring_time_msecs=None,
                 is_active=None,
                 name=None):
        """Constructor for the CreateApiKeyParams class"""

        # Initialize members of the class
        self.expiring_time_msecs = expiring_time_msecs
        self.is_active = is_active
        self.name = name


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
        expiring_time_msecs = dictionary.get('expiringTimeMsecs')
        is_active = dictionary.get('isActive')
        name = dictionary.get('name')

        # Return an object of this model
        return cls(expiring_time_msecs,
                   is_active,
                   name)


