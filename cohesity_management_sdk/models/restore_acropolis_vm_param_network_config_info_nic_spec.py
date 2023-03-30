# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class RestoreAcropolisVMParamNetworkConfigInfoNICSpec(object):

    """Implementation of the 'RestoreAcropolisVMParam_NetworkConfigInfo_NICSpec' model.

    TODO: type model description here.

    Attributes:
        ip_address (string): IP address to assign to the NIC.
        network_uuid (string): The UUID of the network to which the NIC is to
            be attached.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ip_address":'ipAddress',
        "network_uuid":'networkUuid'
    }

    def __init__(self,
                 ip_address=None,
                 network_uuid=None):
        """Constructor for the RestoreAcropolisVMParamNetworkConfigInfoNICSpec class"""

        # Initialize members of the class
        self.ip_address = ip_address
        self.network_uuid = network_uuid


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
        network_uuid = dictionary.get('networkUuid')

        # Return an object of this model
        return cls(ip_address,
                   network_uuid)


