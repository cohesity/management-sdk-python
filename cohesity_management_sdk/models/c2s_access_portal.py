# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class C2SAccessPortal(object):

    """Implementation of the 'C2SAccessPortal' model.

    Specifies information required to connect to CAP to get AWS credentials.
    C2SAccessPortal(CAP) is AWS commercial cloud service access portal.

    Attributes:
        agency (string): Name of the agency.
        base_url (string): Specifies the instance name of the Universal Data
            Adapter entity.
        client_certificate_password (string): Encrypted password of the client
            private key.
        mission (string): Name of the mission.
        role (string): Role type.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "agency":'agency',
        "base_url":'baseUrl',
        "client_certificate_password":'clientCertificatePassword',
        "mission":'mission',
        "role":'role'
    }

    def __init__(self,
                 agency=None,
                 base_url=None,
                 client_certificate_password=None,
                 mission=None,
                 role=None):
        """Constructor for the C2SAccessPortal class"""

        # Initialize members of the class
        self.agency = agency
        self.base_url = base_url
        self.client_certificate_password = client_certificate_password
        self.mission = mission
        self.role = role


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
        agency = dictionary.get('agency')
        base_url = dictionary.get('baseUrl')
        client_certificate_password = dictionary.get('clientCertificatePassword')
        role = dictionary.get('role')
        mission = dictionary.get('mission')

        # Return an object of this model
        return cls(agency,
                   base_url,
                   client_certificate_password,
                   mission,
                   role)


