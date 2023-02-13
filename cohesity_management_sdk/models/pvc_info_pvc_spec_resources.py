# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.pvc_info_pvc_spec_resources_requests_entry

class PVCInfo_PVCSpec_Resources(object):

    """Implementation of the 'PVCInfo_PVCSpec_Resources' model.

    Flocker Volumes.

    Attributes:
        requests (list of PVCInfo_PVCSpec_Resources_RequestsEntry): Map of
            requested resources and their values.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "requests":'requests'
    }

    def __init__(self,
                 requests=None):
        """Constructor for the PVCInfo_PVCSpec_Resources class"""

        # Initialize members of the class
        self.requests = requests


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
        requests = None
        if dictionary.get('requests'):
            requests = list()
            for structure in dictionary.get('requests'):
                requests.append(cohesity_management_sdk.models.pvc_info_pvc_spec_resources_requests_entry.PVCInfo_PVCSpec_Resources_RequestsEntry.from_dictionary(structure))

        # Return an object of this model
        return cls(requests)


