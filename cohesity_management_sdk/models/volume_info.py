# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.volume_info_disk_info
import cohesity_management_sdk.models.volume_info_logical_volume_info
import cohesity_management_sdk.models.volume_info_sub_volume_info


class VolumeInfo(object):

    """Implementation of the 'VolumeInfo' model.

    TODO: type description here.


    Attributes:

        disk_vec (list of VolumeInfo_DiskInfo): Information about all the disks
            and partitions needed to mount this logical volume.
        display_name (string): Display name.
        filesystem_type (string): Filesystem on this volume.
        fs_label (string): Filesystem label.
        fs_uuid (string): Filesystem uuid.
        is_bootable (bool): Is this volume bootable?
        is_dedup (bool): Is this a dedup volume? Currently, set to true only
            for ntfs dedup volume.
        is_supported (bool): Is this a supported Volume (filesystem)?
        lv_info (VolumeInfo_LogicalVolumeInfo): This field is set only for lvm
            and ldm volume only.
        subvol_info (VolumeInfo_SubVolumeInfo): This is set to capture info
            about any active subvolume for this volume.
        volume_guid (string): The guid of the volume represented by this
            virtual disk. This information will be originally populated by
            magneto for physical environments.
        volume_identifier (int): We assign a unique number to every volume
            within a VM which we see for the first time. The identifier will be
            monotonically increasing number startin from 1.
        volume_source_type (int): The source type of the volume. This field is
            typically stamped before processing volume and used to customize
            process behavior like rpc timeout, max retries, mount options, etc.
        volume_type (int): Whether this volume is simple, lvm or ldm.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "disk_vec":'diskVec',
        "display_name":'displayName',
        "filesystem_type":'filesystemType',
        "fs_label":'fsLabel',
        "fs_uuid":'fsUuid',
        "is_bootable":'isBootable',
        "is_dedup":'isDedup',
        "is_supported":'isSupported',
        "lv_info":'lvInfo',
        "subvol_info":'subvolInfo',
        "volume_guid":'volumeGuid',
        "volume_identifier":'volumeIdentifier',
        "volume_source_type":'volumeSourceType',
        "volume_type":'volumeType',
    }
    def __init__(self,
                 disk_vec=None,
                 display_name=None,
                 filesystem_type=None,
                 fs_label=None,
                 fs_uuid=None,
                 is_bootable=None,
                 is_dedup=None,
                 is_supported=None,
                 lv_info=None,
                 subvol_info=None,
                 volume_guid=None,
                 volume_identifier=None,
                 volume_source_type=None,
                 volume_type=None,
            ):

        """Constructor for the VolumeInfo class"""

        # Initialize members of the class
        self.disk_vec = disk_vec
        self.display_name = display_name
        self.filesystem_type = filesystem_type
        self.fs_label = fs_label
        self.fs_uuid = fs_uuid
        self.is_bootable = is_bootable
        self.is_dedup = is_dedup
        self.is_supported = is_supported
        self.lv_info = lv_info
        self.subvol_info = subvol_info
        self.volume_guid = volume_guid
        self.volume_identifier = volume_identifier
        self.volume_source_type = volume_source_type
        self.volume_type = volume_type

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
        disk_vec = None
        if dictionary.get('diskVec') != None:
            disk_vec = list()
            for structure in dictionary.get('diskVec'):
                disk_vec.append(cohesity_management_sdk.models.volume_info_disk_info.VolumeInfo_DiskInfo.from_dictionary(structure))
        display_name = dictionary.get('displayName')
        filesystem_type = dictionary.get('filesystemType')
        fs_label = dictionary.get('fsLabel')
        fs_uuid = dictionary.get('fsUuid')
        is_bootable = dictionary.get('isBootable')
        is_dedup = dictionary.get('isDedup')
        is_supported = dictionary.get('isSupported')
        lv_info = cohesity_management_sdk.models.volume_info_logical_volume_info.VolumeInfo_LogicalVolumeInfo.from_dictionary(dictionary.get('lvInfo')) if dictionary.get('lvInfo') else None
        subvol_info = cohesity_management_sdk.models.volume_info_sub_volume_info.VolumeInfo_SubVolumeInfo.from_dictionary(dictionary.get('subvolInfo')) if dictionary.get('subvolInfo') else None
        volume_guid = dictionary.get('volumeGuid')
        volume_identifier = dictionary.get('volumeIdentifier')
        volume_source_type = dictionary.get('volumeSourceType')
        volume_type = dictionary.get('volumeType')

        # Return an object of this model
        return cls(
            disk_vec,
            display_name,
            filesystem_type,
            fs_label,
            fs_uuid,
            is_bootable,
            is_dedup,
            is_supported,
            lv_info,
            subvol_info,
            volume_guid,
            volume_identifier,
            volume_source_type,
            volume_type
)