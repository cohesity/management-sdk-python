# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class GCPJobDiskExclusionRule_Label(object):

    """Implementation of the 'GCPJobDiskExclusionRule_Label' model.

    TODO: type description here.


    Attributes:

        key (string): Key for the label. Note that if the provided label key's
            length is more than the maximum length allowed by GCP(currently
            63), then the value would be automatically truncated before
            setting.
        value (string): Value for the label. Note that if the provided label
            value's length is more than the maximum length allowed by
            GCP(currently 63), then the value would be automatically truncated
            before setting.
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

        """Constructor for the GCPJobDiskExclusionRule_Label class"""

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
        value = dictionary.get('value')

        # Return an object of this model
        return cls(
            key,
            value
)