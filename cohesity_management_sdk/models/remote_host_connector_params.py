# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.credentials

class RemoteHostConnectorParams(object):

    """Implementation of the 'RemoteHostConnectorParams' model.

    Contains parameters to connect to a remote host.

    Attributes:
        credentials (Credentials): Credentials that will be used to login to
            the remote host. For env of type kLinux, it is expected that user
            has setup the password-less access to the remote host. So only
            username field MUST be specified.
        host_address (string): Address (i.e., IP, hostname or FQDN) of the
            host to connect to. Magneto will connect using ssh or equivalent
            to the host.
        host_type (int): Execution status of the host_address.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "credentials":'credentials',
        "host_address":'hostAddress',
        "host_type":'hostType'
    }

    def __init__(self,
                 credentials=None,
                 host_address=None,
                 host_type=None):
        """Constructor for the RemoteHostConnectorParams class"""

        # Initialize members of the class
        self.credentials = credentials
        self.host_address = host_address
        self.host_type = host_type


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
        credentials = cohesity_management_sdk.models.credentials.Credentials.from_dictionary(dictionary.get('credentials')) if dictionary.get('credentials') else None
        host_address = dictionary.get('hostAddress')
        host_type = dictionary.get('hostType')

        # Return an object of this model
        return cls(credentials,
                   host_address,
                   host_type)


