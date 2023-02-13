# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.vlan

class ClusterPartition(object):

    """Implementation of the 'ClusterPartition' model.

    Provides details about a Cluster Partition.

    Attributes:
        host_name (string): Specifies that hostname that resolves to one or
            more Virtual IP Addresses (VIPs).
        id (long|int): Specifies a unique identifier for the Cluster
            Partition.
        name (string): Specifies the name of the Cluster Partition.
        node_ids (list of long|int): Array of Node Ids.  Specifies a list of
            Node Ids that assigned to the Cluster Partition.
        vips (list of string): Array of VIPs.  Specifies a list of Virtual IP
            Addresses (VIPs) that route network traffic to the Cluster
            Partition.
        vlan_ips (list of string): Array of VLAN IPs.  Specifies a list of
            VLAN IP Addresses that route network traffic within certain VLANs
            to the Cluster Partition.
        vlans (list of Vlan): Array of VLANs.  Specifies a list of VLANs for
            the Cluster Partition.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "host_name":'hostName',
        "id":'id',
        "name":'name',
        "node_ids":'nodeIds',
        "vips":'vips',
        "vlan_ips":'vlanIps',
        "vlans":'vlans'
    }

    def __init__(self,
                 host_name=None,
                 id=None,
                 name=None,
                 node_ids=None,
                 vips=None,
                 vlan_ips=None,
                 vlans=None):
        """Constructor for the ClusterPartition class"""

        # Initialize members of the class
        self.host_name = host_name
        self.id = id
        self.name = name
        self.node_ids = node_ids
        self.vips = vips
        self.vlan_ips = vlan_ips
        self.vlans = vlans


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
        host_name = dictionary.get('hostName')
        id = dictionary.get('id')
        name = dictionary.get('name')
        node_ids = dictionary.get('nodeIds')
        vips = dictionary.get('vips')
        vlan_ips = dictionary.get('vlanIps')
        vlans = None
        if dictionary.get('vlans') != None:
            vlans = list()
            for structure in dictionary.get('vlans'):
                vlans.append(cohesity_management_sdk.models.vlan.Vlan.from_dictionary(structure))

        # Return an object of this model
        return cls(host_name,
                   id,
                   name,
                   node_ids,
                   vips,
                   vlan_ips,
                   vlans)


