# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.cifs_share_info
import cohesity_management_sdk.models.volume_security_info

class NetappVolumeInfo(object):

    """Implementation of the 'NetappVolumeInfo' model.

    Specifies information about a volume in a NetApp cluster.

    Attributes:
        aggregate_name (string): Specifies the containing aggregate name of
            this volume.
        capacity_bytes (long|int): Specifies the total capacity in bytes of
            this volume.
        cifs_shares (list of CifsShareInfo): Array of CIFS Shares.  Specifies
            the set of CIFS Shares exported for this volume.
        creation_time_usecs (long|int): Specifies the creation time of the
            volume specified in Unix epoch time (in microseconds).
        data_protocols (list of DataProtocolEnum): Array of Data Protocols.
            Specifies the set of data protocols supported by this volume.
            'kNfs' indicates NFS connections. 'kCifs' indicates SMB (CIFS)
            connections. 'kIscsi' indicates iSCSI connections. 'kFc' indicates
            Fiber Channel connections. 'kFcache' indicates Flex Cache
            connections. 'kHttp' indicates HTTP connections. 'kNdmp' indicates
            NDMP connections. 'kManagement' indicates non-data connections
            used for management purposes. 'kNvme' indicates NVMe connections.
        export_policy_name (string): Specifies the name of the export policy
            (which defines the access permissions for the mount client) that
            has been assigned to this volume.
        junction_path (string): Specifies the junction path of this volume.
            This path can be used to mount this volume via protocols such as
            NFS.
        name (string): Specifies the name of the NetApp Vserver that this
            volume belongs to.
        security_info (VolumeSecurityInfo): Specifies information about NetApp
            volume security settings.
        state (StateEnum): Specifies the state of this volume. Specifies the
            state of a NetApp Volume. 'kOnline' indicates the volume is
            online. Read and write access to this volume is allowed.
            'kRestricted' indicates the volume is restricted. Some operations,
            such as parity reconstruction, are allowed, but data access is not
            allowed. 'kOffline' indicates the volume is offline. No access to
            the volume is allowed. 'kMixed' indicates the volume is in mixed
            state, which means its aggregates are not all in the same state.
        mtype (TypeNetappVolumeInfoEnum): Specifies the NetApp type of this
            volume. Specifies the type of a NetApp Volume. 'kReadWrite'
            indicates read-write volume. 'kLoadSharing' indicates load-sharing
            volume. 'kDataProtection' indicates data-protection volume.
            'kDataCache' indicates data-cache volume. 'kTmp' indicates
            temporary purpose. 'kUnknownType' indicates unknown type.
        used_bytes (long|int): Specifies the total space (in bytes) used in
            this volume.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "aggregate_name":'aggregateName',
        "capacity_bytes":'capacityBytes',
        "cifs_shares":'cifsShares',
        "creation_time_usecs":'creationTimeUsecs',
        "data_protocols":'dataProtocols',
        "export_policy_name":'exportPolicyName',
        "junction_path":'junctionPath',
        "name":'name',
        "security_info":'securityInfo',
        "state":'state',
        "mtype":'type',
        "used_bytes":'usedBytes'
    }

    def __init__(self,
                 aggregate_name=None,
                 capacity_bytes=None,
                 cifs_shares=None,
                 creation_time_usecs=None,
                 data_protocols=None,
                 export_policy_name=None,
                 junction_path=None,
                 name=None,
                 security_info=None,
                 state=None,
                 mtype=None,
                 used_bytes=None):
        """Constructor for the NetappVolumeInfo class"""

        # Initialize members of the class
        self.aggregate_name = aggregate_name
        self.capacity_bytes = capacity_bytes
        self.cifs_shares = cifs_shares
        self.creation_time_usecs = creation_time_usecs
        self.data_protocols = data_protocols
        self.export_policy_name = export_policy_name
        self.junction_path = junction_path
        self.name = name
        self.security_info = security_info
        self.state = state
        self.mtype = mtype
        self.used_bytes = used_bytes


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
        aggregate_name = dictionary.get('aggregateName')
        capacity_bytes = dictionary.get('capacityBytes')
        cifs_shares = None
        if dictionary.get('cifsShares') != None:
            cifs_shares = list()
            for structure in dictionary.get('cifsShares'):
                cifs_shares.append(cohesity_management_sdk.models.cifs_share_info.CifsShareInfo.from_dictionary(structure))
        creation_time_usecs = dictionary.get('creationTimeUsecs')
        data_protocols = dictionary.get('dataProtocols')
        export_policy_name = dictionary.get('exportPolicyName')
        junction_path = dictionary.get('junctionPath')
        name = dictionary.get('name')
        security_info = cohesity_management_sdk.models.volume_security_info.VolumeSecurityInfo.from_dictionary(dictionary.get('securityInfo')) if dictionary.get('securityInfo') else None
        state = dictionary.get('state')
        mtype = dictionary.get('type')
        used_bytes = dictionary.get('usedBytes')

        # Return an object of this model
        return cls(aggregate_name,
                   capacity_bytes,
                   cifs_shares,
                   creation_time_usecs,
                   data_protocols,
                   export_policy_name,
                   junction_path,
                   name,
                   security_info,
                   state,
                   mtype,
                   used_bytes)


