# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class VmLinkingInfo(object):

    """Implementation of the 'VmLinkingInfo' model.

    Specifies the parameters for configuration of IPMI. This is only needed
    for physical clusters.

    Attributes:
        is_migrated (bool): This is set to true if a VM is linked in entity
            provenance by edge type kVMMigration.
        migrated_time_usecs (long|int): This is the time when ther VM was
            identified to have been migrated by Cohesity. Note that this time
            can differ from the actual migration time in vCenter.
        previous_vm_entity_id (long|int): This is the id of the VM on the
            vCenter where it was originally present
        previous_vm_parent_source_id (long|int): This is the id of vCenter
            where the VM was originally present

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "is_migrated":'isMigrated',
        "migrated_time_usecs":'migratedTimeUsecs',
        "previous_vm_entity_id":'previousVmEntityId',
        "previous_vm_parent_source_id":'previousVmParentSourceId'
    }

    def __init__(self,
                 is_migrated=None,
                 migrated_time_usecs=None,
                 previous_vm_entity_id=None,
                 previous_vm_parent_source_id=None):
        """Constructor for the VmLinkingInfo class"""

        # Initialize members of the class
        self.is_migrated = is_migrated
        self.migrated_time_usecs = migrated_time_usecs
        self.previous_vm_entity_id = previous_vm_entity_id
        self.previous_vm_parent_source_id = previous_vm_parent_source_id


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
        is_migrated = dictionary.get('isMigrated')
        migrated_time_usecs = dictionary.get('migratedTimeUsecs')
        previous_vm_entity_id = dictionary.get('previousVmEntityId')
        previous_vm_parent_source_id = dictionary.get('previousVmParentSourceId')

        # Return an object of this model
        return cls(is_migrated,
                   migrated_time_usecs,
                   previous_vm_entity_id,
                   previous_vm_parent_source_id)


