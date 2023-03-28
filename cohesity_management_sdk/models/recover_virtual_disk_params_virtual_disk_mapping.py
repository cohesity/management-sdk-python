# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.virtual_disk_id


class RecoverVirtualDiskParams_VirtualDiskMapping(object):

    """Implementation of the 'RecoverVirtualDiskParams_VirtualDiskMapping' model.

    TODO: type description here.


    Attributes:

        disk_to_overwrite (VirtualDiskId): If the user is overwriting a
            destination disk, then this will capture the target disk info.
            NOTE: If this is specified, then power_off_vm_before_recovery must
            be true.
        src_disk (VirtualDiskId): The source disk information.
        target_location (EntityProto): This contains the target location
            information, for e.g. a datastore in VMware environment. NOTE: If
            disk_to_overwrite is specified then the target location is
            automatically deduced, if not this must be specified.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "disk_to_overwrite":'diskToOverwrite',
        "src_disk":'srcDisk',
        "target_location":'targetLocation',
    }
    def __init__(self,
                 disk_to_overwrite=None,
                 src_disk=None,
                 target_location=None,
            ):

        """Constructor for the RecoverVirtualDiskParams_VirtualDiskMapping class"""

        # Initialize members of the class
        self.disk_to_overwrite = disk_to_overwrite
        self.src_disk = src_disk
        self.target_location = target_location

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
        disk_to_overwrite = cohesity_management_sdk.models.virtual_disk_id.VirtualDiskId.from_dictionary(dictionary.get('diskToOverwrite')) if dictionary.get('diskToOverwrite') else None
        src_disk = cohesity_management_sdk.models.virtual_disk_id.VirtualDiskId.from_dictionary(dictionary.get('srcDisk')) if dictionary.get('srcDisk') else None
        target_location = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('targetLocation')) if dictionary.get('targetLocation') else None

        # Return an object of this model
        return cls(
            disk_to_overwrite,
            src_disk,
            target_location
)