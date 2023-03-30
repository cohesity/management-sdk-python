# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.cluster_config_proto_subnet
import cohesity_management_sdk.models.alias_smb_config

class ViewAliasInfo(object):

    """Implementation of the 'ViewAliasInfo' model.

    View Alias Info is returned as part of list views.

    Attributes:
        alias_name (string): Alias name.
        client_subnet_whitelist (list of ClusterConfigProtoSubnet): List of
            external client subnet IPs that are allowed to access the share.
        smb_config (AliasSmbConfig): Message defining SMB config for IRIS. SMB
            config contains SMB encryption flags, SMB discoverable flag and
            Share level permissions.
        view_path (string): View path for the alias.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "alias_name":'aliasName',
        "client_subnet_whitelist":'clientSubnetWhitelist',
        "smb_config":'smbConfig',
        "view_path":'viewPath'
    }

    def __init__(self,
                 alias_name=None,
                 client_subnet_whitelist=None,
                 smb_config=None,
                 view_path=None):
        """Constructor for the ViewAliasInfo class"""

        # Initialize members of the class
        self.alias_name = alias_name
        self.client_subnet_whitelist = client_subnet_whitelist
        self.smb_config = smb_config
        self.view_path = view_path


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
        alias_name = dictionary.get('aliasName')
        client_subnet_whitelist = None
        if dictionary.get('clientSubnetWhitelist') != None:
            client_subnet_whitelist = list()
            for structure in dictionary.get('clientSubnetWhitelist'):
                client_subnet_whitelist.append(cohesity_management_sdk.models.cluster_config_proto_subnet.ClusterConfigProtoSubnet.from_dictionary(structure))
        smb_config = cohesity_management_sdk.models.alias_smb_config.AliasSmbConfig.from_dictionary(dictionary.get('smbConfig')) if dictionary.get('smbConfig') else None
        view_path = dictionary.get('viewPath')

        # Return an object of this model
        return cls(alias_name,
                   client_subnet_whitelist,
                   smb_config,
                   view_path)


