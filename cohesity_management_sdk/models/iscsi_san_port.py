# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class IscsiSanPort(object):

    """Implementation of the 'IscsiSanPort' model.

    Specifies an iSCSI SAN Port.

    Attributes:
        ip_address (string): Specifies the IP address of the SAN port.
        iqn (string): Specifies the qualified name of the iSCSI port (IQN).
        tcp_port (int): Specifies the listening port(tcp) of the SAN port.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ip_address":'ipAddress',
        "iqn":'iqn',
        "tcp_port":'tcpPort'
    }

    def __init__(self,
                 ip_address=None,
                 iqn=None,
                 tcp_port=None):
        """Constructor for the IscsiSanPort class"""

        # Initialize members of the class
        self.ip_address = ip_address
        self.iqn = iqn
        self.tcp_port = tcp_port


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
        ip_address = dictionary.get('ipAddress')
        iqn = dictionary.get('iqn')
        tcp_port = dictionary.get('tcpPort')

        # Return an object of this model
        return cls(ip_address,
                   iqn,
                   tcp_port)


