# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.virtual_disk_mapping

class VirtualDiskRestoreParameters(object):

    """Implementation of the 'VirtualDiskRestoreParameters' model.

    Specifies the parameters to recover virtual disks of a vm.

    Attributes:
        power_off_vm_before_recovery (bool): Specifies whether to power off
            the VM before recovering virtual disks.
        power_on_vm_after_recovery (bool): Specifies whether to power on the
            VM after recovering virtual disks.
        target_source_id (long|int): Specifies the target entity to which the
            disks should be attached.
        virtual_disk_mappings (list of VirtualDiskMapping): Specifies the list
            of virtual disks mappings.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "power_off_vm_before_recovery":'powerOffVmBeforeRecovery',
        "power_on_vm_after_recovery":'powerOnVmAfterRecovery',
        "target_source_id":'targetSourceId',
        "virtual_disk_mappings":'virtualDiskMappings'
    }

    def __init__(self,
                 power_off_vm_before_recovery=None,
                 power_on_vm_after_recovery=None,
                 target_source_id=None,
                 virtual_disk_mappings=None):
        """Constructor for the VirtualDiskRestoreParameters class"""

        # Initialize members of the class
        self.power_off_vm_before_recovery = power_off_vm_before_recovery
        self.power_on_vm_after_recovery = power_on_vm_after_recovery
        self.target_source_id = target_source_id
        self.virtual_disk_mappings = virtual_disk_mappings


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
        power_off_vm_before_recovery = dictionary.get('powerOffVmBeforeRecovery')
        power_on_vm_after_recovery = dictionary.get('powerOnVmAfterRecovery')
        target_source_id = dictionary.get('targetSourceId')
        virtual_disk_mappings = None
        if dictionary.get('virtualDiskMappings') != None:
            virtual_disk_mappings = list()
            for structure in dictionary.get('virtualDiskMappings'):
                virtual_disk_mappings.append(cohesity_management_sdk.models.virtual_disk_mapping.VirtualDiskMapping.from_dictionary(structure))

        # Return an object of this model
        return cls(power_off_vm_before_recovery,
                   power_on_vm_after_recovery,
                   target_source_id,
                   virtual_disk_mappings)


