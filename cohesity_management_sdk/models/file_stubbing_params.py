# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.filtering_policy_proto

class FileStubbingParams(object):

    """Implementation of the 'FileStubbingParams' model.

    File Stubbing Parameters Message to capture the additional stubbing params
    for a file-based environment.

    Attributes:
        cold_file_window (long|int): Identifies the cold files in the NAS
            source. Files that haven't been accessed/modified in the last
            cold_file_window msecs or are older than cold_window_msecs are
            migrated.
        file_select_policy (int): File migrate policy based on file
            access/modify time and age.
        file_size (long|int): Gives the size criteria to be used for selecting
            the files to be migrated. The cold files that are equal and
            greater than file_size or smaller than file_size are migrated.
        file_size_policy (int): File size policy for selecting files to
            migrate.
        filtering_policy (FilteringPolicyProto): Proto to encapsulate the
            filtering policy for backup objects like files or directories. If
            an object is not matched by any of the 'allow_filters', it will be
            excluded in the backup. If an object is matched by one of the
            'deny_filters', it will always be excluded in the backup.
            Basically 'deny_filters' overwrite 'allow_filters' if they both
            match the same object. Currently we only support two kinds of
            filter: prefix which always starts with '/', or postfix which
            always starts with '*' (cannot be "*" only). We don't support
            regular expression right now. A concrete example is: Allow
            filters: "/" Deny filters: "/tmp", "*.mp4" Using such a policy
            will include everything under the root directory except the /tmp
            directory and all the mp4 files.
        target_view_name (string): The target view name to which the data will
            be migrated.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cold_file_window":'coldFileWindow',
        "file_select_policy":'fileSelectPolicy',
        "file_size":'fileSize',
        "file_size_policy":'fileSizePolicy',
        "filtering_policy":'filteringPolicy',
        "target_view_name":'targetViewName'
    }

    def __init__(self,
                 cold_file_window=None,
                 file_select_policy=None,
                 file_size=None,
                 file_size_policy=None,
                 filtering_policy=None,
                 target_view_name=None):
        """Constructor for the FileStubbingParams class"""

        # Initialize members of the class
        self.cold_file_window = cold_file_window
        self.file_select_policy = file_select_policy
        self.file_size = file_size
        self.file_size_policy = file_size_policy
        self.filtering_policy = filtering_policy
        self.target_view_name = target_view_name


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
        cold_file_window = dictionary.get('coldFileWindow')
        file_select_policy = dictionary.get('fileSelectPolicy')
        file_size = dictionary.get('fileSize')
        file_size_policy = dictionary.get('fileSizePolicy')
        filtering_policy = cohesity_management_sdk.models.filtering_policy_proto.FilteringPolicyProto.from_dictionary(dictionary.get('filteringPolicy')) if dictionary.get('filteringPolicy') else None
        target_view_name = dictionary.get('targetViewName')

        # Return an object of this model
        return cls(cold_file_window,
                   file_select_policy,
                   file_size,
                   file_size_policy,
                   filtering_policy,
                   target_view_name)


