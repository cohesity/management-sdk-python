# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.host_entry

class AppendHostsParameters(object):

    """Implementation of the 'AppendHostsParameters' model.

    Specifies the parameters needed for an append hosts request.

    Attributes:
        hosts (list of HostEntry): Specifies the list of host entries to be
            added to the Cluster's etc/hosts file.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "hosts":'hosts'
    }

    def __init__(self,
                 hosts=None):
        """Constructor for the AppendHostsParameters class"""

        # Initialize members of the class
        self.hosts = hosts


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
        hosts = None
        if dictionary.get('hosts') != None:
            hosts = list()
            for structure in dictionary.get('hosts'):
                hosts.append(cohesity_management_sdk.models.host_entry.HostEntry.from_dictionary(structure))

        # Return an object of this model
        return cls(hosts)


