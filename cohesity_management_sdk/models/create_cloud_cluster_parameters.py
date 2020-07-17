# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.encryption_configuration
import cohesity_management_sdk.models.cloud_network_configuration

class CreateCloudClusterParameters(object):

    """Implementation of the 'CreateCloudClusterParameters' model.

    Specifies the parameters needed for creation of a new Cluster.

    Attributes:
        cluster_name (string): Specifies the name of the new Cluster.
        encryption_config (EncryptionConfiguration): Specifies the parameters
            the user wants to use when configuring encryption for the new
            Cluster.
        ip_preference (int): Specifies IP preference.
        metadata_fault_tolerance (int): Specifies the metadata fault
            tolerance.
        network_config (CloudNetworkConfiguration): Specifies all of the
            parameters needed for network configuration of the new Cloud
            Cluster.
        node_ips (list of string): Specifies the configuration for the nodes
            in the new cluster.


    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cluster_name":'clusterName',
        "ip_preference":'ipPreference',
        "network_config":'networkConfig',
        "node_ips":'nodeIps',
        "encryption_config":'encryptionConfig',
        "metadata_fault_tolerance":'metadataFaultTolerance'
    }

    def __init__(self,
                 cluster_name=None,
                 network_config=None,
                 node_ips=None,
                 encryption_config=None,
                 metadata_fault_tolerance=None,
                 ip_preference=None):
        """Constructor for the CreateCloudClusterParameters class"""

        # Initialize members of the class
        self.cluster_name = cluster_name
        self.ip_preference = ip_preference
        self.encryption_config = encryption_config
        self.metadata_fault_tolerance = metadata_fault_tolerance
        self.network_config = network_config
        self.node_ips = node_ips


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
        cluster_name = dictionary.get('clusterName')
        ip_preference = dictionary.get('ipPreference', None)
        network_config = cohesity_management_sdk.models.cloud_network_configuration.CloudNetworkConfiguration.from_dictionary(dictionary.get('networkConfig')) if dictionary.get('networkConfig') else None
        node_ips = dictionary.get('nodeIps')
        encryption_config = cohesity_management_sdk.models.encryption_configuration.EncryptionConfiguration.from_dictionary(dictionary.get('encryptionConfig')) if dictionary.get('encryptionConfig') else None
        metadata_fault_tolerance = dictionary.get('metadataFaultTolerance')

        # Return an object of this model
        return cls(cluster_name,
                   network_config,
                   node_ips,
                   encryption_config,
                   metadata_fault_tolerance,
                   ip_preference)


