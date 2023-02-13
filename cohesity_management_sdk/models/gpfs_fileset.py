# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class GpfsFileset(object):

    """Implementation of the 'GpfsFileset' model.

    Specifies information about a fileset in a GPFS file system.

    Attributes:
        id (int): Specifies the id of the fileset.
        is_independent_fileset (bool): If the given fileset is an Independent
            fileset or not.
        name (string): Name of the filesystem associated with the fileset
        path (string): Specifies the absolute path of the fileset.
        protocols (list of ProtocolEnum): Specifies GPFS supported Protocol
            information enabled on GPFS File System 'kNfs' indicates NFS
            exports in a GPFS fileset. 'kSmb' indicates CIFS/SMB Shares in a
            GPFS fileset.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "is_independent_fileset":'isIndependentFileset',
        "name":'name',
        "path":'path',
        "protocols":'protocols'
    }

    def __init__(self,
                 id=None,
                 is_independent_fileset=None,
                 name=None,
                 path=None,
                 protocols=None):
        """Constructor for the GpfsFileset class"""

        # Initialize members of the class
        self.id = id
        self.is_independent_fileset = is_independent_fileset
        self.name = name
        self.path = path
        self.protocols = protocols


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
        id = dictionary.get('id')
        is_independent_fileset = dictionary.get('isIndependentFileset')
        name = dictionary.get('name')
        path = dictionary.get('path')
        protocols = dictionary.get('protocols')

        # Return an object of this model
        return cls(id,
                   is_independent_fileset,
                   name,
                   path,
                   protocols)


