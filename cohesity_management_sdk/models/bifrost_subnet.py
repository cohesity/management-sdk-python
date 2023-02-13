# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class BifrostSubnet(object):

    """Implementation of the 'BifrostSubnet' model.

    Specifies the settings of a Bifrost Subnet.

    Attributes:
        gateway (string): Specifies the Gateway of the VLAN. It can carry V4
            or V6 in case of requests, and carrises V4 in case of response.
        ip_cidr (string): Specifies either an IPv6 address or an IPv4 address.
        ips (list of string): Array of IPs.
            Specifies a list of IPs in the VLAN.
        netmask_bits (int): Specifies the netmask using bits.
        netmask_ip4 (string): Specifies the netmask using an IP4 address.
            The netmask can only be set using netmaskIp4 if the IP address
            is an IPv4 address.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "gateway": 'gateway',
        "ip_cidr": 'ipCidr',
        "ips": 'ips',
        "netmask_bits": 'netmaskBits',
        "netmask_ip4":'netmaskIp4'
    }

    def __init__(self,
                 gateway=None,
                 ip_cidr=None,
                 ips=None,
                 netmask_bits=None,
                 netmask_ip4=None):
        """Constructor for the BifrostSubnet class"""

        # Initialize members of the class
        self.gateway = gateway
        self.ip_cidr = ip_cidr
        self.ips = ips
        self.netmask_bits = netmask_bits
        self.netmask_ip4 = netmask_ip4

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
        ip_cidr = dictionary.get('ipCidr')
        ips = dictionary.get('ips')
        netmask_bits = dictionary.get('netmaskBits')
        netmask_ip4 = dictionary.get('netmaskIp4')

        # Return an object of this model
        return cls(gateway,
                   ip_cidr,
                   ips,
                   netmask_bits,
                   netmask_ip4)


