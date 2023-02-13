# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.cluster_config_proto_vault_cloud_properties

class ClusterConfigProto_Vault_CloudTierType(object):

    """Implementation of the 'ClusterConfigProto_Vault_CloudTierType' model.

    Proto representing a cloud tier type.

    Attributes:
        cloud_properties (ClusterConfigProto_Vault_CloudProperties): Field
            represeting cloud properties, which contains different properties
            (tiers/classes) supported by different cloud providers. In case of
            Oracle cloud, the 'tenant' property of OracleProperties message
            would not be populated for this use case.
        cloud_type (int): Field representing the cloud type.
            Currently tiers are supported for kAzure, kGoogle, kAmazon, kOracle.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cloud_properties": 'cloudProperties',
        "cloud_type": 'cloudType'
    }

    def __init__(self,
                 cloud_properties=None,
                 cloud_type=None):
        """Constructor for the ClusterConfigProto_Vault_CloudTierType class"""

        # Initialize members of the class
        self.cloud_properties = cloud_properties
        self.cloud_type = cloud_type


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
        cloud_properties = cohesity_management_sdk.models.cluster_config_proto_vault_cloud_properties.ClusterConfigProto_Vault_CloudProperties.from_dictionary(dictionary.get('cloudProperties')) if dictionary.get('cloudProperties') else None
        cloud_type = dictionary.get('cloudType')

        # Return an object of this model
        return cls(cloud_properties,
                   cloud_type)


