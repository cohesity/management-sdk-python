# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

import cohesity_management_sdk.models.aws_kms_configuration
import cohesity_management_sdk.models.cryptsoft_kms_config_response

class KmsConfigurationResponse(object):

    """Implementation of the 'KmsConfigurationResponse' model.

    Specifies response parameters to a KMS request.

    Attributes:
        aws_kms (AwsKmsConfiguration): AWS KMS conifg response.
        connection_status (bool): Specifies if connection to this KMS exists.
        cryptsoft_kms (CryptsoftKmsConfigResponse): Specifies the config
            response for cryptsoftKMS.
        id (int): The Id of a KMS server.
        key_name (string): Specifies name of the key.
        removal_state (RemovalStateNodeEnum):  Specifies the state of the Kms
            Server.
            'kDontRemove' means the state of object is functional and
            it is not being removed.
            'kMarkedForRemoval' means the object is being removed.
            'kOkToRemove' means the object has been removed on the Cohesity
            Cluster and if the object is physical, it can be removed from the
            Cohesity Cluster.
        server_name (string): Specifies the name given to the KMS Server.
        server_type (ServerTypeEnum): Specifies the type of key mangement
            system.
            'kInternalKms' indicates an internal KMS object.
            'kAwsKms' indicates an Aws KMS object.
            'kCryptsoftKms' indicates a Cryptsoft KMS object.
        vault_id_list (list of long|int): Specifies the list of Vault Ids.
        view_box_id_list (list of long|int): Specifies the list of View Box Ids.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "aws_kms":'awsKms',
        "connection_status":'connectionStatus',
        "cryptsoft_kms":'cryptsoftKms',
        "id":'id',
        "key_name":'keyName',
        "removal_state":'removalState',
        "server_name":'serverName',
        "server_type":'serverType',
        "vault_id_list":'vaultIdList',
        "view_box_id_list":'viewBoxIdList'
    }

    def __init__(self,
                 aws_kms=None,
                 connection_status=None,
                 cryptsoft_kms=None,
                 id=None,
                 key_name=None,
                 removal_state=None,
                 server_name=None,
                 server_type=None,
                 vault_id_list=None,
                 view_box_id_list=None):
        """Constructor for the KmsConfigurationResponse class"""

        # Initialize members of the class
        self.aws_kms = aws_kms
        self.connection_status = connection_status
        self.cryptsoft_kms = cryptsoft_kms
        self.id = id
        self.key_name = key_name
        self.removal_state = removal_state
        self.server_name = server_name
        self.server_type = server_type
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
        connection_status = dictionary.get('connectionStatus')
        cryptsoft_kms =  cohesity_management_sdk.models.cryptsoft_kms_config_response.CryptsoftKmsConfigResponse.from_dictionary(dictionary.get('cryptsoftKms')) if dictionary.get('cryptsoftKms') else None
        id = dictionary.get('id')
        key_name = dictionary.get('keyName')
        removal_state = dictionary.get('removalState')
        server_name = dictionary.get('serverName')
        server_type = dictionary.get('serverType')
        vault_id_list = dictionary.get('vaultIdList')
        view_box_id_list = dict.get('viewBoxIdList')

        # Return an object of this model
        return cls(aws_kms,
                   connection_status,
                   cryptsoft_kms,
                   id,
                   key_name,
                   removal_state,
                   server_name,
                   server_type,
                   vault_id_list,
                   view_box_id_list)


