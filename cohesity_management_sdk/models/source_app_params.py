# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.ms_exchange_params

class SourceAppParams(object):

    """Implementation of the 'SourceAppParams' model.

    This message contains params specific to application running on the
    source
    such as a VM or a physical host.

    Attributes:
        is_vss_copy_only (bool): If the backup is a VSS full backup with the
            copy-only option specified.
        ms_exchange_params (MSExchangeParams): MS Exchange params.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "is_vss_copy_only":'isVssCopyOnly',
        "ms_exchange_params":'msExchangeParams'
    }

    def __init__(self,
                 is_vss_copy_only=None,
                 ms_exchange_params=None):
        """Constructor for the SourceAppParams class"""

        # Initialize members of the class
        self.is_vss_copy_only = is_vss_copy_only
        self.ms_exchange_params = ms_exchange_params


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
        is_vss_copy_only = dictionary.get('isVssCopyOnly')
        ms_exchange_params = cohesity_management_sdk.models.ms_exchange_params.MSExchangeParams.from_dictionary(dictionary.get('msExchangeParams')) if dictionary.get('msExchangeParams') else None

        # Return an object of this model
        return cls(is_vss_copy_only,
                   ms_exchange_params)


