# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.aws_kms_update_params
import cohesity_management_sdk.models.cryptsoft_kms_update_params

class KmsUpdateRequestParameters(object):

    """Implementation of the 'KmsUpdateRequestParameters' model.

    Request to create a KMS with specified configuration.

    Attributes:
        aws_kms (AwsKmsUpdateParams): AWS KMS conifg.
        cryptsoft_kms (CryptsoftKmsUpdateParams): Cryptsoft KMS config.
        id (int): The Id of a KMS server.
        server_name (string): Specifies the name given to the KMS Server.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "aws_kms": 'awsKms',
        "cryptsoft_kms": 'cryptsoftKms',
        "id": 'id',
        "server_name": 'serverName'
    }

    def __init__(self,
                 aws_kms=None,
                 cryptsoft_kms=None,
                 id=None,
                 server_name=None):
        """Constructor for the KmsUpdateRequestParameters class"""

        # Initialize members of the class
        self.aws_kms = aws_kms
        self.cryptsoft_kms = cryptsoft_kms
        self.id = id
        self.server_name = server_name

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
        aws_kms = cohesity_management_sdk.models.aws_kms_update_params.AwsKmsUpdateParams.from_dictionary(dictionary.get('awsKms')) if dictionary.get('awsKms') else None
        cryptsoft_kms = cohesity_management_sdk.models.cryptsoft_kms_update_params.CryptsoftKmsUpdateParams.from_dictionary(dictionary.get('cryptsoftKms')) if dictionary.get('cryptsoftKms') else None
        id = dictionary.get('id')
        server_name = dictionary.get('serverName')

        # Return an object of this model
        return cls(aws_kms,
                   cryptsoft_kms,
                   id,
                   server_name)


