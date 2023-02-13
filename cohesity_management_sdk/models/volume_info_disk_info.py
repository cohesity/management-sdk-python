# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.volume_info_disk_info_partition_info
import cohesity_management_sdk.models.volume_info_disk_info_physical_range

class VolumeInfoDiskInfo(object):

    """Implementation of the 'VolumeInfo_DiskInfo' model.

    Information about each disk in volume.

    Attributes:
        disk_file_name (string): Disk name. This is the vmdk names, and not
            the flat file name.
        disk_format (int): Disk format type of this file. See
            util/disklib/base/enums.proto for available types.
        disk_uuid (string): Disk uuid.
        partition_type (int): Disk partition type.
        partition_vec (list of VolumeInfoDiskInfoPartitionInfo): Information
            about all the partitions in this disk.
        physical_range_vec (list of VolumeInfoDiskInfoPhysicalRange): This
            disk is formed by following physical ranges. Ranges are arranged
            sequentially to form a disk.
        sector_size (long|int): Sector size of disk. This is sector size of
            disk which is formed by mapping the physical ranges of the disk
            into a linear device.
        vmdk_size (long|int): Disk size in bytes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "disk_file_name":'diskFileName',
        "disk_format":'diskFormat',
        "disk_uuid":'diskUuid',
        "partition_type":'partitionType',
        "partition_vec":'partitionVec',
        "physical_range_vec":'physicalRangeVec',
        "sector_size":'sectorSize',
        "vmdk_size":'vmdkSize'
    }

    def __init__(self,
                 disk_file_name=None,
                 disk_format=None,
                 disk_uuid=None,
                 partition_type=None,
                 partition_vec=None,
                 physical_range_vec=None,
                 sector_size=None,
                 vmdk_size=None):
        """Constructor for the VolumeInfoDiskInfo class"""

        # Initialize members of the class
        self.disk_file_name = disk_file_name
        self.disk_format = disk_format
        self.disk_uuid = disk_uuid
        self.partition_type = partition_type
        self.partition_vec = partition_vec
        self.physical_range_vec = physical_range_vec
        self.sector_size = sector_size
        self.vmdk_size = vmdk_size


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
        disk_file_name = dictionary.get('diskFileName')
        disk_format = dictionary.get('diskFormat')
        disk_uuid = dictionary.get('diskUuid')
        partition_type = dictionary.get('partitionType')
        partition_vec = None
        if dictionary.get('partitionVec') != None:
            partition_vec = list()
            for structure in dictionary.get('partitionVec'):
                partition_vec.append(cohesity_management_sdk.models.volume_info_disk_info_partition_info.VolumeInfoDiskInfoPartitionInfo.from_dictionary(structure))
        physical_range_vec = None
        if dictionary.get('physicalRangeVec') != None:
            physical_range_vec = list()
            for structure in dictionary.get('physicalRangeVec'):
                physical_range_vec.append(cohesity_management_sdk.models.volume_info_disk_info_physical_range.VolumeInfoDiskInfoPhysicalRange.from_dictionary(structure))
        sector_size = dictionary.get('sectorSize')
        vmdk_size = dictionary.get('vmdkSize')

        # Return an object of this model
        return cls(disk_file_name,
                   disk_format,
                   disk_uuid,
                   partition_type,
                   partition_vec,
                   physical_range_vec,
                   sector_size,
                   vmdk_size)


