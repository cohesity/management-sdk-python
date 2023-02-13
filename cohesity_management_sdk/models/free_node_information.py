# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class FreeNodeInformation(object):

    """Implementation of the 'FreeNodeInformation' model.

    Specifies the Metadata of a free Node on the network.

    Attributes:
        chassis_serial (string): Specifies the serial number of the Chassis
            the Node is installed in.
        connected_to (bool): Specifies whether or not this is the Node that is
            sending the response.
        hostname (string): Free node hostname.
        id (long|int): Specifies the ID of the node.
        ip (string): Deprecated. Specifies the IP address of the Node. Use Ips
            instead.
        ipmi_ip (string): Specifies the IPMI IP of the Node.
        ips (list of string): List of discovered ipv4/ipv6 addresses of the
            node. Ip field returns ips as comma separated single string which
            is incorrect.
        node_serial (string): Specifies the serial number of the Node.
        node_ui_slot (string): Specifies the postition for the UI to display
            the Node in the Cluster creation page.
        num_slots_in_chassis (int): Specifies the number of Node slots present
            in the Chassis where this Node is installed.
        product_model (string): Specifies the product model of the node.
        slot_number (string): Specifies the number of the slot the Node is
            installed in.
        software_version (string): Specifies the version of the software
            installed on the Node.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "chassis_serial":'chassisSerial',
        "connected_to":'connectedTo',
        "hostname":'hostname',
        "id":'id',
        "ip":'ip',
        "ipmi_ip":'ipmiIp',
        "ips":'ips',
        "node_serial":'nodeSerial',
        "node_ui_slot":'nodeUiSlot',
        "num_slots_in_chassis":'numSlotsInChassis',
        "product_model":'productModel',
        "slot_number":'slotNumber',
        "software_version":'softwareVersion'
    }

    def __init__(self,
                 chassis_serial=None,
                 connected_to=None,
                 hostname=None,
                 id=None,
                 ip=None,
                 ipmi_ip=None,
                 ips=None,
                 node_serial=None,
                 node_ui_slot=None,
                 num_slots_in_chassis=None,
                 product_model=None,
                 slot_number=None,
                 software_version=None):
        """Constructor for the FreeNodeInformation class"""

        # Initialize members of the class
        self.chassis_serial = chassis_serial
        self.connected_to = connected_to
        self.hostname = hostname
        self.id = id
        self.ip = ip
        self.ipmi_ip = ipmi_ip
        self.ips = ips
        self.node_serial = node_serial
        self.node_ui_slot = node_ui_slot
        self.num_slots_in_chassis = num_slots_in_chassis
        self.product_model = product_model
        self.slot_number = slot_number
        self.software_version = software_version


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
        connected_to = dictionary.get('connectedTo')
        hostname = dictionary.get('hostname')
        id = dictionary.get('id')
        ip = dictionary.get('ip')
        ipmi_ip = dictionary.get('ipmiIp')
        ips = dictionary.get('ips')
        node_serial = dictionary.get('nodeSerial')
        node_ui_slot = dictionary.get('nodeUiSlot')
        num_slots_in_chassis = dictionary.get('numSlotsInChassis')
        product_model = dictionary.get('productModel', None)
        slot_number = dictionary.get('slotNumber')
        software_version = dictionary.get('softwareVersion')

        # Return an object of this model
        return cls(chassis_serial,
                   connected_to,
                   hostname,
                   id,
                   ip,
                   ipmi_ip,
                   ips,
                   node_serial,
                   node_ui_slot,
                   num_slots_in_chassis,
                   product_model,
                   slot_number,
                   software_version)


