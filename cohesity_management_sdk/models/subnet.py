# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class Subnet(object):

    """Implementation of the 'Subnet' model.

    Defines a Subnet (Subnetwork).
    The netmask can be specified by setting netmaskBits or netmaskIp4.
    The netmask can only be set using netmaskIp4 if the IP address
    is an IPv4 address.

    Attributes:
        component (string): Component that has reserved the subnet.
        description (string): Description of the subnet.
        id (int): ID of the subnet.
        ip (string): Specifies either an IPv6 address or an IPv4 address.
        netmask_bits (int): Specifies the netmask using bits.
        netmask_ip_4 (string): Specifies the netmask using an IP4 address. The
            netmask can only be set using netmaskIp4 if the IP address is an
            IPv4 address.
        nfs_access (NfsAccessEnum): Specifies whether clients from this subnet
            can mount using NFS protocol. Protocol access level. 'kDisabled'
            indicates Protocol access level 'Disabled' 'kReadOnly' indicates
            Protocol access level 'ReadOnly' 'kReadWrite' indicates Protocol
            access level 'ReadWrite'
        nfs_all_squash (bool): Specifies whether all clients from this subnet
            can map view with view_all_squash_uid/view_all_squash_gid
            configured in the view.
        nfs_root_squash (bool): Specifies whether clients from this subnet can
            mount as root on NFS.
        smb_access (SmbAccessEnum): Specifies whether clients from this subnet
            can mount using SMB protocol. Protocol access level. 'kDisabled'
            indicates Protocol access level 'Disabled' 'kReadOnly' indicates
            Protocol access level 'ReadOnly' 'kReadWrite' indicates Protocol
            access level 'ReadWrite'
        s3_access (S3AccessEnum): Specifies whether clients from this subnet
            can access using S3 protocol.
            Protocol access level.
            'kDisabled' indicates Protocol access level 'Disabled'
            'kReadOnly' indicates Protocol access level 'ReadOnly'
            'kReadWrite' indicates Protocol access level 'ReadWrite'
        tenant_id (string): Specifies the unique id of the tenant.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "component":'component',
        "description":'description',
        "id":'id',
        "ip":'ip',
        "netmask_bits":'netmaskBits',
        "netmask_ip_4":'netmaskIp4',
        "nfs_access":'nfsAccess',
        "nfs_all_squash":'nfsAllSquash',
        "nfs_root_squash":'nfsRootSquash',
        "s3_access":'s3Access',
        "smb_access":'smbAccess',
        "tenant_id":'tenantId'
    }

    def __init__(self,
                 component=None,
                 description=None,
                 id=None,
                 ip=None,
                 netmask_bits=None,
                 netmask_ip_4=None,
                 nfs_access=None,
                 nfs_all_squash=None,
                 nfs_root_squash=None,
                 s3_access=None,
                 smb_access=None,
                 tenant_id=None):
        """Constructor for the Subnet class"""

        # Initialize members of the class
        self.component = component
        self.description = description
        self.id = id
        self.ip = ip
        self.netmask_bits = netmask_bits
        self.netmask_ip_4 = netmask_ip_4
        self.nfs_access = nfs_access
        self.nfs_all_squash = nfs_all_squash
        self.nfs_root_squash = nfs_root_squash
        self.s3_access = s3_access
        self.smb_access = smb_access
        self.tenant_id = tenant_id


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
        id = dictionary.get('id')
        ip = dictionary.get('ip')
        netmask_bits = dictionary.get('netmaskBits')
        netmask_ip_4 = dictionary.get('netmaskIp4')
        nfs_access = dictionary.get('nfsAccess')
        nfs_all_squash = dictionary.get('nfsAllSquash')
        nfs_root_squash = dictionary.get('nfsRootSquash')
        s3_access = dictionary.get('s3Access')
        smb_access = dictionary.get('smbAccess')
        tenant_id = dictionary.get('tenantId')

        # Return an object of this model
        return cls(component,
                   description,
                   id,
                   ip,
                   netmask_bits,
                   netmask_ip_4,
                   nfs_access,
                   nfs_all_squash,
                   nfs_root_squash,
                   s3_access,
                   smb_access,
                   tenant_id)


