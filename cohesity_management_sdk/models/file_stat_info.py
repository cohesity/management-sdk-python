# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class FileStatInfo(object):

    """Implementation of the 'FileStatInfo' model.

    TODO: type description here.


    Attributes:

        backup_source_inode_id (long|int): Source inode id metadata for certain
            adapters e.g. Netapp.
        mtime_usecs (long|int): If this is a file, the mtime as returned by
            stat.
        size (long|int): If this is a file, the size of the file as returned by
            stat.
        mtype (int): The type of this entity. This field will not be populated
            for ReadDir results, since the DirEntry already contains the type
            information.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "backup_source_inode_id":'backupSourceInodeId',
        "mtime_usecs":'mtimeUsecs',
        "size":'size',
        "mtype":'type',
    }
    def __init__(self,
                 backup_source_inode_id=None,
                 mtime_usecs=None,
                 size=None,
                 mtype=None,
            ):

        """Constructor for the FileStatInfo class"""

        # Initialize members of the class
        self.backup_source_inode_id = backup_source_inode_id
        self.mtime_usecs = mtime_usecs
        self.size = size
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
        backup_source_inode_id = dictionary.get('backupSourceInodeId')
        mtime_usecs = dictionary.get('mtimeUsecs')
        size = dictionary.get('size')
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(
            backup_source_inode_id,
            mtime_usecs,
            size,
            mtype
)