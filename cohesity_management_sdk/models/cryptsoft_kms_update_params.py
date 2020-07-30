# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class CryptsoftKmsUpdateParams(object):

    """Implementation of the 'CryptsoftKmsUpdateParams' model.

    Specifies the parameters for kmip KMS configuration.

    Attributes:
        ca_certificate (string): Specifies the CA certificate in PEM format.
        client_certificate (string): Specifies the client certificate.
            It is in PEM format.
        client_key (string): Specifies the client private key.
        kmip_protocol_version (string): Specifies protocol version used to
            communicate with the KMS.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ca_certificate": 'caCertificate',
        "client_certificate": 'clientCertificate',
        "client_key": 'clientKey',
        "kmip_protocol_version": 'kmipProtocolVersion'
    }

    def __init__(self,
                 ca_certificate=None,
                 client_certificate=None,
                 client_key=None,
                 kmip_protocol_version=None):
        """Constructor for the CryptsoftKmsUpdateParams class"""

        # Initialize members of the class
        self.ca_certificate = ca_certificate
        self.client_certificate = client_certificate
        self.client_key = client_key
        self.kmip_protocol_version = kmip_protocol_version

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
        ca_certificate = dictionary.get('caCertificate')
        client_certificate = dictionary.get('clientCertificate')
        client_key = dictionary.get('clientKey')
        kmip_protocol_version = dictionary.get('kmipProtocolVersion')

        # Return an object of this model
        return cls(ca_certificate,
                   client_certificate,
                   client_key,
                   kmip_protocol_version)

