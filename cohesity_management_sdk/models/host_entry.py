# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class HostEntry(object):

    """Implementation of the 'HostEntry' model.

    Specifies the parameters of a host entry that can be stored in the
    cluster's /etc/hosts file.

    Attributes:
        domain_names (list of string): Specifies the domain names of the
            host.
        ip (string): Specifies the IP address of the host.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "domain_names":'domainNames',
        "ip":'ip'
    }

    def __init__(self,
                 domain_names=None,
                 ip=None):
        """Constructor for the HostEntry class"""

        # Initialize members of the class
        self.domain_names = domain_names
        self.ip = ip


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
        domain_names = dictionary.get('domainNames')
        ip = dictionary.get('ip')

        # Return an object of this model
        return cls(domain_names,
                   ip)


