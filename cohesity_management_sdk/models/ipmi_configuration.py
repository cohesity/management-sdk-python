# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class IpmiConfiguration(object):

    """Implementation of the 'IpmiConfiguration' model.

    Specifies the parameters for configuration of IPMI. This is only needed
    for physical clusters.

    Attributes:
        ipmi_gateway (string): Specifies the default Gateway IP Address for
            the IPMI network.
        ipmi_password (string): Specifies the IPMI Password.
        ipmi_subnet_mask (string): Specifies the subnet mask for the IPMI
            network.
        ipmi_username (string): Specifies the IPMI Username.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ipmi_gateway":'ipmiGateway',
        "ipmi_password":'ipmiPassword',
        "ipmi_subnet_mask":'ipmiSubnetMask',
        "ipmi_username":'ipmiUsername'
    }

    def __init__(self,
                 ipmi_gateway=None,
                 ipmi_password=None,
                 ipmi_subnet_mask=None,
                 ipmi_username=None):
        """Constructor for the IpmiConfiguration class"""

        # Initialize members of the class
        self.ipmi_gateway = ipmi_gateway
        self.ipmi_password = ipmi_password
        self.ipmi_subnet_mask = ipmi_subnet_mask
        self.ipmi_username = ipmi_username


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
        ipmi_gateway = dictionary.get('ipmiGateway')
        ipmi_password = dictionary.get('ipmiPassword')
        ipmi_subnet_mask = dictionary.get('ipmiSubnetMask')
        ipmi_username = dictionary.get('ipmiUsername')

        # Return an object of this model
        return cls(ipmi_gateway,
                   ipmi_password,
                   ipmi_subnet_mask,
                   ipmi_username)


