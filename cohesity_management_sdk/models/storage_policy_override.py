# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class StoragePolicyOverride(object):

    """Implementation of the 'StoragePolicyOverride' model.

    Specifies if inline deduplication and compression settings inherited from
    Storage Domain (View Box) should be disabled for this View.

    Attributes:
        disable_inline_dedup_and_compression (bool): If false, the inline
            deduplication and compression settings inherited from the Storage
            Domain (View Box) apply to this View. If true, both inline
            deduplication and compression are disabled for this View. This can
            only be set to true if inline deduplication is set for the Storage
            Domain (View Box).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "disable_inline_dedup_and_compression":'disableInlineDedupAndCompression'
    }

    def __init__(self,
                 disable_inline_dedup_and_compression=None):
        """Constructor for the StoragePolicyOverride class"""

        # Initialize members of the class
        self.disable_inline_dedup_and_compression = disable_inline_dedup_and_compression


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
        disable_inline_dedup_and_compression = dictionary.get('disableInlineDedupAndCompression')

        # Return an object of this model
        return cls(disable_inline_dedup_and_compression)


