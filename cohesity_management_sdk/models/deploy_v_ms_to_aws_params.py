# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto

class DeployVMsToAWSParams(object):

    """Implementation of the 'DeployVMsToAWSParams' model.

    Contains AWS specific information needed to identify various resources
    when converting and deploying a VM to AWS.

    Attributes:
        instance_type (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        key_pair_name (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        network_security_groups (list of EntityProto): Names of the network
            security groups within the above VPC. At least one entry should be
            present.
        region (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        subnet (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        vpc (EntityProto): Specifies the attributes and the latest statistics
            about an entity.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "instance_type":'instanceType',
        "key_pair_name":'keyPairName',
        "network_security_groups":'networkSecurityGroups',
        "region":'region',
        "subnet":'subnet',
        "vpc":'vpc'
    }

    def __init__(self,
                 instance_type=None,
                 key_pair_name=None,
                 network_security_groups=None,
                 region=None,
                 subnet=None,
                 vpc=None):
        """Constructor for the DeployVMsToAWSParams class"""

        # Initialize members of the class
        self.instance_type = instance_type
        self.key_pair_name = key_pair_name
        self.network_security_groups = network_security_groups
        self.region = region
        self.subnet = subnet
        self.vpc = vpc


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
        instance_type = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('instanceType')) if dictionary.get('instanceType') else None
        key_pair_name = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('keyPairName')) if dictionary.get('keyPairName') else None
        network_security_groups = None
        if dictionary.get('networkSecurityGroups') != None:
            network_security_groups = list()
            for structure in dictionary.get('networkSecurityGroups'):
                network_security_groups.append(cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(structure))
        region = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('region')) if dictionary.get('region') else None
        subnet = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('subnet')) if dictionary.get('subnet') else None
        vpc = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('vpc')) if dictionary.get('vpc') else None

        # Return an object of this model
        return cls(instance_type,
                   key_pair_name,
                   network_security_groups,
                   region,
                   subnet,
                   vpc)


