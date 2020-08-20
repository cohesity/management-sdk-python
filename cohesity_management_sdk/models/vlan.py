# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.subnet
import cohesity_management_sdk.models.ip_range

class Vlan(object):

    """Implementation of the 'Vlan' model.

    Specifies the settings of a VLAN. Its used by both Request and Response
    structures.

    Attributes:
        add_to_cluster_partition (bool): Specifies whether to add the VLAN IPs
            to the cluster partition that already has one or more IPs from
            this VLAN.
        all_tenant_access (bool): Specifies if this VLAN can be used by all
            tenants without explicit assignment to them. This option can only
            be set true for VLANs that are not assigned to any tenant.
        appsips (list of string): Array of Athena Apps IPs. Specifies a list
            of Athena IPs in the VLAN.
        description (string): Specifies a description of the VLAN.
        gateway (string): Specifies the Gateway of the VLAN.
        gateway_v6 (string):  Specifies the Gateway of the VLAN.
        hostname (string): Specifies the hostname of the VLAN.
        id (int): Specifies the id of the VLAN.
        iface_group_name (string): Specifies the interface group name of the
            VLAN. It is in the format of
            <base_interface_group_name>.<vlan_id>.
        interface_name (string): Specifies the interface name
        ip_family (int|long): Specifies IP family. Based on this,
            subnet/gateway field contains V4 or V6 values. Used in Request.
        ip_range (IpRange):  IP Range for vip addition
        ips (list of string): Array of IPs.  Specifies a list of IPs in the
            VLAN.
        mtu (int): TODO: type description here.
        subnet (Subnet): Specifies the subnet of the VLAN. The netmask can be
            specified by setting netmaskBits or netmaskIp4. The netmask can
            only be set using netmaskIp4 if the IP address is an IPv4
            address.
        subnet_v6 (Subnet): Specifies the subnet of the VLAN.
            The netmask can be specified by setting netmaskBits or netmaskIp4.
            The netmask can only be set using netmaskIp4 if the IP address is
            an IPv4 address.
        tenant_id (string): Optional tenant id that this vlan belongs to.
        vlan_name (string): Specifies the VLAN name of the vlanId.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "add_to_cluster_partition":'addToClusterPartition',
        "all_tenant_access":'allTenantAccess',
        "appsips":'appsips',
        "description":'description',
        "gateway":'gateway',
        "gateway_v6":'gatewayV6',
        "hostname":'hostname',
        "id":'id',
        "iface_group_name":'ifaceGroupName',
        "interface_name":'interfaceName',
        "ip_family":'ipFamily',
        "ip_range":'ipRange',
        "ips":'ips',
        "mtu":'mtu',
        "subnet":'subnet',
        "subnet_v6":'subnetV6',
        "tenant_id":'tenantId',
        "vlan_name":'vlanName'
    }

    def __init__(self,
                 add_to_cluster_partition=None,
                 all_tenant_access=None,
                 appsips=None,
                 description=None,
                 gateway=None,
                 gateway_v6=None,
                 hostname=None,
                 id=None,
                 iface_group_name=None,
                 interface_name=None,
                 ip_family=None,
                 ip_range=None,
                 ips=None,
                 mtu=None,
                 subnet=None,
                 subnet_v6=None,
                 tenant_id=None,
                 vlan_name=None):
        """Constructor for the Vlan class"""

        # Initialize members of the class
        self.add_to_cluster_partition = add_to_cluster_partition
        self.all_tenant_access = all_tenant_access
        self.appsips = appsips
        self.description = description
        self.gateway = gateway
        self.gateway_v6 = gateway_v6
        self.hostname = hostname
        self.id = id
        self.iface_group_name = iface_group_name
        self.interface_name = interface_name
        self.ip_family = ip_family
        self.ip_range = ip_range
        self.ips = ips
        self.mtu = mtu
        self.subnet = subnet
        self.subnet_v6 = subnet_v6
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
        appsips = dictionary.get('appsips')
        description = dictionary.get('description')
        gateway = dictionary.get('gateway')
        gateway_v6 = dictionary.get('gatewayV6')
        hostname = dictionary.get('hostname')
        id = dictionary.get('id')
        iface_group_name = dictionary.get('ifaceGroupName')
        interface_name = dictionary.get('interfaceName')
        ip_family = dictionary.get('ipFamily')
        ip_range = cohesity_management_sdk.models.ip_range.IpRange.from_dictionary(dictionary.get('ipRange')) if  dictionary.get('ipRange') else None
        ips = dictionary.get('ips')
        mtu = dictionary.get('mtu')
        subnet = cohesity_management_sdk.models.subnet.Subnet.from_dictionary(dictionary.get('subnet')) if dictionary.get('subnet') else None
        subnet_v6 = cohesity_management_sdk.models.subnet.Subnet.from_dictionary(dictionary.get('subnetV6')) if dictionary.get('subnetV6') else None
        tenant_id = dictionary.get('tenantId')
        vlan_name = dictionary.get('vlanName')

        # Return an object of this model
        return cls(add_to_cluster_partition,
                   all_tenant_access,
                   appsips,
                   description,
                   gateway,
                   gateway_v6,
                   hostname,
                   id,
                   iface_group_name,
                   interface_name,
                   ip_family,
                   ip_range,
                   ips,
                   mtu,
                   subnet,
                   subnet_v6,
                   tenant_id,
                   vlan_name)


