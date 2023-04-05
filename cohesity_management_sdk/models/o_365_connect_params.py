# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.objects_discovery_params


class O365ConnectParams(object):

    """Implementation of the 'O365ConnectParams' model.

    Specifies an Object containing information about a registered Office 365
    source.


    Attributes:

        objects_discovery_params (ObjectsDiscoveryParams): Specifies the
            parameters used for selectively discovering the office 365 objects
            during source registration or refresh.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "objects_discovery_params":'ObjectsDiscoveryParams',
    }
    def __init__(self,
                 objects_discovery_params=None,
            ):

        """Constructor for the O365ConnectParams class"""

        # Initialize members of the class
        self.objects_discovery_params = objects_discovery_params

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
        objects_discovery_params = cohesity_management_sdk.models.objects_discovery_params.ObjectsDiscoveryParams.from_dictionary(dictionary.get('ObjectsDiscoveryParams')) if dictionary.get('ObjectsDiscoveryParams') else None

        # Return an object of this model
        return cls(
            objects_discovery_params
)