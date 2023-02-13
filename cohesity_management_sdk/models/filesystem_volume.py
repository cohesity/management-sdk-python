# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.disk
import cohesity_management_sdk.models.logical_volume

class FilesystemVolume(object):

    """Implementation of the 'FilesystemVolume' model.

    Specifies information about a filesystem volume.

    Attributes:
        disks (list of Disk): Array of Disks and Partitions.  Specifies
            information about all the disks and partitions needed to mount
            this logical volume.
        display_name (string): Specifies a description about the filesystem.
        filesystem_type (string): Specifies type of the filesystem on this
            volume.
        filesystem_uuid (string): Specifies the uuid of the filesystem.
        is_supported (bool): If true, this is a supported filesystem volume
            type.
        logical_volume (LogicalVolume): Specify attributes for a kLMV (Linux)
            or kLDM (Windows) filesystem. This field is set only for kLVM and
            kLDM volume types.
        logical_volume_type (LogicalVolumeTypeEnum): Specifies the type of
            logical volume such as kSimpleVolume, kLVM or kLDM.
            'kSimpleVolume' indicates a simple volume. Data can be used by
            just mounting the only one partition present on the disk. 'kLVM'
            indicates a logical volume on Linux managed by a Logical Volume
            Manager. In order to access the data, deviceTree must be created
            based on the specification in logicalVolume.deviceTree. 'kLDM'
            indicates a logical volume on Windows managed by Logical Disk
            Manager.
        name (string): Specifies the name of the volume such as /C.
        volume_guid (string): VolumeGuid is the Volume guid. This is populated
            for kPhysical environments.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "disks":'disks',
        "display_name":'displayName',
        "filesystem_type":'filesystemType',
        "filesystem_uuid":'filesystemUuid',
        "is_supported":'isSupported',
        "logical_volume":'logicalVolume',
        "logical_volume_type":'logicalVolumeType',
        "name":'name',
        "volume_guid":'volumeGuid'
    }

    def __init__(self,
                 disks=None,
                 display_name=None,
                 filesystem_type=None,
                 filesystem_uuid=None,
                 is_supported=None,
                 logical_volume=None,
                 logical_volume_type=None,
                 name=None,
                 volume_guid=None):
        """Constructor for the FilesystemVolume class"""

        # Initialize members of the class
        self.disks = disks
        self.display_name = display_name
        self.filesystem_type = filesystem_type
        self.filesystem_uuid = filesystem_uuid
        self.is_supported = is_supported
        self.logical_volume = logical_volume
        self.logical_volume_type = logical_volume_type
        self.name = name
        self.volume_guid = volume_guid


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
        disks = None
        if dictionary.get('disks') != None:
            disks = list()
            for structure in dictionary.get('disks'):
                disks.append(cohesity_management_sdk.models.disk.Disk.from_dictionary(structure))
        display_name = dictionary.get('displayName')
        filesystem_type = dictionary.get('filesystemType')
        filesystem_uuid = dictionary.get('filesystemUuid')
        is_supported = dictionary.get('isSupported')
        logical_volume = cohesity_management_sdk.models.logical_volume.LogicalVolume.from_dictionary(dictionary.get('logicalVolume')) if dictionary.get('logicalVolume') else None
        logical_volume_type = dictionary.get('logicalVolumeType')
        name = dictionary.get('name')
        volume_guid = dictionary.get('volumeGuid')

        # Return an object of this model
        return cls(disks,
                   display_name,
                   filesystem_type,
                   filesystem_uuid,
                   is_supported,
                   logical_volume,
                   logical_volume_type,
                   name,
                   volume_guid)


