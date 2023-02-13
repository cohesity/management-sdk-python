# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.protection_source
import cohesity_management_sdk.models.virtual_disk_mapping_response

class VirtualDiskRestoreResponse(object):

    """Implementation of the 'VirtualDiskRestoreResponse' model.

    Specifies the parameters to recover virtual disks of a vm with full
    Protection Source.

    Attributes:
        power_off_vm_before_recovery (bool): Specifies whether to power off
            the VM before recovering virtual disks.
        power_on_vm_after_recovery (bool): Specifies whether to power on the
            VM after recovering virtual disks.
        target_source (ProtectionSource): Specifies a generic structure that
            represents a node in the Protection Source tree. Node details will
            depend on the environment of the Protection Source.
        virtual_disk_mappings (list of VirtualDiskMappingResponse): Specifies
            the list of virtual disks mappings.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "power_off_vm_before_recovery":'powerOffVmBeforeRecovery',
        "power_on_vm_after_recovery":'powerOnVmAfterRecovery',
        "target_source":'targetSource',
        "virtual_disk_mappings":'virtualDiskMappings'
    }

    def __init__(self,
                 power_off_vm_before_recovery=None,
                 power_on_vm_after_recovery=None,
                 target_source=None,
                 virtual_disk_mappings=None):
        """Constructor for the VirtualDiskRestoreResponse class"""

        # Initialize members of the class
        self.power_off_vm_before_recovery = power_off_vm_before_recovery
        self.power_on_vm_after_recovery = power_on_vm_after_recovery
        self.target_source = target_source
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
        target_source = cohesity_management_sdk.models.protection_source.ProtectionSource.from_dictionary(dictionary.get('targetSource')) if dictionary.get('targetSource') else None
        virtual_disk_mappings = None
        if dictionary.get('virtualDiskMappings') != None:
            virtual_disk_mappings = list()
            for structure in dictionary.get('virtualDiskMappings'):
                virtual_disk_mappings.append(cohesity_management_sdk.models.virtual_disk_mapping_response.VirtualDiskMappingResponse.from_dictionary(structure))

        # Return an object of this model
        return cls(power_off_vm_before_recovery,
                   power_on_vm_after_recovery,
                   target_source,
                   virtual_disk_mappings)


