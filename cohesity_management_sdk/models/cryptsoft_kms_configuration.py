# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class CryptsoftKmsConfiguration(object):

    """Implementation of the 'CryptsoftKmsConfiguration' model.

    Specifies the parameters for kmip KMS configuration.

    Attributes:
        ca_certificate (string): Specifies the CA certificate in PEM format.
        client_certificate (string): Specifies the client certificate.
            It is in PEM format.
        client_key (string): Specifies the client private key.
        kmip_protocol_version (string): Specifies protocol version used to
            communicate with the KMS.
        server_ip (string): Specifies the KMS IP address
        server_port (int): Specifies port on which the server is listening.
            Default port is 5696.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ca_certificate": 'caCertificate',
        "client_certificate": 'clientCertificate',
        "client_key": 'clientKey',
        "kmip_protocol_version": 'kmipProtocolVersion',
        "server_ip":'serverIp',
        "server_port":'serverPort'
    }

    def __init__(self,
                 ca_certificate=None,
                 client_certificate=None,
                 client_key=None,
                 kmip_protocol_version=None,
                 server_ip=None,
                 server_port=None):
        """Constructor for the CryptsoftKmsConfiguration class"""

        # Initialize members of the class
        self.ca_certificate = ca_certificate
        self.client_certificate = client_certificate
        self.client_key = client_key
        self.kmip_protocol_version = kmip_protocol_version
        self.server_ip = server_ip
        self.server_port = server_port

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
        server_ip = dictionary.get('serverIp')
        server_port = dictionary.get('serverPort')

        # Return an object of this model
        return cls(ca_certificate,
                   client_certificate,
                   client_key,
                   kmip_protocol_version,
                   server_ip,
                   server_port)


