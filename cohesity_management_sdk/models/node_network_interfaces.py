# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.network_interface

class NodeNetworkInterfaces(object):

    """Implementation of the 'NodeNetworkInterfaces' model.

    Specifies the network interfaces present on a specific Node in a Cluster.

    Attributes:
        chassis_serial (string): Specifies the serial number of Chassis.
        id (long|int): Specifies the ID of the Node.
        interfaces (list of NetworkInterface): Specifies the list of network
            interfaces present on this Node.
        message (string): Specifies an optional message describing the result
            of the request pertaining to this Node.
        slot (long|int): Specifies the slot number the Node is located in.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "chassis_serial":'chassisSerial',
        "id":'id',
        "interfaces":'interfaces',
        "message":'message',
        "slot":'slot'
    }

    def __init__(self,
                 chassis_serial=None,
                 id=None,
                 interfaces=None,
                 message=None,
                 slot=None):
        """Constructor for the NodeNetworkInterfaces class"""

        # Initialize members of the class
        self.chassis_serial = chassis_serial
        self.id = id
        self.interfaces = interfaces
        self.message = message
        self.slot = slot


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
        chassis_serial = dictionary.get('chassisSerial')
        id = dictionary.get('id')
        interfaces = None
        if dictionary.get('interfaces') != None:
            interfaces = list()
            for structure in dictionary.get('interfaces'):
                interfaces.append(cohesity_management_sdk.models.network_interface.NetworkInterface.from_dictionary(structure))
        message = dictionary.get('message')
        slot = dictionary.get('slot')

        # Return an object of this model
        return cls(chassis_serial,
                   id,
                   interfaces,
                   message,
                   slot)


