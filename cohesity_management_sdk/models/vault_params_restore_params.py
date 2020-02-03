# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.vault_params_restore_params_glacier

class VaultParamsRestoreParams(object):

    """Implementation of the 'VaultParams_RestoreParams' model.

    TODO: type model description here.

    Attributes:
        glacier (VaultParamsRestoreParamsGlacier): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "glacier":'glacier'
    }

    def __init__(self,
                 glacier=None):
        """Constructor for the VaultParamsRestoreParams class"""

        # Initialize members of the class
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
        glacier = cohesity_management_sdk.models.vault_params_restore_params_glacier.VaultParamsRestoreParamsGlacier.from_dictionary(dictionary.get('glacier')) if dictionary.get('glacier') else None

        # Return an object of this model
        return cls(glacier)


