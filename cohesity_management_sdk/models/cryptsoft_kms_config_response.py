# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class CryptsoftKmsConfigResponse(object):

    """Implementation of the 'CryptsoftKmsConfigResponse' model.

    CryptsoftKmsConfigResponse specifies response parameters for cryptsoftKMS.

    Attributes:
        client_certificate_expiry_date (int): Specifies expiry date of client
            certificate.
        kmip_protocol_version (string): Specifies protocol version used to
            communicate with the KMS.
        server_ip (string): Specifies the KMS IP address.
        server_port (int): Specifies port on which the server is listening.
            Default port is 5696.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "client_certificate_expiry_date":'clientCertificateExpiryDate',
        "kmip_protocol_version":'kmipProtocolVersion',
        "server_ip":'serverIp',
        "server_port":'serverPort'
    }

    def __init__(self,
                 client_certificate_expiry_date=None,
                 kmip_protocol_version=None,
                 server_ip=None,
                 server_port=None):
        """Constructor for the CryptsoftKmsConfigResponse class"""

        # Initialize members of the class
        self.client_certificate_expiry_date = client_certificate_expiry_date
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
        client_certificate_expiry_date = dictionary.get('clientCertificateExpiryDate')
        kmip_protocol_version = dictionary.get('kmipProtocolVersion')
        server_ip = dictionary.get('serverIp')
        server_port = dictionary.get('serverPort')

        # Return an object of this model
        return cls(client_certificate_expiry_date,
                   kmip_protocol_version,
                   server_ip,
                   server_port)


