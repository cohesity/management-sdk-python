# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class VmNumReplicas(object):

    """Implementation of the 'VmNumReplicas' model.

    TODO: Type description here.

    Attributes:
        num_replicas (long|int): Replica count.
        vm_name (string): Vm-name.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "num_replicas": 'numReplicas',
        "vm_name": 'vmName'
    }

    def __init__(self,
                 num_replicas=None,
                 vm_name=None):
        """Constructor for the VmNumReplicas class"""

        # Initialize members of the class
        self.num_replicas = num_replicas
        self.vm_name = vm_name


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
        num_replicas = dictionary.get('numReplicas', None)
        vm_name = dictionary.get('vmName', None)

        # Return an object of this model
        return cls(num_replicas,
                   vm_name)


