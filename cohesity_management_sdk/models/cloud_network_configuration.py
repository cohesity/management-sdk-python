# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class CloudNetworkConfiguration(object):

    """Implementation of the 'CloudNetworkConfiguration' model.

    Specifies all of the parameters needed for network configuration of
    the new Cloud Cluster.

    Attributes:
        cluster_gateway (string): Specifies the default gateway IP address (or
            addresses) for the Cluster network.
        cluster_subnet_mask (string): Specifies the subnet mask (or masks) of
            the Cluster network.
        dns_servers (list of string): Specifies the list of DNS Servers this
            cluster should be configured with.
        domain_names (list of string): Specifies the list of domain names this
            cluster should be configured with.
        ntp_servers (list of string): Specifies the list of NTP Servers this
            cluster should be configured with.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cluster_gateway":'clusterGateway',
        "cluster_subnet_mask":'clusterSubnetMask',
        "dns_servers":'dnsServers',
        "domain_names":'domainNames',
        "ntp_servers":'ntpServers'
    }

    def __init__(self,
                 cluster_gateway=None,
                 cluster_subnet_mask=None,
                 dns_servers=None,
                 domain_names=None,
                 ntp_servers=None):
        """Constructor for the CloudNetworkConfiguration class"""

        # Initialize members of the class
        self.cluster_gateway = cluster_gateway
        self.cluster_subnet_mask = cluster_subnet_mask
        self.dns_servers = dns_servers
        self.domain_names = domain_names
        self.ntp_servers = ntp_servers


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
        cluster_gateway = dictionary.get('clusterGateway')
        cluster_subnet_mask = dictionary.get('clusterSubnetMask')
        dns_servers = dictionary.get('dnsServers')
        domain_names = dictionary.get('domainNames')
        ntp_servers = dictionary.get('ntpServers')

        # Return an object of this model
        return cls(cluster_gateway,
                   cluster_subnet_mask,
                   dns_servers,
                   domain_names,
                   ntp_servers)


