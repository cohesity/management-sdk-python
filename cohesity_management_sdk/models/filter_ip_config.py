# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class FilterIpConfig(object):

    """Implementation of the 'FilterIpConfig' model.

    Specifies the list of IP addresses that are allowed or denied at the job
    level. Allowed IPs and Denied IPs cannot be used together.

    Attributes:
        allowed_ip_addresses (list of string): Specifies the IP addresses that
            should be used exclusively at the job level. Cannot be set if
            deniedIpAddresses is set.
        denied_ip_addresses (list of string): Specifies the IP addresses that
            should not be used at the job level. Cannot be set if
            allowedIpAddresses is set.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "allowed_ip_addresses": 'allowedIpAddresses',
        "denied_ip_addresses": 'deniedIpAddresses'
    }

    def __init__(self,
                 allowed_ip_addresses=None,
                 denied_ip_addresses=None):
        """Constructor for the FilterIpConfig class"""

        # Initialize members of the class
        self.allowed_ip_addresses = allowed_ip_addresses
        self.denied_ip_addresses = denied_ip_addresses


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
        allowed_ip_addresses = dictionary.get('allowedIpAddresses', None)
        denied_ip_addresses = dictionary.get('deniedIpAddresses', None)

        # Return an object of this model
        return cls(allowed_ip_addresses,
                   denied_ip_addresses)


