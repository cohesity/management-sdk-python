# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.disk_block
import cohesity_management_sdk.models.disk_partition

class Disk(object):

    """Implementation of the 'Disk' model.

    Specifies information about a disk and partitions in a volume.

    Attributes:
        disk_blocks (list of DiskBlock): Array of Disk Blocks.  Specifies a
            set of disk blocks by defining the location and offset of disk
            blocks in a disk.
        disk_format (DiskFormatEnum): Specifies the format of the virtual
            disk. 'kVMDK' indicates VMware's Virtual Disk format. 'kVHD'
            indicates Microsoft's Virtual Hard Drive format. 'kVHDx' indicates
            Microsoft's Hyper-V Virtual Hard Drive format. 'kRaw' indicates
            Raw disk format used by KVM, Acropolis. 'kUnknow' indicates
            Unknown disk format.
        disk_partitions (list of DiskPartition): Array of Partitions.
            Specifies information about all the partitions in this disk.
        partition_table_format (PartitionTableFormatEnum): Specifies partition
            table format on a disk. 'kNoPartition' indicates missing partition
            table. 'kMBRPartition' indicates partition table is in Master Boot
            Record format. 'kGPTPartition' indicates partition table is in
            Guid Partition Table format. 'kSGIPartition' indicates partition
            table uses SGI scheme. 'kSUNPartition' indicates partition table
            uses SUN scheme.
        sector_size_bytes (long|int): Specifies the sector size of hard disk.
            It is used for mapping the disk blocks of the disk file into a
            linear list of sectors.
        uuid (string): Specifies the disk uuid.
        vmdk_file_name (string): Specifies the disk file name. This is the
            VMDK name and not the flat file name.
        vmdk_size_bytes (long|int): Specifies the disk size in bytes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "disk_blocks":'diskBlocks',
        "disk_format":'diskFormat',
        "disk_partitions":'diskPartitions',
        "partition_table_format":'partitionTableFormat',
        "sector_size_bytes":'sectorSizeBytes',
        "uuid":'uuid',
        "vmdk_file_name":'vmdkFileName',
        "vmdk_size_bytes":'vmdkSizeBytes'
    }

    def __init__(self,
                 disk_blocks=None,
                 disk_format=None,
                 disk_partitions=None,
                 partition_table_format=None,
                 sector_size_bytes=None,
                 uuid=None,
                 vmdk_file_name=None,
                 vmdk_size_bytes=None):
        """Constructor for the Disk class"""

        # Initialize members of the class
        self.disk_blocks = disk_blocks
        self.disk_format = disk_format
        self.disk_partitions = disk_partitions
        self.partition_table_format = partition_table_format
        self.sector_size_bytes = sector_size_bytes
        self.uuid = uuid
        self.vmdk_file_name = vmdk_file_name
        self.vmdk_size_bytes = vmdk_size_bytes


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
        disk_blocks = None
        if dictionary.get('diskBlocks') != None:
            disk_blocks = list()
            for structure in dictionary.get('diskBlocks'):
                disk_blocks.append(cohesity_management_sdk.models.disk_block.DiskBlock.from_dictionary(structure))
        disk_format = dictionary.get('diskFormat')
        disk_partitions = None
        if dictionary.get('diskPartitions') != None:
            disk_partitions = list()
            for structure in dictionary.get('diskPartitions'):
                disk_partitions.append(cohesity_management_sdk.models.disk_partition.DiskPartition.from_dictionary(structure))
        partition_table_format = dictionary.get('partitionTableFormat')
        sector_size_bytes = dictionary.get('sectorSizeBytes')
        uuid = dictionary.get('uuid')
        vmdk_file_name = dictionary.get('vmdkFileName')
        vmdk_size_bytes = dictionary.get('vmdkSizeBytes')

        # Return an object of this model
        return cls(disk_blocks,
                   disk_format,
                   disk_partitions,
                   partition_table_format,
                   sector_size_bytes,
                   uuid,
                   vmdk_file_name,
                   vmdk_size_bytes)


