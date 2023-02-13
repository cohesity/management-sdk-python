# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.subnet
import cohesity_management_sdk.models.ip_range
import cohesity_management_sdk.models.dns_delegation_zone

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
        app_ip_vec_in_use (bool): Set to true when ips are in use by Athena
            Apps. Note: If it is true then vlan interface can't be deleted.
        appsips (list of string): Array of Athena Apps IPs. Specifies a list
            of Athena IPs in the VLAN.
        description (string): Specifies a description of the VLAN.
        dns_delegation_zones (list of DnsDelegationZone): Specifies list of
            dns delegation zones.
        ecmp_enabled (bool): EcmpEnabled. Specifies if ECMP is enabled in the
            VLAN.
        gateway (string): Specifies the Gateway of the VLAN.
        gateway_v6 (string):  Specifies the Gateway of the VLAN.
        hostname (string): Specifies the hostname of the VLAN.
        id (int): Specifies the id of the VLAN.
        iface_group_name (string): Specifies the interface group name of the
            VLAN. It is in the format of
            <base_interface_group_name>.<vlan_id>.
        interface_group_id (int): Specifies the id of the Loopback Interface
            group. Used only in get, for display.
        interface_name (string): Specifies the interface name
        ip_family (int|long): Specifies IP family. Based on this,
            subnet/gateway field contains V4 or V6 values. Used in Request.
        ip_pool_map (dict<object, list of string>): IpPoolMap. Pool IPs to
            program VIP followers.
        ip_range (IpRange):  IP Range for vip addition
        ip_ranges (list of IpRange): Array of range of ips. If specified in
            PUT request, Ips field will be ignored. Specifies ips in
            compressed way using list of [start, end] vips.
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
        "app_ip_vec_in_use":'appIpVecInUse',
        "appsips":'appsips',
        "description":'description',
        "dns_delegation_zones":'dnsDelegationZones',
        "ecmp_enabled":'ecmpEnabled',
        "gateway":'gateway',
        "gateway_v6":'gatewayV6',
        "hostname":'hostname',
        "id":'id',
        "iface_group_name":'ifaceGroupName',
        "interface_group_id":'interfaceGroupId',
        "interface_name":'interfaceName',
        "ip_family":'ipFamily',
        "ip_pool_map":'ipPoolMap',
        "ip_range":'ipRange',
        "ip_ranges":'ipRanges',
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
                 app_ip_vec_in_use=None,
                 appsips=None,
                 description=None,
                 dns_delegation_zones=None,
                 ecmp_enabled=None,
                 gateway=None,
                 gateway_v6=None,
                 hostname=None,
                 id=None,
                 iface_group_name=None,
                 interface_group_id=None,
                 interface_name=None,
                 ip_family=None,
                 ip_pool_map=None,
                 ip_range=None,
                 ip_ranges=None,
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
        self.app_ip_vec_in_use = app_ip_vec_in_use
        self.appsips = appsips
        self.description = description
        self.dns_delegation_zones = dns_delegation_zones
        self.ecmp_enabled = ecmp_enabled
        self.gateway = gateway
        self.gateway_v6 = gateway_v6
        self.hostname = hostname
        self.id = id
        self.iface_group_name = iface_group_name
        self.interface_group_id = interface_group_id
        self.interface_name = interface_name
        self.ip_family = ip_family
        self.ip_pool_map = ip_pool_map
        self.ip_range = ip_range
        self.ip_ranges = ip_ranges
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
        app_ip_vec_in_use = dictionary.get('appIpVecInUse')
        appsips = dictionary.get('appsips')
        description = dictionary.get('description')
        dns_delegation_zones = None
        if dictionary.get('dnsDelegationZones') != None:
            dns_delegation_zones = list()
            for structure in dictionary.get('dnsDelegationZones'):
                dns_delegation_zones.append(cohesity_management_sdk.models.dns_delegation_zone.DnsDelegationZone.from_dictionary(structure))
        ecmp_enabled = dictionary.get('ecmpEnabled')
        gateway = dictionary.get('gateway')
        gateway_v6 = dictionary.get('gatewayV6')
        hostname = dictionary.get('hostname')
        id = dictionary.get('id')
        iface_group_name = dictionary.get('ifaceGroupName')
        interface_group_id = dictionary.get('interfaceGroupId')
        interface_name = dictionary.get('interfaceName')
        ip_family = dictionary.get('ipFamily')
        ip_pool_map = dictionary.get('ipPoolMap')
        ip_range = cohesity_management_sdk.models.ip_range.IpRange.from_dictionary(dictionary.get('ipRange')) if  dictionary.get('ipRange') else None
        ip_ranges = None
        if dictionary.get('ipRanges') != None:
            ip_ranges = list()
            for structure in dictionary.get('ipRanges'):
                ip_ranges.append(cohesity_management_sdk.models.ip_range.IpRange.from_dictionary(structure))
        ips = dictionary.get('ips')
        mtu = dictionary.get('mtu')
        subnet = cohesity_management_sdk.models.subnet.Subnet.from_dictionary(dictionary.get('subnet')) if dictionary.get('subnet') else None
        subnet_v6 = cohesity_management_sdk.models.subnet.Subnet.from_dictionary(dictionary.get('subnetV6')) if dictionary.get('subnetV6') else None
        tenant_id = dictionary.get('tenantId')
        vlan_name = dictionary.get('vlanName')

        # Return an object of this model
        return cls(add_to_cluster_partition,
                   all_tenant_access,
                   app_ip_vec_in_use,
                   appsips,
                   description,
                   dns_delegation_zones,
                   ecmp_enabled,
                   gateway,
                   gateway_v6,
                   hostname,
                   id,
                   iface_group_name,
                   interface_group_id,
                   interface_name,
                   ip_family,
                   ip_pool_map,
                   ip_range,
                   ip_ranges,
                   ips,
                   mtu,
                   subnet,
                   subnet_v6,
                   tenant_id,
                   vlan_name)


