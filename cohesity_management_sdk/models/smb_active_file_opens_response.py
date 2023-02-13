# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.smb_active_file_path

class SmbActiveFileOpensResponse(object):

    """Implementation of the 'SmbActiveFileOpensResponse' model.

    Query response to SMB active file opens.

    Attributes:
        active_file_paths (list of SmbActiveFilePath): Specifies the active
            opens for an SMB file in a view.
        cookie (string): Specifies an opaque string to pass to get the next
            set of active opens. If null is returned, this response is the
            last set of active opens.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "active_file_paths":'activeFilePaths',
        "cookie":'cookie'
    }

    def __init__(self,
                 active_file_paths=None,
                 cookie=None):
        """Constructor for the SmbActiveFileOpensResponse class"""

        # Initialize members of the class
        self.active_file_paths = active_file_paths
        self.cookie = cookie


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
        active_file_paths = None
        if dictionary.get('activeFilePaths') != None:
            active_file_paths = list()
            for structure in dictionary.get('activeFilePaths'):
                active_file_paths.append(cohesity_management_sdk.models.smb_active_file_path.SmbActiveFilePath.from_dictionary(structure))
        cookie = dictionary.get('cookie')

        # Return an object of this model
        return cls(active_file_paths,
                   cookie)


