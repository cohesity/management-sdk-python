# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class HostEntry(object):

    """Implementation of the 'HostEntry' model.

    Specifies the parameters of a host entry that can be stored in the
    cluster's /etc/hosts file.

    Attributes:
        description (string): Description the host entry.
        domain_names (list of string): Specifies the domain names of the
            host.
        ip (string): Specifies the IP address of the host.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description":'description',
        "domain_names":'domainNames',
        "ip":'ip'
    }

    def __init__(self,
                 description=None,
                 domain_names=None,
                 ip=None):
        """Constructor for the HostEntry class"""

        # Initialize members of the class
        self.description = description
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
        description = dictionary.get('description')
        domain_names = dictionary.get('domainNames')
        ip = dictionary.get('ip')

        # Return an object of this model
        return cls(description,
                   domain_names,
                   ip)


