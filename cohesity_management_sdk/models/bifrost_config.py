# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.bifrost_subnet

class BifrostConfig(object):

    """Implementation of the 'BifrostConfig' model.

    Specifies the settings of a BifrostConfig. Its used by both Request and
    Response structures.

    Attributes:
        image_version (string): Specifies the bifrost image version.
        cpu (int): Specifies the cpu for the bifrost config.
        description (string): Specifies a description of the VLAN.
        id (int): Specifies the id of the VLAN tag.
        iface_group_name (string): Specifies the interface group name of the VLAN. It
            is in the format of <base_interface_group_name>.<vlan_id>.
        memory (int): Specifies the memory for the bifrost config.
        mtu (int): Specifies the mtu for the bifrost vlan.
        state (string): 4 types of States
            UNKNOWN
            ACTIVE
            DISABLED
            DELETING
        subnet (BifrostSubnet): Specifies the subnet of the VLAN.
            The netmask can be specified by setting netmaskBits or netmaskIp4.
            The netmask can only be set using netmaskIp4 if the IP address is
            an IPv4 address. It can carry V4 or V6 in case of requests, and
            carries V4 in case of response.
        tenant_id (string): Specifies the tenant id that this vlan belongs to.
            mcm-on-prem-mode. If set to true, it is in mcm on prem mode. This
            need mcm-mode to be true.
        mtype (string): Two types of bifrost vlans.
            INTERNAL
            EXTERNAL
        vlan_name (string): Specifies the VLAN name of the vlanId.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "image_version":'ImageVersion',
        "cpu":'cpu',
        "description":'description',
        "id":'id',
        "iface_group_name":'ifaceGroupName',
        "memory":'memory',
        "mtu":'mtu',
        "state":'state',
        "subnet":'subnet',
        "tenant_id":'tenantId',
        "mtype":'type',
        "vlan_name":'vlanName'
    }

    def __init__(self,
                 image_version=None,
                 cpu=None,
                 description=None,
                 id=None,
                 iface_group_name=None,
                 memory=None,
                 mtu=None,
                 state=None,
                 subnet=None,
                 tenant_id=None,
                 mtype=None,
                 vlan_name=None):
        """Constructor for the BifrostConfig class"""

        # Initialize members of the class
        self.image_version = image_version
        self.cpu = cpu
        self.description = description
        self.id = id
        self.iface_group_name = iface_group_name
        self.memory = memory
        self.mtu = mtu
        self.state = state
        self.subnet = subnet
        self.tenant_id = tenant_id
        self.mtype = mtype
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
        image_version = dictionary.get('ImageVersion')
        cpu = dictionary.get('cpu')
        description = dictionary.get('description')
        id = dictionary.get('id')
        iface_group_name = dictionary.get('ifaceGroupName')
        memory = dictionary.get('memory')
        mtu = dictionary.get('mtu')
        state = dictionary.get('state')
        subnet = cohesity_management_sdk.models.bifrost_subnet.BifrostSubnet.from_dictionary(dictionary.get('subnet')) if dictionary.get('subnet') else None
        tenant_id = dictionary.get('tenantId')
        mtype = dictionary.get('type')
        vlan_name = dictionary.get('vlanName')

        # Return an object of this model
        return cls(image_version,
                   cpu,
                   description,
                   id,
                   iface_group_name,
                   memory,
                   mtu,
                   state,
                   subnet,
                   tenant_id,
                   mtype,
                   vlan_name)


