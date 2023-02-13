# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.aws_kms_update_params
import cohesity_management_sdk.models.cryptsoft_kms_update_params

class KmsUpdateRequestParameters(object):

    """Implementation of the 'KmsUpdateRequestParameters' model.

    Request to create a KMS with specified configuration.

    Attributes:
        aws_kms (AwsKmsUpdateParams): AWS KMS conifg.
        cryptsoft_kms (CryptsoftKmsUpdateParams): Cryptsoft KMS config.
        id (int): The Id of a KMS server.
        key_name (string): Specifies name of the key.
        server_name (string): Specifies the name given to the KMS Server.
        vault_id_list (list of long|int): Specifies the list of Vault Ids.
        view_box_id_list (list of long|int): Specifies the list of View Box
            Ids.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "aws_kms": 'awsKms',
        "cryptsoft_kms": 'cryptsoftKms',
        "id": 'id',
        "key_name":'keyName',
        "server_name": 'serverName',
        "vault_id_list":'vaultIdList',
        "view_box_id_list":'viewBoxIdList'
    }

    def __init__(self,
                 aws_kms=None,
                 cryptsoft_kms=None,
                 id=None,
                 key_name=None,
                 server_name=None,
                 vault_id_list=None,
                 view_box_id_list=None):
        """Constructor for the KmsUpdateRequestParameters class"""

        # Initialize members of the class
        self.aws_kms = aws_kms
        self.cryptsoft_kms = cryptsoft_kms
        self.id = id
        self.key_name = key_name
        self.server_name = server_name
        self.vault_id_list = vault_id_list
        self.view_box_id_list = view_box_id_list

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
        key_name = dictionary.get('keyName')
        server_name = dictionary.get('serverName')
        vault_id_list = dictionary.get('vaultIdList')
        view_box_id_list = dictionary.get('viewBoxIdList')

        # Return an object of this model
        return cls(aws_kms,
                   cryptsoft_kms,
                   id,
                   key_name,
                   server_name,
                   vault_id_list,
                   view_box_id_list)


