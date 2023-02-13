# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.zone_config

class RegisteredProtectionSourceIsilonParams(object):

    """Implementation of the 'RegisteredProtectionSourceIsilonParams' model.

    Contains any additional hive environment specific backup params at the
    job level.

    Attributes:
        zone_config_list (list of ZoneConfig): List of access zone info in an
            Isilion Cluster.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "zone_config_list":'zoneConfigList'
    }

    def __init__(self,
                 zone_config_list=None):
        """Constructor for the RegisteredProtectionSourceIsilonParams class"""

        # Initialize members of the class
        self.zone_config_list = zone_config_list


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
        zone_config_list = None
        if dictionary.get('zoneConfigList') != None:
            zone_config_list = list()
            for structure in dictionary.get('zoneConfigList'):
                zone_config_list.append(cohesity_management_sdk.models.zone_config.ZoneConfig.from_dictionary(structure))

        # Return an object of this model
        return cls(zone_config_list)


