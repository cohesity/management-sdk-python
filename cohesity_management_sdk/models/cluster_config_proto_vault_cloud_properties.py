# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.cluster_config_proto_vault_cloud_properties_amazon_properties
import cohesity_management_sdk.models.cluster_config_proto_vault_cloud_properties_azure_properties
import cohesity_management_sdk.models.cluster_config_proto_vault_cloud_properties_google_properties
import cohesity_management_sdk.models.cluster_config_proto_vault_cloud_properties_oracle_properties

class ClusterConfigProto_Vault_CloudProperties(object):

    """Implementation of the 'ClusterConfigProto_Vault_CloudProperties' model.

    The following represents the cloud properties proto which handles
    different properties supported by different cloud providers.

    Attributes:
        amazon_properties (
            ClusterConfigProto_Vault_CloudProperties_AmazonProperties):
            TODO: Type description here.
        azure_properties (
            ClusterConfigProto_Vault_CloudProperties_AzureProperties):
            TODO: Type description here.
        google_properties (ClusterConfigProto_Vault_CloudProperties_GoogleProperties):
            TODO: Type description here.
        oracle_properties (ClusterConfigProto_Vault_CloudProperties_OracleProperties):
            TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amazon_properties":'amazonProperties',
        "azure_properties":'azureProperties',
        "google_properties":'googleProperties',
        "oracle_properties":'oracleProperties'
    }

    def __init__(self,
                 amazon_properties=None,
                 azure_properties=None,
                 google_properties=None,
                 oracle_properties=None):
        """Constructor for the ClusterConfigProto_Vault_CloudProperties class"""

        # Initialize members of the class
        self.amazon_properties = amazon_properties
        self.azure_properties = azure_properties
        self.google_properties = google_properties
        self.oracle_properties = oracle_properties


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
        amazon_properties = cohesity_management_sdk.models.cluster_config_proto_vault_cloud_properties_amazon_properties.ClusterConfigProto_Vault_CloudProperties_AmazonProperties.from_dictionary(dictionary.get('amazonProperties')) if dictionary.get('amazonProperties') else None
        azure_properties = cohesity_management_sdk.models.cluster_config_proto_vault_cloud_properties_azure_properties.ClusterConfigProto_Vault_CloudProperties_AzureProperties.from_dictionary(dictionary.get('azureProperties')) if dictionary.get('azureProperties') else None
        google_properties = cohesity_management_sdk.models.cluster_config_proto_vault_cloud_properties_google_properties.ClusterConfigProto_Vault_CloudProperties_GoogleProperties.from_dictionary(dictionary.get('googleProperties')) if dictionary.get('googleProperties') else None
        oracle_properties = cohesity_management_sdk.models.cluster_config_proto_vault_cloud_properties_oracle_properties.ClusterConfigProto_Vault_CloudProperties_OracleProperties.from_dictionary(dictionary.get('oracleProperties')) if dictionary.get('oracleProperties') else None

        # Return an object of this model
        return cls(amazon_properties,
                   azure_properties,
                   google_properties,
                   oracle_properties)


