# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class IpDetails(object):

    """Implementation of the 'IpDetails' model.

    IP address details
    The table below captures the type if information published by an entity
    type using this field.

    Attributes:
        details (string): Details of the IP Addresses captured below
        ip_addresses (list of string): The IP Addresses

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "details": 'details',
        "ip_addresses": 'ipAddresses'
    }

    def __init__(self,
                 details=None,
                 ip_addresses=None):
        """Constructor for the IpDetails class"""

        # Initialize members of the class
        self.details = details
        self.ip_addresses = ip_addresses


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
        details = dictionary.get('details', None)
        ip_addresses = dictionary.get('ipAddresses', None)

        # Return an object of this model
        return cls(details,
                   ip_addresses)


