# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class VmwareParams(object):

    """Implementation of the 'VmwareParams' model.

    TODO: Type description here.

    Attributes:
        use_vm_bios_uuid (bool): Specifies to use VM BIOS UUID to track virtual
        machines in the host.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "use_vm_bios_uuid":'useVmBiosUuid'
    }

    def __init__(self,
                 use_vm_bios_uuid=None):
        """Constructor for the VmwareParams class"""

        # Initialize members of the class
        self.use_vm_bios_uuid = use_vm_bios_uuid


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
        use_vm_bios_uuid = dictionary.get('useVmBiosUuid')

        # Return an object of this model
        return cls(use_vm_bios_uuid)


