# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ElastifileCluster(object):

    """Implementation of the 'ElastifileCluster' model.

    Specifies information about a Elastifile Cluster.

    Attributes:
        enode_ip_address_vec (list of string): IP addresses of Elastifile
            nodes.
        load_balancer_vip (string): Specifies the load balancer VIP if
            present.
        name (string): Specifies name of a Elastifile Cluster
        uuid (string): Specifies the UUID of a Elastifile Cluster.
        version (string): Specifies the version of a Elastifile Cluster.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enode_ip_address_vec":'enodeIpAddressVec',
        "load_balancer_vip":'loadBalancerVip',
        "name":'name',
        "uuid":'uuid',
        "version":'version'
    }

    def __init__(self,
                 enode_ip_address_vec=None,
                 load_balancer_vip=None,
                 name=None,
                 uuid=None,
                 version=None):
        """Constructor for the ElastifileCluster class"""

        # Initialize members of the class
        self.enode_ip_address_vec = enode_ip_address_vec
        self.load_balancer_vip = load_balancer_vip
        self.name = name
        self.uuid = uuid
        self.version = version


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
        enode_ip_address_vec = dictionary.get('enodeIpAddressVec')
        load_balancer_vip = dictionary.get('loadBalancerVip')
        name = dictionary.get('name')
        uuid = dictionary.get('uuid')
        version = dictionary.get('version')

        # Return an object of this model
        return cls(enode_ip_address_vec,
                   load_balancer_vip,
                   name,
                   uuid,
                   version)


