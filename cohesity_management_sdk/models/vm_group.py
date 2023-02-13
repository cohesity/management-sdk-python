# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.vm_info

class VmGroup(object):

    """Implementation of the 'VmGroup' model.

    VmGroup specifies information of a VM Group.

    Attributes:
        name (string): Specifies name of the VM group.
        vms (list of VmInfo): Specifies VMs in the group.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "vms":'vms'
    }

    def __init__(self,
                 name=None,
                 vms=None):
        """Constructor for the VmGroup class"""

        # Initialize members of the class
        self.name = name
        self.vms = vms


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
        name = dictionary.get('name')
        vms = None
        if dictionary.get('vms') != None:
            vms = list()
            for structure in dictionary.get('vms'):
                vms.append(cohesity_management_sdk.models.vm_info.VmInfo.from_dictionary(structure))

        # Return an object of this model
        return cls(name,
                   vms)


