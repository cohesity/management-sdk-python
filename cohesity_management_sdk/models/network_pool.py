# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.network_pool_range

class NetworkPool(object):

    """Implementation of the 'NetworkPool' model.

    Specifies the network pool config of an Isilon Access Zone.

    Attributes:
        address_family (AddressFamilyEnum): Specifies the enum for the IP
            address families.
            'kUnknown' indicates IP address families are unknown.
            'kIPv4' indicates IP addresses used are from IPv4 family.
            'kIPv6' indicates IP addresses used are from IPv6 family.
        allocation_method (AllocationMethodEnum): Specifies the enum for IP
            allocation method.
            'kUnknownAllocMethod' indicates allocation method is unknown.
            'kStaticAllocMethod' indicates static allocation method for IP
                addresses.
            'kDynamicAllocMethod' indicates dynamic allocation method for IP
                addresses.
        groupnet (string): Specifies the groupnet name of the network pool.
        id (string): Specifies the unique identifier of the network pool.
        name (string): Specifies the name of the network pool.
        ranges (list of NetworkPoolRange): Specifies the IP address range.
        smart_connect_dns_zone (string): Specifies the SmartConnect zone name
            of the network pool.
        subnet (string): Specifies the subnet name of the network pool.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address_family": 'addressFamily',
        "allocation_method": 'allocationMethod',
        "groupnet":'groupnet',
        "id":'id',
        "name":'name',
        "ranges":'ranges',
        "smart_connect_dns_zone":'smartConnectDnsZone',
        "subnet":'subnet'
    }

    def __init__(self,
                 address_family=None,
                 allocation_method=None,
                 groupnet=None,
                 id=None,
                 name=None,
                 ranges=None,
                 smart_connect_dns_zone=None,
                 subnet=None):
        """Constructor for the NetworkPool class"""

        # Initialize members of the class
        self.address_family = address_family
        self.allocation_method = allocation_method
        self.groupnet = groupnet
        self.id = id
        self.name = name
        self.ranges = ranges
        self.smart_connect_dns_zone = smart_connect_dns_zone
        self.subnet = subnet

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
        address_family = dictionary.get('addressFamily')
        allocation_method = dictionary.get('allocationMethod')
        groupnet = dictionary.get('groupnet')
        id = dictionary.get('id')
        name = dictionary.get('name')
        ranges = None
        if dictionary.get('ranges') != None:
            ranges = list()
            for structure in dictionary.get('ranges'):
                ranges.append(cohesity_management_sdk.models.network_pool_range.NetworkPoolRange.from_dictionary(structure))
        smart_connect_dns_zone = dictionary.get('smartConnectDnsZone')
        subnet = dictionary.get('subnet')

        # Return an object of this model
        return cls(address_family,
                   allocation_method,
                   groupnet,
                   id,
                   name,
                   ranges,
                   smart_connect_dns_zone,
                   subnet)


