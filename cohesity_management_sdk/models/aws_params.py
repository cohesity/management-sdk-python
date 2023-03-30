# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.custom_tag_params
import cohesity_management_sdk.models.rds_params


class AwsParams(object):

    """Implementation of the 'AwsParams' model.

    Specifies various resources when converting and deploying a VM to AWS.


    Attributes:

        custom_tag_list (list of CustomTagParams): Specifies the list of Custom
            Tag Parameters to be applied to resources created in AWS Cloudspin.
        instance_id (long|int): Specifies id of the AWS instance type in which
            to deploy the VM.
        network_security_group_ids (list of long|int): Specifies ids of the
            network security groups within above VPC.
        rds_params (RdsParams): Specifies Amazon RDS parameters.
        region (long|int): Specifies id of the AWS region in which to deploy
            the VM.
        subnet_id (long|int): Specifies id of the subnet within above VPC.
        virtual_private_cloud_id (long|int): Specifies id of the Virtual
            Private Cloud to chose for the instance type.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "custom_tag_list":'customTagList',
        "instance_id":'instanceId',
        "network_security_group_ids":'networkSecurityGroupIds',
        "rds_params":'rdsParams',
        "region":'region',
        "subnet_id":'subnetId',
        "virtual_private_cloud_id":'virtualPrivateCloudId',
    }
    def __init__(self,
                 custom_tag_list=None,
                 instance_id=None,
                 network_security_group_ids=None,
                 rds_params=None,
                 region=None,
                 subnet_id=None,
                 virtual_private_cloud_id=None,
            ):

        """Constructor for the AwsParams class"""

        # Initialize members of the class
        self.custom_tag_list = custom_tag_list
        self.instance_id = instance_id
        self.network_security_group_ids = network_security_group_ids
        self.rds_params = rds_params
        self.region = region
        self.subnet_id = subnet_id
        self.virtual_private_cloud_id = virtual_private_cloud_id

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
        custom_tag_list = None
        if dictionary.get('customTagList') != None:
            custom_tag_list = list()
            for structure in dictionary.get('customTagList'):
                custom_tag_list.append(cohesity_management_sdk.models.custom_tag_params.CustomTagParams.from_dictionary(structure))
        instance_id = dictionary.get('instanceId')
        network_security_group_ids = dictionary.get("networkSecurityGroupIds")
        rds_params = cohesity_management_sdk.models.rds_params.RdsParams.from_dictionary(dictionary.get('rdsParams')) if dictionary.get('rdsParams') else None
        region = dictionary.get('region')
        subnet_id = dictionary.get('subnetId')
        virtual_private_cloud_id = dictionary.get('virtualPrivateCloudId')

        # Return an object of this model
        return cls(
            custom_tag_list,
            instance_id,
            network_security_group_ids,
            rds_params,
            region,
            subnet_id,
            virtual_private_cloud_id
)