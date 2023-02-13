# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class DeviceTreePartitionSlice(object):

    """Implementation of the 'DeviceTree_PartitionSlice' model.

    TODO: type model description here.

    Attributes:
        disk_file_name (string): The disk to use.
        length (long|int): The length of data for the LVM volume (for which
            this device tree is being built) in bytes. It does not include
            size of the LVM meta data.
        lvm_data_offset (long|int): Each LVM partition starts with LVM meta
            data. After the meta data there can be data for one or more LVM
            volumes.  This field indicates the offset in bytes (relative to
            partition) where data for various LVM volumes starts on the
            partition. NOTE: If this device tree represents first LVM volume
            on the  partition, 'lvm_data_offset' is equal to 'offset'.
        offset (long|int): This is the offset (in bytes) where data for the
            LVM volume (for which this device tree is being build) starts
            relative to the start of the partition above.
        partition_number (int): The partition to use in the disk above.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "disk_file_name":'diskFileName',
        "length":'length',
        "lvm_data_offset":'lvmDataOffset',
        "offset":'offset',
        "partition_number":'partitionNumber'
    }

    def __init__(self,
                 disk_file_name=None,
                 length=None,
                 lvm_data_offset=None,
                 offset=None,
                 partition_number=None):
        """Constructor for the DeviceTreePartitionSlice class"""

        # Initialize members of the class
        self.disk_file_name = disk_file_name
        self.length = length
        self.lvm_data_offset = lvm_data_offset
        self.offset = offset
        self.partition_number = partition_number


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
        length = dictionary.get('length')
        lvm_data_offset = dictionary.get('lvmDataOffset')
        offset = dictionary.get('offset')
        partition_number = dictionary.get('partitionNumber')

        # Return an object of this model
        return cls(disk_file_name,
                   length,
                   lvm_data_offset,
                   offset,
                   partition_number)


