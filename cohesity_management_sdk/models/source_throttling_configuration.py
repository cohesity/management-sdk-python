# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.throttling_configuration

class SourceThrottlingConfiguration(object):

    """Implementation of the 'SourceThrottlingConfiguration' model.

    Specifies the source side throttling configuration.

    Attributes:
        cpu_throttling_config (ThrottlingConfiguration): CPU throttling
            configuration.
        network_throttling_config (ThrottlingConfiguration): Network throttling
            configuration.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cpu_throttling_config": 'cpuThrottlingConfig',
        "network_throttling_config": 'networkThrottlingConfig'
    }

    def __init__(self,
                 cpu_throttling_config=None,
                 network_throttling_config=None):
        """Constructor for the SourceThrottlingConfiguration class"""

        # Initialize members of the class
        self.cpu_throttling_config = cpu_throttling_config
        self.network_throttling_config = network_throttling_config


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
        cpu_throttling_config = cohesity_management_sdk.models.throttling_configuration.ThrottlingConfiguration.from_dictionary(dictionary.get('cpuThrottlingConfig')) if  dictionary.get('cpuThrottlingConfig') else None
        network_throttling_config = cohesity_management_sdk.models.throttling_configuration.ThrottlingConfiguration.from_dictionary(dictionary.get('networkThrottlingConfig')) if dictionary.get('networkThrottlingConfig') else None

        # Return an object of this model
        return cls(cpu_throttling_config,
                   network_throttling_config)


