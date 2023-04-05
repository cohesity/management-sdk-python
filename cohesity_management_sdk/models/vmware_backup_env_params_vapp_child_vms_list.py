# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class VmwareBackupEnvParams_VAppChildVmsList(object):

    """Implementation of the 'VmwareBackupEnvParams_VAppChildVmsList' model.

    TODO: type description here.


    Attributes:

        vapp_entity_id (long|int): vApp entity id.
        vm_entity_ids (list of long|int): List of entity ids of all child VMs
            under vApp with id 'vapp_entity_id'.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "vapp_entity_id":'vappEntityId',
        "vm_entity_ids":'vmEntityIds',
    }
    def __init__(self,
                 vapp_entity_id=None,
                 vm_entity_ids=None,
            ):

        """Constructor for the VmwareBackupEnvParams_VAppChildVmsList class"""

        # Initialize members of the class
        self.vapp_entity_id = vapp_entity_id
        self.vm_entity_ids = vm_entity_ids

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
        vapp_entity_id = dictionary.get('vappEntityId')
        vm_entity_ids = dictionary.get("vmEntityIds")

        # Return an object of this model
        return cls(
            vapp_entity_id,
            vm_entity_ids
)