# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class VserverNetworkInterface(object):

    """Implementation of the 'VserverNetworkInterface' model.

    Specifies information about a logical network interface on a
    NetApp Vserver. The interface's IP address is the mount point for a
    specific data protocol, such as NFS or CIFS.

    Attributes:
        data_protocols (list of DataProtocolEnum): Array of Data Protocols.
            Specifies the set of data protocols supported by this interface.
            'kNfs' indicates NFS connections. 'kCifs' indicates SMB (CIFS)
            connections. 'kIscsi' indicates iSCSI connections. 'kFc' indicates
            Fiber Channel connections. 'kFcache' indicates Flex Cache
            connections. 'kHttp' indicates HTTP connections. 'kNdmp' indicates
            NDMP connections. 'kManagement' indicates non-data connections
            used for management purposes.
        ip_address (string): Specifies the IP address of this interface.
        name (string): Specifies the name of this interface.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data_protocols":'dataProtocols',
        "ip_address":'ipAddress',
        "name":'name'
    }

    def __init__(self,
                 data_protocols=None,
                 ip_address=None,
                 name=None):
        """Constructor for the VserverNetworkInterface class"""

        # Initialize members of the class
        self.data_protocols = data_protocols
        self.ip_address = ip_address
        self.name = name


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
        ip_address = dictionary.get('ipAddress')
        name = dictionary.get('name')

        # Return an object of this model
        return cls(data_protocols,
                   ip_address,
                   name)


