# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.vserver_network_interface
import cohesity_management_sdk.models.cifs_share_info

class NetappVserverInfo(object):

    """Implementation of the 'NetappVserverInfo' model.

    Specifies information about a NetApp Vserver in a NetApp Protection
    Source.

    Attributes:
        data_protocols (list of DataProtocolEnum): Array of Data Protocols.
            Specifies the set of data protocols supported by this Vserver. The
            kManagement protocol is not supported for this case. 'kNfs'
            indicates NFS connections. 'kCifs' indicates SMB (CIFS)
            connections. 'kIscsi' indicates iSCSI connections. 'kFc' indicates
            Fiber Channel connections. 'kFcache' indicates Flex Cache
            connections. 'kHttp' indicates HTTP connections. 'kNdmp' indicates
            NDMP connections. 'kManagement' indicates non-data connections
            used for management purposes. 'kNvme' indicates NVMe connections.
        interfaces (list of VserverNetworkInterface): Array of Interfaces.
            Specifies information about all interfaces on this Vserver.
        root_cifs_share (CifsShareInfo): Specifies information about a CIFS
            share of a NetApp volume.
        mtype (TypeNetappVserverInfoEnum): Specifies the type of this Vserver.
            Specifies the type of the NetApp Vserver. 'kData' indicates the
            Vserver is used for data backup and restore. 'kAdmin' indicates
            the Vserver is used for cluster-wide management. 'kSystem'
            indicates the Vserver is used for cluster-scoped communications in
            an IPspace. 'kNode' indicates the Vserver is used as the physical
            controller. 'kUnknown' indicates the Vserver is used for an
            unknown purpose.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data_protocols":'dataProtocols',
        "interfaces":'interfaces',
        "root_cifs_share":'rootCifsShare',
        "mtype":'type'
    }

    def __init__(self,
                 data_protocols=None,
                 interfaces=None,
                 root_cifs_share=None,
                 mtype=None):
        """Constructor for the NetappVserverInfo class"""

        # Initialize members of the class
        self.data_protocols = data_protocols
        self.interfaces = interfaces
        self.root_cifs_share = root_cifs_share
        self.mtype = mtype


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
        data_protocols = dictionary.get('dataProtocols')
        interfaces = None
        if dictionary.get('interfaces') != None:
            interfaces = list()
            for structure in dictionary.get('interfaces'):
                interfaces.append(cohesity_management_sdk.models.vserver_network_interface.VserverNetworkInterface.from_dictionary(structure))
        root_cifs_share = cohesity_management_sdk.models.cifs_share_info.CifsShareInfo.from_dictionary(dictionary.get('rootCifsShare')) if dictionary.get('rootCifsShare') else None
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(data_protocols,
                   interfaces,
                   root_cifs_share,
                   mtype)


