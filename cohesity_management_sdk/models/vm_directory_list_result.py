# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.vm_dir_entry

class VmDirectoryListResult(object):

    """Implementation of the 'VmDirectoryListResult' model.

    VmDirectoryListResult is a struct containing information about each
    directory entry.

    Attributes:
        cookie (string): Cookie is used for paginating results. If
            ReadVMDirResult is returning partial results, this field will be
            set. Supplying this cookie will resume listing from where this
            result left off.
        entries (list of VmDirEntry): Entries is the array of files and
            folders that are immediate children of the parent directory
            specified in the request.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cookie":'cookie',
        "entries":'entries'
    }

    def __init__(self,
                 cookie=None,
                 entries=None):
        """Constructor for the VmDirectoryListResult class"""

        # Initialize members of the class
        self.cookie = cookie
        self.entries = entries


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
        cookie = dictionary.get('cookie')
        entries = None
        if dictionary.get('entries') != None:
            entries = list()
            for structure in dictionary.get('entries'):
                entries.append(cohesity_management_sdk.models.vm_dir_entry.VmDirEntry.from_dictionary(structure))

        # Return an object of this model
        return cls(cookie,
                   entries)


