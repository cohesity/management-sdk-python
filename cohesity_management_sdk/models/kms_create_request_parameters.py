# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.aws_kms_configuration
import cohesity_management_sdk.models.cryptsoft_kms_configuration


class KmsCreateRequestParameters(object):

    """Implementation of the 'KmsCreateRequestParameters' model.

    TODO: type description here.


    Attributes:

        aws_kms (AwsKmsConfiguration): AWS KMS conifg.
        cryptsoft_kms (CryptsoftKmsConfiguration): Cryptsoft KMS config.
        id (long|int): The Id of a KMS server.
        key_name (string): Specifies name of the key.
        ownership_context (OwnershipContextEnum): Specifies the consumption
            model for the KMS Key. 'Local' indicates an internal KMS object.
            'FortKnox' indicates an FortKnox KMS object.
        server_name (string): Specifies the name given to the KMS Server.
        server_type (ServerTypeEnum): Specifies the type of key mangement
            system. 'kInternalKms' indicates an internal KMS object. 'kAwsKms'
            indicates an Aws KMS object. 'kCryptsoftKms' indicates a Cryptsoft
            KMS object.
        usage_type (UsageTypeEnum): Specifies the usage type of the kms config.
            kArchival indicates this is used for regular archival.
            kRpaasArchival indicates this is used for RPaaS only. 'kArchival'
            indicates an internal KMS object. 'kRpaasArchival' indicates an Aws
            KMS object.
        vault_id_list (list of long|int): Specifies the list of Vault Ids.
        view_box_id_list (list of long|int): Specifies the list of View Box
            Ids.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "aws_kms":'awsKms',
        "cryptsoft_kms":'cryptsoftKms',
        "id":'id',
        "key_name":'keyName',
        "ownership_context":'ownershipContext',
        "server_name":'serverName',
        "server_type":'serverType',
        "usage_type":'usageType',
        "vault_id_list":'vaultIdList',
        "view_box_id_list":'viewBoxIdList',
    }
    def __init__(self,
                 aws_kms=None,
                 cryptsoft_kms=None,
                 id=None,
                 key_name=None,
                 ownership_context=None,
                 server_name=None,
                 server_type=None,
                 usage_type=None,
                 vault_id_list=None,
                 view_box_id_list=None,
            ):

        """Constructor for the KmsCreateRequestParameters class"""

        # Initialize members of the class
        self.aws_kms = aws_kms
        self.cryptsoft_kms = cryptsoft_kms
        self.id = id
        self.key_name = key_name
        self.ownership_context = ownership_context
        self.server_name = server_name
        self.server_type = server_type
        self.usage_type = usage_type
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
        aws_kms = cohesity_management_sdk.models.aws_kms_configuration.AwsKmsConfiguration.from_dictionary(dictionary.get('awsKms')) if dictionary.get('awsKms') else None
        cryptsoft_kms = cohesity_management_sdk.models.cryptsoft_kms_configuration.CryptsoftKmsConfiguration.from_dictionary(dictionary.get('cryptsoftKms')) if dictionary.get('cryptsoftKms') else None
        id = dictionary.get('id')
        key_name = dictionary.get('keyName')
        ownership_context = dictionary.get('ownershipContext')
        server_name = dictionary.get('serverName')
        server_type = dictionary.get('serverType')
        usage_type = dictionary.get('usageType')
        vault_id_list = dictionary.get("vaultIdList")
        view_box_id_list = dictionary.get("viewBoxIdList")

        # Return an object of this model
        return cls(
            aws_kms,
            cryptsoft_kms,
            id,
            key_name,
            ownership_context,
            server_name,
            server_type,
            usage_type,
            vault_id_list,
            view_box_id_list
)