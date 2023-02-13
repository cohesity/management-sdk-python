# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.file_stat_info

class VmDirEntry(object):

    """Implementation of the 'VmDirEntry' model.

    VmDirEntry is the struct to respresent a file or a folder on a VM.

    Attributes:
        fstat_info (FileStatInfo):  FstatInfo is the stat information for the
            file.
        full_path (string): FullPath is the full path of the file/directory.
        name (string): Name is the name of the file or folder. For
            /test/file.txt, name will be file.txt.
        mtype (TypeVmDirEntryEnum): DirEntryType is the type of entry i.e.
            file/folder. Specifies the type of directory entry.  'kFile'
            indicates that current entry is of file type. 'kDirectory'
            indicates that current entry is of directory type. 'kSymlink'
            indicates that current entry is of symbolic link.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "fstat_info":'fstatInfo',
        "full_path":'fullPath',
        "name":'name',
        "mtype":'type'
    }

    def __init__(self,
                 fstat_info=None,
                 full_path=None,
                 name=None,
                 mtype=None):
        """Constructor for the VmDirEntry class"""

        # Initialize members of the class
        self.fstat_info = fstat_info
        self.full_path = full_path
        self.name = name
        self.mtype = mtype


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
        fstat_info = cohesity_management_sdk.models.file_stat_info.FileStatInfo.from_dictionary(dictionary.get('fstatInfo')) if dictionary.get('fstatInfo') else None
        full_path = dictionary.get('fullPath')
        name = dictionary.get('name')
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(fstat_info,
                   full_path,
                   name,
                   mtype)


