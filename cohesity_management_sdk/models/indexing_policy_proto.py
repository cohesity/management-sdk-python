# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class IndexingPolicyProto(object):

    """Implementation of the 'IndexingPolicyProto' model.

    Proto to encapsulate file level indexing policy for VMs in a backup job.

    Attributes:
        allow_prefixes (list of string): List of directory prefixes to allow
            for indexing.
        deny_prefixes (list of string): List of directory prefixes to filter
            out.
        disable_indexing (bool): If this field is set all the files in the VM
            will be filtered.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "allow_prefixes":'allowPrefixes',
        "deny_prefixes":'denyPrefixes',
        "disable_indexing":'disableIndexing'
    }

    def __init__(self,
                 allow_prefixes=None,
                 deny_prefixes=None,
                 disable_indexing=None):
        """Constructor for the IndexingPolicyProto class"""

        # Initialize members of the class
        self.allow_prefixes = allow_prefixes
        self.deny_prefixes = deny_prefixes
        self.disable_indexing = disable_indexing


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
        allow_prefixes = dictionary.get('allowPrefixes')
        deny_prefixes = dictionary.get('denyPrefixes')
        disable_indexing = dictionary.get('disableIndexing')

        # Return an object of this model
        return cls(allow_prefixes,
                   deny_prefixes,
                   disable_indexing)


