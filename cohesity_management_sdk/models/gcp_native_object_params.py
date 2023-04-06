# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.gcp_disk_exclusion_object_params


class GCPNativeObjectParams(object):

    """Implementation of the 'GCPNativeObjectParams' model.

    TODO: type description here.


    Attributes:

        disk_exclusion_params (GCPDiskExclusionObjectParams): Specifies the
            criteria for GCP VM disk exclusion.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "disk_exclusion_params":'diskExclusionParams',
    }
    def __init__(self,
                 disk_exclusion_params=None,
            ):

        """Constructor for the GCPNativeObjectParams class"""

        # Initialize members of the class
        self.disk_exclusion_params = disk_exclusion_params

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
        disk_exclusion_params = cohesity_management_sdk.models.gcp_disk_exclusion_object_params.GCPDiskExclusionObjectParams.from_dictionary(dictionary.get('diskExclusionParams')) if dictionary.get('diskExclusionParams') else None

        # Return an object of this model
        return cls(
            disk_exclusion_params
)