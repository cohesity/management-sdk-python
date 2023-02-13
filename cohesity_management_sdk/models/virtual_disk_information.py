# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.protection_source

class VirtualDiskInformation(object):

    """Implementation of the 'VirtualDiskInformation' model.

    Specifies information about the virtual disk.

    Attributes:
        bus_number (long|int): Specifies the Id of the controller bus that
            controls the disk.
        controller_type (string): Specifies the controller type like SCSI, or
            IDE etc.
        disk_id (string): Specifies original disk id. This is sufficient to
            identify the disk information, but in some scenarios, user's may
            specify the controller option instead.
        disk_location (ProtectionSource): Specifies location of the disk, e.g.
            this will contain the location of datastore in VMware environment.
        disk_size_in_bytes (long|int): Specifies size of the virtual disk in
            bytes.
        file_path (string): Specifies the original file path if applicable.
        mount_points (list of string): Specifies the list of mount points.
        unit_number (long|int): Specifies the disk file name. This is the VMDK
            name and not the flat file name.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bus_number":'busNumber',
        "controller_type":'controllerType',
        "disk_id":'diskId',
        "disk_location":'diskLocation',
        "disk_size_in_bytes":'diskSizeInBytes',
        "file_path":'filePath',
        "mount_points":'mountPoints',
        "unit_number":'unitNumber'
    }

    def __init__(self,
                 bus_number=None,
                 controller_type=None,
                 disk_id=None,
                 disk_location=None,
                 disk_size_in_bytes=None,
                 file_path=None,
                 mount_points=None,
                 unit_number=None):
        """Constructor for the VirtualDiskInformation class"""

        # Initialize members of the class
        self.bus_number = bus_number
        self.controller_type = controller_type
        self.disk_id = disk_id
        self.disk_location = disk_location
        self.disk_size_in_bytes = disk_size_in_bytes
        self.file_path = file_path
        self.mount_points = mount_points
        self.unit_number = unit_number


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
        bus_number = dictionary.get('busNumber')
        controller_type = dictionary.get('controllerType')
        disk_id = dictionary.get('diskId')
        disk_location = cohesity_management_sdk.models.protection_source.ProtectionSource.from_dictionary(dictionary.get('diskLocation')) if dictionary.get('diskLocation') else None
        disk_size_in_bytes = dictionary.get('diskSizeInBytes')
        file_path = dictionary.get('filePath')
        mount_points = dictionary.get('mountPoints')
        unit_number = dictionary.get('unitNumber')

        # Return an object of this model
        return cls(bus_number,
                   controller_type,
                   disk_id,
                   disk_location,
                   disk_size_in_bytes,
                   file_path,
                   mount_points,
                   unit_number)


