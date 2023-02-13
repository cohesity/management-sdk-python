# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ElastifileContainer(object):

    """Implementation of the 'ElastifileContainer' model.

    Specifies information about container in an Elastifile Cluster.

    Attributes:
        created_at (string): Specifies the creation date of the container.
        id (int): Specifies id of a Elastifile Container in a Cluster.
        is_nfs_interface (bool): Specifies if the container has NFS volumes or
            not.
        is_smb_interface (bool): Specifies if the container has SMB volumes or
            not.
        name (string): Specifies the name of the container.
        protocols (list of ProtocolEnum): Specifies Elastifile supported
            Protocol information enabled on Elastifile container. 'kNfs'
            indicates NFS protocol in an elastifile container. 'kSmb'
            indicates SMB protocol in an elastifile container.
        used_bytes (long|int): Specifies the bytes used by the container.
        uuid (string): Specifies the UUID of the container.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "created_at":'createdAt',
        "id":'id',
        "is_nfs_interface":'isNfsInterface',
        "is_smb_interface":'isSmbInterface',
        "name":'name',
        "protocols":'protocols',
        "used_bytes":'usedBytes',
        "uuid":'uuid'
    }

    def __init__(self,
                 created_at=None,
                 id=None,
                 is_nfs_interface=None,
                 is_smb_interface=None,
                 name=None,
                 protocols=None,
                 used_bytes=None,
                 uuid=None):
        """Constructor for the ElastifileContainer class"""

        # Initialize members of the class
        self.created_at = created_at
        self.id = id
        self.is_nfs_interface = is_nfs_interface
        self.is_smb_interface = is_smb_interface
        self.name = name
        self.protocols = protocols
        self.used_bytes = used_bytes
        self.uuid = uuid


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
        created_at = dictionary.get('createdAt')
        id = dictionary.get('id')
        is_nfs_interface = dictionary.get('isNfsInterface')
        is_smb_interface = dictionary.get('isSmbInterface')
        name = dictionary.get('name')
        protocols = dictionary.get('protocols')
        used_bytes = dictionary.get('usedBytes')
        uuid = dictionary.get('uuid')

        # Return an object of this model
        return cls(created_at,
                   id,
                   is_nfs_interface,
                   is_smb_interface,
                   name,
                   protocols,
                   used_bytes,
                   uuid)


