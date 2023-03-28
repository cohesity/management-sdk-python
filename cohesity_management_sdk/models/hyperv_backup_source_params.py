# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.source_app_params


class HyperVBackupSourceParams(object):

    """Implementation of the 'HyperVBackupSourceParams' model.

    Message to capture additional backup params for a Hyper-V type source.


    Attributes:

        source_app_params (SourceAppParams): This message will capture params
            for applications that are running as part of the server.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "source_app_params":'sourceAppParams',
    }
    def __init__(self,
                 source_app_params=None,
            ):

        """Constructor for the HyperVBackupSourceParams class"""

        # Initialize members of the class
        self.source_app_params = source_app_params

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
        source_app_params = cohesity_management_sdk.models.source_app_params.SourceAppParams.from_dictionary(dictionary.get('sourceAppParams')) if dictionary.get('sourceAppParams') else None

        # Return an object of this model
        return cls(
            source_app_params
)