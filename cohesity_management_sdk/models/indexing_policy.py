# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class IndexingPolicy(object):

    """Implementation of the 'IndexingPolicy' model.

    Specifies settings for indexing files found in an Object
    (such as a VM) so these files can be searched and recovered.
    This also specifies inclusion and exclusion rules that determine
    the directories to index.

    Attributes:
        allow_prefixes (list of string): Array of Indexed Directories.
            Specifies a list of directories to index.
        deny_prefixes (list of string): Array of Excluded Directories.
            Specifies a list of directories to exclude from indexing.
        disable_indexing (bool): Specifies if the files found in an Object
            (such as a VM) should be indexed. If false (the default), files
            are indexed.

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
        """Constructor for the IndexingPolicy class"""

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


