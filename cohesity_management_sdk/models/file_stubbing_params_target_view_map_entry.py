# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.file_stubbing_params_target_view_data


class FileStubbingParams_TargetViewMapEntry(object):

    """Implementation of the 'FileStubbingParams_TargetViewMapEntry' model.

    TODO: type description here.


    Attributes:

        key (long|int): TODO: Type description here.
        value (FileStubbingParams_TargetViewData): TODO: Type description here.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "key":'key',
        "value":'value',
    }
    def __init__(self,
                 key=None,
                 value=None,
            ):

        """Constructor for the FileStubbingParams_TargetViewMapEntry class"""

        # Initialize members of the class
        self.key = key
        self.value = value

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
        key = dictionary.get('key')
        value = cohesity_management_sdk.models.file_stubbing_params_target_view_data.FileStubbingParams_TargetViewData.from_dictionary(dictionary.get('value')) if dictionary.get('value') else None

        # Return an object of this model
        return cls(
            key,
            value
)