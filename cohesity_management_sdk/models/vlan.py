# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.subnet

class Vlan(object):

    """Implementation of the 'Vlan' model.

    Specifies the settings of a VLAN.

    Attributes:
        add_to_cluster_partition (bool): Specifies whether to add the VLAN IPs
            to the cluster partition that already has one or more IPs from
            this VLAN.
        all_tenant_access (bool): Specifies if this VLAN can be used by all
            tenants without explicit assignment to them. This option can only
            be set true for VLANs that are not assigned to any tenant.
        description (string): Specifies a description of the VLAN.
        gateway (string): Specifies the Gateway of the VLAN.
        hostname (string): Specifies the hostname of the VLAN.
        id (int): Specifies the id of the VLAN.
        iface_group_name (string): Specifies the interface group name of the
            VLAN. It is in the format of
            <base_interface_group_name>.<vlan_id>.
        interface_name (string): Specifies the interface name of the VLAN.
        ips (list of string): Array of IPs.  Specifies a list of IPs in the
            VLAN.
        subnet (Subnet): Specifies the subnet of the VLAN. The netmask can be
            specified by setting netmaskBits or netmaskIp4. The netmask can
            only be set using netmaskIp4 if the IP address is an IPv4
            address.
        tenant_id (string): Optional tenant id that this vlan belongs to.
        vlan_name (string): Specifies the VLAN name of the vlanId.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "add_to_cluster_partition":'addToClusterPartition',
        "all_tenant_access":'allTenantAccess',
        "description":'description',
        "gateway":'gateway',
        "hostname":'hostname',
        "id":'id',
        "iface_group_name":'ifaceGroupName',
        "interface_name":'interfaceName',
        "ips":'ips',
        "subnet":'subnet',
        "tenant_id":'tenantId',
        "vlan_name":'vlanName'
    }

    def __init__(self,
                 add_to_cluster_partition=None,
                 all_tenant_access=None,
                 description=None,
                 gateway=None,
                 hostname=None,
                 id=None,
                 iface_group_name=None,
                 interface_name=None,
                 ips=None,
                 subnet=None,
                 tenant_id=None,
                 vlan_name=None):
        """Constructor for the Vlan class"""

        # Initialize members of the class
        self.add_to_cluster_partition = add_to_cluster_partition
        self.all_tenant_access = all_tenant_access
        self.description = description
        self.gateway = gateway
        self.hostname = hostname
        self.id = id
        self.iface_group_name = iface_group_name
        self.interface_name = interface_name
        self.ips = ips
        self.subnet = subnet
        self.tenant_id = tenant_id
        self.vlan_name = vlan_name


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
        add_to_cluster_partition = dictionary.get('addToClusterPartition')
        all_tenant_access = dictionary.get('allTenantAccess')
        description = dictionary.get('description')
        gateway = dictionary.get('gateway')
        hostname = dictionary.get('hostname')
        id = dictionary.get('id')
        iface_group_name = dictionary.get('ifaceGroupName')
        interface_name = dictionary.get('interfaceName')
        ips = dictionary.get('ips')
        subnet = cohesity_management_sdk.models.subnet.Subnet.from_dictionary(dictionary.get('subnet')) if dictionary.get('subnet') else None
        tenant_id = dictionary.get('tenantId')
        vlan_name = dictionary.get('vlanName')

        # Return an object of this model
        return cls(add_to_cluster_partition,
                   all_tenant_access,
                   description,
                   gateway,
                   hostname,
                   id,
                   iface_group_name,
                   interface_name,
                   ips,
                   subnet,
                   tenant_id,
                   vlan_name)


