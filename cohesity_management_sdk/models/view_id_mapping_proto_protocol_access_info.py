# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class ViewIdMappingProtoProtocolAccessInfo(object):

    """Implementation of the 'ViewIdMappingProto_ProtocolAccessInfo' model.

    TODO: type model description here.

    Attributes:
        iscsi_access (int): Access control for iSCSI protocol for this view.
        nfs_access (int): Access control for NFS protocol for this view.
        s_3_access (int): Access control for S3 protocol for this view.
        smb_access (int): Access control for SMB protocol for this view.
        swift_access (int): Access control for Swift protocol for this view.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "iscsi_access":'iscsiAccess',
        "nfs_access":'nfsAccess',
        "s_3_access":'s3Access',
        "smb_access":'smbAccess',
        "swift_access":'swiftAccess'
    }

    def __init__(self,
                 iscsi_access=None,
                 nfs_access=None,
                 s_3_access=None,
                 smb_access=None,
                 swift_access=None):
        """Constructor for the ViewIdMappingProtoProtocolAccessInfo class"""

        # Initialize members of the class
        self.iscsi_access = iscsi_access
        self.nfs_access = nfs_access
        self.s_3_access = s_3_access
        self.smb_access = smb_access
        self.swift_access = swift_access


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
        iscsi_access = dictionary.get('iscsiAccess')
        nfs_access = dictionary.get('nfsAccess')
        s_3_access = dictionary.get('s3Access')
        smb_access = dictionary.get('smbAccess')
        swift_access = dictionary.get('swiftAccess')

        # Return an object of this model
        return cls(iscsi_access,
                   nfs_access,
                   s_3_access,
                   smb_access,
                   swift_access)


