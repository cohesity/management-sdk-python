# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.cloud_network_configuration
import cohesity_management_sdk.models.encryption_configuration


class CreateCloudClusterParameters(object):

    """Implementation of the 'CreateCloudClusterParameters' model.

    Specifies the parameters needed for creation of a new Cluster.


    Attributes:

        cluster_name (string, required): Specifies the name of the new Cluster.
        cluster_size (ClusterSizeEnum): Specifies the size of the cluster. It
            is set as Large by default if the parameter is not specified.
        encryption_config (EncryptionConfiguration): Specifies the encryption
            configuration parameters.
        ip_preference (int): Specifies IP preference.
        metadata_fault_tolerance (int): Specifies the metadata fault tolerance.
        network_config (CloudNetworkConfiguration, required): Specifies the
            network configuration parameters.
        node_ips (list of string, required): Specifies the configuration for
            the nodes in the new cluster.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "cluster_name":'clusterName',
        "cluster_size":'clusterSize',
        "encryption_config":'encryptionConfig',
        "ip_preference":'ipPreference',
        "metadata_fault_tolerance":'metadataFaultTolerance',
        "network_config":'networkConfig',
        "node_ips":'nodeIps',
    }
    def __init__(self,
                 cluster_name=None,
                 cluster_size=None,
                 encryption_config=None,
                 ip_preference=None,
                 metadata_fault_tolerance=None,
                 network_config=None,
                 node_ips=None,
            ):

        """Constructor for the CreateCloudClusterParameters class"""

        # Initialize members of the class
        self.cluster_name = cluster_name
        self.cluster_size = cluster_size
        self.encryption_config = encryption_config
        self.ip_preference = ip_preference
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
        cluster_size = dictionary.get('clusterSize')
        encryption_config = cohesity_management_sdk.models.encryption_configuration.EncryptionConfiguration.from_dictionary(dictionary.get('encryptionConfig')) if dictionary.get('encryptionConfig') else None
        ip_preference = dictionary.get('ipPreference')
        metadata_fault_tolerance = dictionary.get('metadataFaultTolerance')
        network_config = cohesity_management_sdk.models.cloud_network_configuration.CloudNetworkConfiguration.from_dictionary(dictionary.get('networkConfig')) if dictionary.get('networkConfig') else None
        node_ips = dictionary.get("nodeIps")

        # Return an object of this model
        return cls(
            cluster_name,
            cluster_size,
            encryption_config,
            ip_preference,
            metadata_fault_tolerance,
            network_config,
            node_ips
)