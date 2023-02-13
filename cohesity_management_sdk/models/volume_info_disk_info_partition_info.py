# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class VolumeInfoDiskInfoPartitionInfo(object):

    """Implementation of the 'VolumeInfo_DiskInfo_PartitionInfo' model.

    Offset/Length here is relative to the logical range starting at 0,
    formed by mapping the physical ranges of the disk into a linear device.

    Attributes:
        length (long|int): Length of partition in bytes.
        partition_number (long|int): Partition number.
        partition_type_uuid (string): Partition type uuid. If disk is
            unpartitioned, this field will not be set. If disk is MBR
            partitioned, this field will be set to partition type. Example: 83
            (from below fdisk output) [This value is in hex] bash$ fdisk -l
            foobar.vmdk Device        Boot Start   End    Sectors  Size Id
            Type foobar.vmdk1       2048  1050623  1048576  512M 83 Linux If
            disk is GPT partitioned, this field will be set to partition type
            GUID. Example: fc63daf-8483-4772-8e793d69d8477de4 (Linux
            filesystem data)
        partition_uuid (string): Partition uuid. If disk is unpartitioned,
            this field will not be set. If disk is MBR partitioned, this field
            will not be set. If disk is GPT partitioned, this field will be
            set to partition GUID.
        start_offset (long|int): Start offset of partition in bytes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "length":'length',
        "partition_number":'partitionNumber',
        "partition_type_uuid":'partitionTypeUuid',
        "partition_uuid":'partitionUuid',
        "start_offset":'startOffset'
    }

    def __init__(self,
                 length=None,
                 partition_number=None,
                 partition_type_uuid=None,
                 partition_uuid=None,
                 start_offset=None):
        """Constructor for the VolumeInfoDiskInfoPartitionInfo class"""

        # Initialize members of the class
        self.length = length
        self.partition_number = partition_number
        self.partition_type_uuid = partition_type_uuid
        self.partition_uuid = partition_uuid
        self.start_offset = start_offset


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
        length = dictionary.get('length')
        partition_number = dictionary.get('partitionNumber')
        partition_type_uuid = dictionary.get('partitionTypeUuid')
        partition_uuid = dictionary.get('partitionUuid')
        start_offset = dictionary.get('startOffset')

        # Return an object of this model
        return cls(length,
                   partition_number,
                   partition_type_uuid,
                   partition_uuid,
                   start_offset)


