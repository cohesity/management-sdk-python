# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.flash_blade_nfs_info

class FlashBladeFileSystem(object):

    """Implementation of the 'FlashBladeFileSystem' model.

    Specifies information about a Flash Blade File System in a Storage Array.

    Attributes:
        backup_enabled (bool): Specifies whether the .snapshot directory
            exists on the file system. Backup is enabled only if the directory
            exists.
        created_time_msecs (long|int): Specifies the time when the filesystem
            was created in Unix epoch time in milliseconds.
        logical_capacity_bytes (long|int): Specifies the total capacity in
            bytes of the file system.
        logical_used_bytes (long|int): Specifies the size of logical data
            currently represented on the file system in bytes.
        nfs_info (FlashBladeNfsInfo): Specifies information specific to NFS
            protocol exposed by Pure Flash Blade file system.
        physical_used_bytes (long|int): Specifies the size of physical data
            currently consumed by the file system. This includes the space
            used for the snapshots.
        protocols (list of ProtocolFlashBladeFileSystemEnum): List of
            Protocols.  Specifies the list of protocols enabled on the file
            system. 'kNfs' indicates NFS exports are supported on Pure
            FlashBlade File System. 'kCifs2' indicates CIFS/SMB Shares are
            supported on Pure FlashBlade File System. 'kHttp' indicates object
            protocol over HTTP and HTTPS are supported.
        unique_used_bytes (long|int): Specifies the size of physical data
            consumed by the file system itself not including the size of the
            snapshots.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "backup_enabled":'backupEnabled',
        "created_time_msecs":'createdTimeMsecs',
        "logical_capacity_bytes":'logicalCapacityBytes',
        "logical_used_bytes":'logicalUsedBytes',
        "nfs_info":'nfsInfo',
        "physical_used_bytes":'physicalUsedBytes',
        "protocols":'protocols',
        "unique_used_bytes":'uniqueUsedBytes'
    }

    def __init__(self,
                 backup_enabled=None,
                 created_time_msecs=None,
                 logical_capacity_bytes=None,
                 logical_used_bytes=None,
                 nfs_info=None,
                 physical_used_bytes=None,
                 protocols=None,
                 unique_used_bytes=None):
        """Constructor for the FlashBladeFileSystem class"""

        # Initialize members of the class
        self.backup_enabled = backup_enabled
        self.created_time_msecs = created_time_msecs
        self.logical_capacity_bytes = logical_capacity_bytes
        self.logical_used_bytes = logical_used_bytes
        self.nfs_info = nfs_info
        self.physical_used_bytes = physical_used_bytes
        self.protocols = protocols
        self.unique_used_bytes = unique_used_bytes


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
        backup_enabled = dictionary.get('backupEnabled')
        created_time_msecs = dictionary.get('createdTimeMsecs')
        logical_capacity_bytes = dictionary.get('logicalCapacityBytes')
        logical_used_bytes = dictionary.get('logicalUsedBytes')
        nfs_info = cohesity_management_sdk.models.flash_blade_nfs_info.FlashBladeNfsInfo.from_dictionary(dictionary.get('nfsInfo')) if dictionary.get('nfsInfo') else None
        physical_used_bytes = dictionary.get('physicalUsedBytes')
        protocols = dictionary.get('protocols')
        unique_used_bytes = dictionary.get('uniqueUsedBytes')

        # Return an object of this model
        return cls(backup_enabled,
                   created_time_msecs,
                   logical_capacity_bytes,
                   logical_used_bytes,
                   nfs_info,
                   physical_used_bytes,
                   protocols,
                   unique_used_bytes)


