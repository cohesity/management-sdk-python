# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.c2s_access_portal

class C2SServerInfo(object):

    """Implementation of the 'C2SServerInfo' model.

    C2S Server Info.

    Specifies information required to connect to CAP to get AWS credentials.
    C2SAccessPortal(CAP) is AWS commercial cloud service access portal.

    Attributes:
        c2s_access_portal (C2SAccessPortal): Specifies the C2S Access Portal
            (CAP) which is used to get the aws credentials in Amazon
            Commercial Cloud Service(C2S).
        ca_trusted_certificate (string): Specifies the CA (certificate
            authority) trusted certificate.
        client_certificate (string): Specifies the client CA  certificate.
            This certificate is in pem format.
        client_private_key (string): Specifies the client private key. This
            certificate is in pem format.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "c2s_access_portal":'c2sAccessPortal',
        "ca_trusted_certificate":'caTrustedCertificate',
        "client_certificate":'clientCertificate',
        "client_private_key":'clientPrivateKey'
    }

    def __init__(self,
                 c2s_access_portal=None,
                 ca_trusted_certificate=None,
                 client_certificate=None,
                 client_private_key=None):
        """Constructor for the C2SServerInfo class"""

        # Initialize members of the class
        self.c2s_access_portal = c2s_access_portal
        self.ca_trusted_certificate = ca_trusted_certificate
        self.client_certificate = client_certificate
        self.client_private_key = client_private_key


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
        c2s_access_portal = cohesity_management_sdk.models.c2s_access_portal.C2SAccessPortal.from_dictionary(dictionary.get('c2sAccessPortal')) if dictionary.get('c2sAccessPortal') else None
        ca_trusted_certificate = dictionary.get('caTrustedCertificate')
        client_certificate = dictionary.get('clientCertificate')
        client_private_key = dictionary.get('clientPrivateKey')

        # Return an object of this model
        return cls(c2s_access_portal,
                   ca_trusted_certificate,
                   client_certificate,
                   client_private_key)


