# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.file_stat_info

class FileFstatResult(object):

    """Implementation of the 'FileFstatResult' model.

    FileFstatResult is the struct to return the result of file Fstats.

    Attributes:
        cookie (int): Cookie is used for paginating results. If
            ReadVMDirResult is returning partial results, this field will be
            set. Supplying this cookie will resume listing from where this
            result left off.
        fstat_info (FileStatInfo): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cookie":'cookie',
        "fstat_info":'fstatInfo'
    }

    def __init__(self,
                 cookie=None,
                 fstat_info=None):
        """Constructor for the FileFstatResult class"""

        # Initialize members of the class
        self.cookie = cookie
        self.fstat_info = fstat_info


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
        fstat_info = cohesity_management_sdk.models.file_stat_info.FileStatInfo.from_dictionary(dictionary.get('fstatInfo')) if dictionary.get('fstatInfo') else None

        # Return an object of this model
        return cls(cookie,
                   fstat_info)


