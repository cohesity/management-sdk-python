# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.vcd_storage_profile

class ListStorageProfilesResponseBody(object):

    """Implementation of the 'ListStorageProfilesResponseBody' model.

    Specifies the response to request to list the storage profiles associated
    with a VDC.

    Attributes:
        storage_profiles (list of VcdStorageProfile): Specifies a list of
            storage profiles.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "storage_profiles":'storageProfiles'
    }

    def __init__(self,
                 storage_profiles=None):
        """Constructor for the ListStorageProfilesResponseBody class"""

        # Initialize members of the class
        self.storage_profiles = storage_profiles


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
        storage_profiles = None
        if dictionary.get('storageProfiles') != None:
            storage_profiles = list()
            for structure in dictionary.get('storageProfiles'):
                storage_profiles.append(cohesity_management_sdk.models.vcd_storage_profile.VcdStorageProfile.from_dictionary(structure))

        # Return an object of this model
        return cls(storage_profiles)

