# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class OracleVlanInfo(object):

    """Implementation of the 'OracleVlanInfo' model.

    TODO: Type model description here.

    Attributes:
        gateway (string): Gateway for this VLAN.
        id (int): ID of this VLAN.
        ip_vec (list of string): List of IPs in this VLAN.
        subnet_ip (string): Subnet IP for this VLAN.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "gateway":'gateway',
        "id":'id',
        "ip_vec":'ipVec',
        "subnet_ip":'subnetIp'
    }

    def __init__(self,
                 gateway=None,
                 id=None,
                 ip_vec=None,
                 subnet_ip=None):
        """Constructor for the OracleVlanInfo class"""

        # Initialize members of the class
        self.gateway = gateway
        self.id = id
        self.ip_vec = ip_vec
        self.subnet_ip = subnet_ip


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
        gateway = dictionary.get('gateway')
        id = dictionary.get('id')
        ip_vec = dictionary.get('ipVec')
        subnet_ip = dictionary.get('subnetIp')

        # Return an object of this model
        return cls(gateway,
                   id,
                   ip_vec,
                   subnet_ip)

