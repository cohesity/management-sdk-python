# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.isilon_env_params_zone_config

class IsilonEnvParams_ZoneConfigMapEntry(object):

    """Implementation of the 'IsilonEnvParams_ZoneConfigMapEntry' model.


    Attributes:
        key (string): TODO: type description here.
        value (IsilonEnvParams_ZoneConfig): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "key": 'key',
        "value": 'value'
    }

    def __init__(self,
                 key=None,
                 value=None):
        """Constructor for the IsilonEnvParams_ZoneConfigMapEntry class"""

        # Initialize members of the class
        self.key = key
        self.value = value


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
        key = dictionary.get('key')
        value = cohesity_management_sdk.models.isilon_env_params_zone_config.IsilonEnvParams_ZoneConfig.from_dictionary(dictionary.get('value')) if dictionary.get('value') else None

        # Return an object of this model
        return cls(key,
                   value)


