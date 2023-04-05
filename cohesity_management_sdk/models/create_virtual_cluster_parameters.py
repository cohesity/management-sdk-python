# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.encryption_configuration
import cohesity_management_sdk.models.network_configuration
import cohesity_management_sdk.models.virtual_node_configuration


class CreateVirtualClusterParameters(object):

    """Implementation of the 'CreateVirtualClusterParameters' model.

    Specifies the parameters needed for creation of a new Cluster.


    Attributes:

        cluster_name (string, required): Specifies the name of the new Cluster.
        encryption_config (EncryptionConfiguration): Specifies the encryption
            configuration parameters.
        ip_preference (int): Specifies IP preference.
        metadata_fault_tolerance (int): Specifies the metadata fault tolerance.
        network_config (NetworkConfiguration, required): Specifies the network
            configuration parameters.
        node_configs (list of VirtualNodeConfiguration, required): Specifies
            the configuration for the nodes in the new cluster.
        trust_domain (string): Specifies Trust Domain used for Service
            Identity.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "cluster_name":'clusterName',
        "encryption_config":'encryptionConfig',
        "ip_preference":'ipPreference',
        "metadata_fault_tolerance":'metadataFaultTolerance',
        "network_config":'networkConfig',
        "node_configs":'nodeConfigs',
        "trust_domain":'trustDomain',
    }
    def __init__(self,
                 cluster_name=None,
                 encryption_config=None,
                 ip_preference=None,
                 metadata_fault_tolerance=None,
                 network_config=None,
                 node_configs=None,
                 trust_domain=None,
            ):

        """Constructor for the CreateVirtualClusterParameters class"""

        # Initialize members of the class
        self.cluster_name = cluster_name
        self.encryption_config = encryption_config
        self.ip_preference = ip_preference
        self.metadata_fault_tolerance = metadata_fault_tolerance
        self.network_config = network_config
        self.node_configs = node_configs
        self.trust_domain = trust_domain

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
        encryption_config = cohesity_management_sdk.models.encryption_configuration.EncryptionConfiguration.from_dictionary(dictionary.get('encryptionConfig')) if dictionary.get('encryptionConfig') else None
        ip_preference = dictionary.get('ipPreference')
        metadata_fault_tolerance = dictionary.get('metadataFaultTolerance')
        network_config = cohesity_management_sdk.models.network_configuration.NetworkConfiguration.from_dictionary(dictionary.get('networkConfig')) if dictionary.get('networkConfig') else None
        node_configs = None
        if dictionary.get('nodeConfigs') != None:
            node_configs = list()
            for structure in dictionary.get('nodeConfigs'):
                node_configs.append(cohesity_management_sdk.models.virtual_node_configuration.VirtualNodeConfiguration.from_dictionary(structure))
        trust_domain = dictionary.get('trustDomain')

        # Return an object of this model
        return cls(
            cluster_name,
            encryption_config,
            ip_preference,
            metadata_fault_tolerance,
            network_config,
            node_configs,
            trust_domain
)