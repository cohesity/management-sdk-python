# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.recover_virtual_disk_params_virtual_disk_mapping

class RecoverVirtualDiskParams(object):

    """Implementation of the 'RecoverVirtualDiskParams' model.

    TODO: type model description here.

    Attributes:
        power_off_vm_before_recovery (bool): Whether to power-off the VM
            before recovering virtual disks.
        power_on_vm_after_recovery (bool): Whether to power-on the VM after
            recovering virtual disks.
        target_entity (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        virtual_disk_mappings (list of
            RecoverVirtualDiskParamsVirtualDiskMapping): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "power_off_vm_before_recovery":'powerOffVmBeforeRecovery',
        "power_on_vm_after_recovery":'powerOnVmAfterRecovery',
        "target_entity":'targetEntity',
        "virtual_disk_mappings":'virtualDiskMappings'
    }

    def __init__(self,
                 power_off_vm_before_recovery=None,
                 power_on_vm_after_recovery=None,
                 target_entity=None,
                 virtual_disk_mappings=None):
        """Constructor for the RecoverVirtualDiskParams class"""

        # Initialize members of the class
        self.power_off_vm_before_recovery = power_off_vm_before_recovery
        self.power_on_vm_after_recovery = power_on_vm_after_recovery
        self.target_entity = target_entity
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
        target_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('targetEntity')) if dictionary.get('targetEntity') else None
        virtual_disk_mappings = None
        if dictionary.get('virtualDiskMappings') != None:
            virtual_disk_mappings = list()
            for structure in dictionary.get('virtualDiskMappings'):
                virtual_disk_mappings.append(cohesity_management_sdk.models.recover_virtual_disk_params_virtual_disk_mapping.RecoverVirtualDiskParamsVirtualDiskMapping.from_dictionary(structure))

        # Return an object of this model
        return cls(power_off_vm_before_recovery,
                   power_on_vm_after_recovery,
                   target_entity,
                   virtual_disk_mappings)


