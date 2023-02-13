# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class DiskPartition(object):

    """Implementation of the 'DiskPartition' model.

    Specifies information about each partition in a physical disk.

    Attributes:
        length_bytes (long|int): Specifies the length of the block in bytes.
        number (long|int): Specifies a unique number of the partition within
            the linear disk file.
        offset_bytes (long|int): Specifies the offset of the block (in bytes)
            from the beginning of the containing object such as a physical
            disk or a virtual disk file.
        type_uuid (string): Specifies the partition type uuid. If disk is
            unpartitioned, this field is not set. If disk is MBR partitioned,
            this field is set to a partition type. If disk is GPT partitioned,
            this field is set to a partition type GUID.
        uuid (string): Specifies the partition uuid. If disk is unpartitioned,
            this field is not set. If disk is MBR partitioned, this field is
            not set. If disk is GPT partitioned, this field is set to a
            partition GUID.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "length_bytes":'lengthBytes',
        "number":'number',
        "offset_bytes":'offsetBytes',
        "type_uuid":'typeUuid',
        "uuid":'uuid'
    }

    def __init__(self,
                 length_bytes=None,
                 number=None,
                 offset_bytes=None,
                 type_uuid=None,
                 uuid=None):
        """Constructor for the DiskPartition class"""

        # Initialize members of the class
        self.length_bytes = length_bytes
        self.number = number
        self.offset_bytes = offset_bytes
        self.type_uuid = type_uuid
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
        length_bytes = dictionary.get('lengthBytes')
        number = dictionary.get('number')
        offset_bytes = dictionary.get('offsetBytes')
        type_uuid = dictionary.get('typeUuid')
        uuid = dictionary.get('uuid')

        # Return an object of this model
        return cls(length_bytes,
                   number,
                   offset_bytes,
                   type_uuid,
                   uuid)


