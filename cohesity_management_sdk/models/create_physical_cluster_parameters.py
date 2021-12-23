# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

import cohesity_management_sdk.models.encryption_configuration
import cohesity_management_sdk.models.ipmi_configuration
import cohesity_management_sdk.models.network_configuration
import cohesity_management_sdk.models.physical_node_configuration

class CreatePhysicalClusterParameters(object):

    """Implementation of the 'CreatePhysicalClusterParameters' model.

    Specifies the parameters needed for creation of a new Cluster.

    Attributes:
        cluster_destroy_hmac_key (string): Specifies HMAC secret key that will
            be used to validate OTP used for destroy request. This is b32 format
            of the HMAC key. This should only be set/modified during cluster
            creation.
        cluster_name (string): Specifies the name of the new Cluster.
        enable_cluster_destroy (bool): Specifies if cluster destroy op is
            enabled on this cluster.
            This should only be set/modified during cluster creation.
        encryption_config (EncryptionConfiguration): Specifies the parameters
            the user wants to use when configuring encryption for the new
            Cluster.
        ip_preference (int): Specifies IP preference.
        ipmi_config (IpmiConfiguration): Specifies the parameters for
            configuration of IPMI. This is only needed for physical clusters.
        metadata_fault_tolerance (int): Specifies the metadata fault
            tolerance.
        network_config (NetworkConfiguration): Specifies all of the parameters
            needed for network configuration of the new Cluster.
        node_configs (list of PhysicalNodeConfiguration): Specifies the
            configuration for the nodes in the new cluster.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cluster_destroy_hmac_key":'clusterDestroyHmacKey',
        "cluster_name":'clusterName',
        "enable_cluster_destroy":'enableClusterDestroy',
        "ip_preference":'ipPreference',
        "ipmi_config":'ipmiConfig',
        "network_config":'networkConfig',
        "node_configs":'nodeConfigs',
        "encryption_config":'encryptionConfig',
        "metadata_fault_tolerance":'metadataFaultTolerance'
    }

    def __init__(self,
                 cluster_destroy_hmac_key=None,
                 cluster_name=None,
                 enable_cluster_destroy=None,
                 ipmi_config=None,
                 network_config=None,
                 node_configs=None,
                 encryption_config=None,
                 metadata_fault_tolerance=None,
                 ip_preference=None):
        """Constructor for the CreatePhysicalClusterParameters class"""

        # Initialize members of the class
        self.cluster_destroy_hmac_key = cluster_destroy_hmac_key
        self.cluster_name = cluster_name
        self.enable_cluster_destroy = enable_cluster_destroy
        self.encryption_config = encryption_config
        self.ip_preference = ip_preference
        self.ipmi_config = ipmi_config
        self.metadata_fault_tolerance = metadata_fault_tolerance
        self.network_config = network_config
        self.node_configs = node_configs


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
        cluster_destroy_hmac_key = dictionary.get('clusterDestroyHmacKey')
        enable_cluster_destroy = dictionary.get('enableClusterDestroy')
        ipmi_config = cohesity_management_sdk.models.ipmi_configuration.IpmiConfiguration.from_dictionary(dictionary.get('ipmiConfig')) if dictionary.get('ipmiConfig') else None
        ip_preference = dictionary.get('ipPreference', None)
        network_config = cohesity_management_sdk.models.network_configuration.NetworkConfiguration.from_dictionary(dictionary.get('networkConfig')) if dictionary.get('networkConfig') else None
        node_configs = None
        if dictionary.get('nodeConfigs') != None:
            node_configs = list()
            for structure in dictionary.get('nodeConfigs'):
                node_configs.append(cohesity_management_sdk.models.physical_node_configuration.PhysicalNodeConfiguration.from_dictionary(structure))
        encryption_config = cohesity_management_sdk.models.encryption_configuration.EncryptionConfiguration.from_dictionary(dictionary.get('encryptionConfig')) if dictionary.get('encryptionConfig') else None
        metadata_fault_tolerance = dictionary.get('metadataFaultTolerance')

        # Return an object of this model
        return cls(cluster_destroy_hmac_key,
                   cluster_name,
                   enable_cluster_destroy,
                   ipmi_config,
                   network_config,
                   node_configs,
                   encryption_config,
                   metadata_fault_tolerance,
                   ip_preference)


