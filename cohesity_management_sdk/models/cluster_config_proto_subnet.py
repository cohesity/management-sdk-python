# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ClusterConfigProto_Subnet(object):

    """Implementation of the 'ClusterConfigProto_Subnet' model.

    TODO: type description here.


    Attributes:

        component (int): The component that has claimed this subnet.
        description (string): Description of the subnet.
        gateway (string): Gateway for the subnet.
        id (int): ID for this subnet.
        ip (string): ip is subnet IP address given either in v4 or v6. Netmask
            is specified by giving CIDR length in netmask_bits for ipv6. For
            IPv4 addresses, netmask_ip4 field is set in dotted decimal.
        netmask_bits (int): TODO: Type description here.
        netmask_ip_4 (string): TODO: Type description here.
        nfs_access (int): Whether clients from this subnet can mount using NFS
            protocol.
        nfs_all_squash (bool): Whether all clients from this subnet can map
            view with view_all_squash_uid/view_all_squash_gid configured in the
            view.
        nfs_root_squash (bool): Whether clients from this subnet can mount as
            root on NFS.
        s3_access (int): Whether clients from this subnet can accept requests
            using S3 protocol.
        smb_access (int): Whether clients from this subnet can mount using SMB
            protocol.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "component":'component',
        "description":'description',
        "gateway":'gateway',
        "id":'id',
        "ip":'ip',
        "netmask_bits":'netmaskBits',
        "netmask_ip_4":'netmaskIp4',
        "nfs_access":'nfsAccess',
        "nfs_all_squash":'nfsAllSquash',
        "nfs_root_squash":'nfsRootSquash',
        "s3_access":'s3Access',
        "smb_access":'smbAccess',
    }
    def __init__(self,
                 component=None,
                 description=None,
                 gateway=None,
                 id=None,
                 ip=None,
                 netmask_bits=None,
                 netmask_ip_4=None,
                 nfs_access=None,
                 nfs_all_squash=None,
                 nfs_root_squash=None,
                 s3_access=None,
                 smb_access=None,
            ):

        """Constructor for the ClusterConfigProto_Subnet class"""

        # Initialize members of the class
        self.component = component
        self.description = description
        self.gateway = gateway
        self.id = id
        self.ip = ip
        self.netmask_bits = netmask_bits
        self.netmask_ip_4 = netmask_ip_4
        self.nfs_access = nfs_access
        self.nfs_all_squash = nfs_all_squash
        self.nfs_root_squash = nfs_root_squash
        self.s3_access = s3_access
        self.smb_access = smb_access

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
        component = dictionary.get('component')
        description = dictionary.get('description')
        gateway = dictionary.get('gateway')
        id = dictionary.get('id')
        ip = dictionary.get('ip')
        netmask_bits = dictionary.get('netmaskBits')
        netmask_ip_4 = dictionary.get('netmaskIp4')
        nfs_access = dictionary.get('nfsAccess')
        nfs_all_squash = dictionary.get('nfsAllSquash')
        nfs_root_squash = dictionary.get('nfsRootSquash')
        s3_access = dictionary.get('s3Access')
        smb_access = dictionary.get('smbAccess')

        # Return an object of this model
        return cls(
            component,
            description,
            gateway,
            id,
            ip,
            netmask_bits,
            netmask_ip_4,
            nfs_access,
            nfs_all_squash,
            nfs_root_squash,
            s3_access,
            smb_access
)