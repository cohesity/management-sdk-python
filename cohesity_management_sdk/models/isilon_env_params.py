# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.isilon_env_params_zone_config_map_entry

class IsilonEnvParams(object):

    """Implementation of the 'IsilonEnvParams' model.

    Message to capture Ision-spcific environment parameters.

    Attributes:
        zone_config_map (list of IsilonEnvParams_ZoneConfigMapEntry): Mapping from
            access zone name to configuration.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "zone_config_map":'zoneConfigMap'
    }

    def __init__(self,
                 zone_config_map=None):
        """Constructor for the IsilonEnvParams class"""

        # Initialize members of the class
        self.zone_config_map = zone_config_map


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
        zone_config_map = None
        if dictionary.get('zoneConfigMap') != None:
            zone_config_map = list()
            for structure in dictionary('zoneConfigMap'):
                zone_config_map.append(cohesity_management_sdk.models.isilon_env_params_zone_config_map_entry.IsilonEnvParams_ZoneConfigMapEntry.from_dictionary(structure))

        # Return an object of this model
        return cls(zone_config_map)


