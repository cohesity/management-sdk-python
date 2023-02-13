# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.nas_mount_credential_params
import cohesity_management_sdk.models.network_pool_config

class ZoneConfig(object):

    """Implementation of the 'ZoneConfig' model.

    Specifies the access zone config of the Isilon Access Zone.

    Attributes:
        dynamic_network_pool_config (NetworkPoolConfig): Specifies the Dynamic
            network pool configuration for the Access Zone. Dynamic pool is
            used for stateless protocols, e.g. NFSv3.
        groupnet (string): Specifies the name of the Access Zone's groupnet.
        name (string): Specifies the name of the Access Zone.
        smb_credentials (NasMountCredentialParams): SMB credentials for the
            Access Zone.
        static_network_pool_config (NetworkPoolConfig): Specifies the Static
            network pool configuration for the Access Zone. Static pool is
            used for stateful protocols: e.g. SMB, NFSv4, and for stateless
            protocols e.g. NFSv3 if dynamic pool below is not set.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dynamic_network_pool_config": 'dynamicNetworkPoolConfig',
        "groupnet": 'groupnet',
        "name": 'name',
        "smb_credentials": 'smbCredentials',
        "static_network_pool_config":'staticNetworkPoolConfig'
    }

    def __init__(self,
                 dynamic_network_pool_config=None,
                 groupnet=None,
                 name=None,
                 smb_credentials=None,
                 static_network_pool_config=None):
        """Constructor for the ZoneConfig class"""

        # Initialize members of the class
        self.dynamic_network_pool_config = dynamic_network_pool_config
        self.groupnet = groupnet
        self.name = name
        self.smb_credentials = smb_credentials
        self.static_network_pool_config = static_network_pool_config

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
        dynamic_network_pool_config = cohesity_management_sdk.models.network_pool_config.NetworkPoolConfig.from_dictionary(dictionary.get('dynamicNetworkPoolConfig')) if dictionary.get('dynamicNetworkPoolConfig') else None
        groupnet = dictionary.get('groupnet')
        name = dictionary.get('name')
        smb_credentials = cohesity_management_sdk.models.nas_mount_credential_params.NasMountCredentialParams.from_dictionary(dictionary.get('smbCredentials')) if dictionary.get('smbCredentials') else None
        static_network_pool_config = cohesity_management_sdk.models.network_pool_config.NetworkPoolConfig.from_dictionary(dictionary.get('staticNetworkPoolConfig')) if dictionary.get('staticNetworkPoolConfig') else None

        # Return an object of this model
        return cls(dynamic_network_pool_config,
                   groupnet,
                   name,
                   smb_credentials,
                   static_network_pool_config)


