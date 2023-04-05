# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.encryption_configuration
import cohesity_management_sdk.models.ipmi_configuration
import cohesity_management_sdk.models.network_configuration
import cohesity_management_sdk.models.physical_node_configuration


class CreatePhysicalClusterParameters(object):

    """Implementation of the 'CreatePhysicalClusterParameters' model.

    Specifies the parameters needed for creation of a new Cluster.


    Attributes:

        allow_api_based_fetch (bool): Specifies if API based GET should be
            enabled for cluster destroy params.
        cluster_destroy_hmac_key (string): Specifies HMAC secret key that will
            be used to validate OTP used for destroy request. This is b32
            format of the HMAC key. This should only be set/modified during
            cluster creation.
        cluster_name (string, required): Specifies the name of the new Cluster.
        enable_cluster_destroy (bool): Specifies if cluster destroy op is
            enabled on this cluster. This should only be set/modified during
            cluster creation.
        encryption_config (EncryptionConfiguration): Specifies the encryption
            configuration parameters.
        ip_preference (int): Specifies IP preference.
        ipmi_config (IpmiConfiguration, required): Specifies the IPMI
            configuration parameters.
        metadata_fault_tolerance (int): Specifies the metadata fault tolerance.
        network_config (NetworkConfiguration, required): Specifies the network
            configuration parameters.
        node_configs (list of PhysicalNodeConfiguration, required): Specifies
            the configuration for the nodes in the new cluster.
        trust_domain (string): Specifies Trust Domain used for Service
            Identity.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "allow_api_based_fetch":'allowApiBasedFetch',
        "cluster_destroy_hmac_key":'clusterDestroyHmacKey',
        "cluster_name":'clusterName',
        "enable_cluster_destroy":'enableClusterDestroy',
        "encryption_config":'encryptionConfig',
        "ip_preference":'ipPreference',
        "ipmi_config":'ipmiConfig',
        "metadata_fault_tolerance":'metadataFaultTolerance',
        "network_config":'networkConfig',
        "node_configs":'nodeConfigs',
        "trust_domain":'trustDomain',
    }
    def __init__(self,
                 allow_api_based_fetch=None,
                 cluster_destroy_hmac_key=None,
                 cluster_name=None,
                 enable_cluster_destroy=None,
                 encryption_config=None,
                 ip_preference=None,
                 ipmi_config=None,
                 metadata_fault_tolerance=None,
                 network_config=None,
                 node_configs=None,
                 trust_domain=None,
            ):

        """Constructor for the CreatePhysicalClusterParameters class"""

        # Initialize members of the class
        self.allow_api_based_fetch = allow_api_based_fetch
        self.cluster_destroy_hmac_key = cluster_destroy_hmac_key
        self.cluster_name = cluster_name
        self.enable_cluster_destroy = enable_cluster_destroy
        self.encryption_config = encryption_config
        self.ip_preference = ip_preference
        self.ipmi_config = ipmi_config
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
        allow_api_based_fetch = dictionary.get('allowApiBasedFetch')
        cluster_destroy_hmac_key = dictionary.get('clusterDestroyHmacKey')
        cluster_name = dictionary.get('clusterName')
        enable_cluster_destroy = dictionary.get('enableClusterDestroy')
        encryption_config = cohesity_management_sdk.models.encryption_configuration.EncryptionConfiguration.from_dictionary(dictionary.get('encryptionConfig')) if dictionary.get('encryptionConfig') else None
        ip_preference = dictionary.get('ipPreference')
        ipmi_config = cohesity_management_sdk.models.ipmi_configuration.IpmiConfiguration.from_dictionary(dictionary.get('ipmiConfig')) if dictionary.get('ipmiConfig') else None
        metadata_fault_tolerance = dictionary.get('metadataFaultTolerance')
        network_config = cohesity_management_sdk.models.network_configuration.NetworkConfiguration.from_dictionary(dictionary.get('networkConfig')) if dictionary.get('networkConfig') else None
        node_configs = None
        if dictionary.get('nodeConfigs') != None:
            node_configs = list()
            for structure in dictionary.get('nodeConfigs'):
                node_configs.append(cohesity_management_sdk.models.physical_node_configuration.PhysicalNodeConfiguration.from_dictionary(structure))
        trust_domain = dictionary.get('trustDomain')

        # Return an object of this model
        return cls(
            allow_api_based_fetch,
            cluster_destroy_hmac_key,
            cluster_name,
            enable_cluster_destroy,
            encryption_config,
            ip_preference,
            ipmi_config,
            metadata_fault_tolerance,
            network_config,
            node_configs,
            trust_domain
)