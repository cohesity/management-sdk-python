# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ClusterConfigProtoStoragePolicyOverride(object):

    """Implementation of the 'ClusterConfigProto_StoragePolicyOverride' model.

    TODO: type model description here.

    Attributes:
        disable_dedup (bool): If the following id set to true, we would
            disable dedup for writes made in this view irrespective of the
            view box's storage policy.
        disable_inline_dedup_and_compression (bool): If this is set to true,
            we will not do inline dedup and compression even if
            deduplicate_compress_delay_secs is set to 0 in the view box's
            storage policy.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "disable_dedup":'disableDedup',
        "disable_inline_dedup_and_compression":'disableInlineDedupAndCompression'
    }

    def __init__(self,
                 disable_dedup=None,
                 disable_inline_dedup_and_compression=None):
        """Constructor for the ClusterConfigProtoStoragePolicyOverride class"""

        # Initialize members of the class
        self.disable_dedup = disable_dedup
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
        disable_dedup = dictionary.get('disableDedup')
        disable_inline_dedup_and_compression = dictionary.get('disableInlineDedupAndCompression')

        # Return an object of this model
        return cls(disable_dedup, disable_inline_dedup_and_compression)


