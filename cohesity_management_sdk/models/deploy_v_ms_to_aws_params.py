# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.deploy_db_instances_to_rds_params

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
        proxy_vm_subnet (EntityProto): Name of the subnet within the above VPC
            which will be associated with the proxy vm.
        proxy_vm_vpc (EntityProto): Virtual Private Cloud (VPC) in which the
            proxy vm will be deployed.
        rds_params (DeployDBInstancesToRDSParams): Contains RDS specfic
            options that can be supplied while restoring the RDS DB instance.
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
        "proxy_vm_subnet":'proxyVmSubnet',
        "proxy_vm_vpc":'proxyVmVpc',
        "rds_params":'rdsParams',
        "region":'region',
        "subnet":'subnet',
        "vpc":'vpc'
    }

    def __init__(self,
                 instance_type=None,
                 key_pair_name=None,
                 network_security_groups=None,
                 proxy_vm_subnet=None,
                 proxy_vm_vpc=None,
                 rds_params=None,
                 region=None,
                 subnet=None,
                 vpc=None):
        """Constructor for the DeployVMsToAWSParams class"""

        # Initialize members of the class
        self.instance_type = instance_type
        self.key_pair_name = key_pair_name
        self.network_security_groups = network_security_groups
        self.proxy_vm_subnet = proxy_vm_subnet
        self.proxy_vm_vpc = proxy_vm_vpc
        self.rds_params = rds_params
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
        proxy_vm_subnet = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('proxyVmSubnet')) if dictionary.get('proxyVmSubnet') else None
        proxy_vm_vpc = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('proxyVmVpc')) if dictionary.get('proxyVmVpc') else None
        rds_params = cohesity_management_sdk.models.deploy_db_instances_to_rds_params.DeployDBInstancesToRDSParams.from_dictionary(dictionary.get('rdsParams')) if dictionary.get('rdsParams') else None
        region = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('region')) if dictionary.get('region') else None
        subnet = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('subnet')) if dictionary.get('subnet') else None
        vpc = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('vpc')) if dictionary.get('vpc') else None

        # Return an object of this model
        return cls(instance_type,
                   key_pair_name,
                   network_security_groups,
                   proxy_vm_subnet,
                   proxy_vm_vpc,
                   rds_params,
                   region,
                   subnet,
                   vpc)


