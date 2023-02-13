# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.vault_params_restore_params_glacier

class VaultParamsRestoreParams(object):

    """Implementation of the 'VaultParams_RestoreParams' model.

    TODO: type model description here.

    Attributes:
        allow_marked_for_removal (bool): TODO: type description here.
        glacier (VaultParamsRestoreParamsGlacier): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "allow_marked_for_removal":'allowMarkedForRemoval',
        "glacier":'glacier'
    }

    def __init__(self,
                 allow_marked_for_removal=None,
                 glacier=None):
        """Constructor for the VaultParamsRestoreParams class"""

        # Initialize members of the class
        self.allow_marked_for_removal = allow_marked_for_removal
        self.glacier = glacier


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
        allow_marked_for_removal = dictionary.get('allowMarkedForRemoval')
        glacier = cohesity_management_sdk.models.vault_params_restore_params_glacier.VaultParamsRestoreParamsGlacier.from_dictionary(dictionary.get('glacier')) if dictionary.get('glacier') else None

        # Return an object of this model
        return cls(allow_marked_for_removal, glacier)


