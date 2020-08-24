# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.aws_kms_configuration
import cohesity_management_sdk.models.cryptsoft_kms_configuration

class KmsCreateRequestParameters(object):

    """Implementation of the 'KmsCreateRequestParameters' model.

    Request to create a KMS with specified configuration.

    Attributes:
        aws_kms (AwsKmsConfiguration): AWS KMS conifg.
        cryptsoft_kms (CryptsoftKmsConfiguration): Cryptsoft KMS config.
        id (int): The Id of a KMS server.
        server_name (string): Specifies the name given to the KMS Server.
        server_type (ServerTypeKmsCreateRequestParametersEnum): Specifies the
            type of key mangement system.
            'kInternalKms' indicates an internal KMS object.
            'kAwsKms' indicates an Aws KMS object.
            'kCryptsoftKms' indicates a Cryptsoft KMS object.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "aws_kms": 'awsKms',
        "cryptsoft_kms": 'cryptsoftKms',
        "id": 'id',
        "server_name": 'serverName',
        "server_type":'serverType'
    }

    def __init__(self,
                 aws_kms=None,
                 cryptsoft_kms=None,
                 id=None,
                 server_name=None,
                 server_type=None):
        """Constructor for the KmsCreateRequestParameters class"""

        # Initialize members of the class
        self.aws_kms = aws_kms
        self.cryptsoft_kms = cryptsoft_kms
        self.id = id
        self.server_name = server_name
        self.server_type = server_type

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
        aws_kms = cohesity_management_sdk.models.aws_kms_configuration.AwsKmsConfiguration.from_dictionary(dictionary.get('awsKms')) if dictionary.get('awsKms') else None
        cryptsoft_kms = cohesity_management_sdk.models.cryptsoft_kms_configuration.CryptsoftKmsConfiguration.from_dictionary(dictionary.get('cryptsoftKms')) if dictionary.get('cryptsoftKms') else None
        id = dictionary.get('id')
        server_name = dictionary.get('serverName')
        server_type = dictionary.get('serverType')

        # Return an object of this model
        return cls(aws_kms,
                   cryptsoft_kms,
                   id,
                   server_name,
                   server_type)


