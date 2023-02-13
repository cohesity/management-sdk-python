# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.node_port

class VmInfo(object):

    """Implementation of the 'VmInfo' model.

    VmInfo specifies information of a VM.

    Attributes:
        health_detail (string): Specifies the reason if vm is unhealthy.
        health_status (int): Specifies the current health status of the app
            instance.
        name (string): Specifies name of the VM.
        node_ports (list of NodePort): Specifies nodeports assigned to the
            vm.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "health_detail":'healthDetail',
        "health_status":'healthStatus',
        "name":'name',
        "node_ports":'nodePorts'
    }

    def __init__(self,
                 health_detail=None,
                 health_status=None,
                 name=None,
                 node_ports=None):
        """Constructor for the VmInfo class"""

        # Initialize members of the class
        self.health_detail = health_detail
        self.health_status = health_status
        self.name = name
        self.node_ports = node_ports


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
        health_detail = dictionary.get('healthDetail')
        health_status = dictionary.get('healthStatus')
        name = dictionary.get('name')
        node_ports = None
        if dictionary.get('nodePorts') != None:
            node_ports = list()
            for structure in dictionary.get('nodePorts'):
                node_ports.append(cohesity_management_sdk.models.node_port.NodePort.from_dictionary(structure))

        # Return an object of this model
        return cls(health_detail,
                   health_status,
                   name,
                   node_ports)


