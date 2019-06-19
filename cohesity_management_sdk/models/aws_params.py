# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.


class AwsParams(object):

    """Implementation of the 'AwsParams' model.

    Specifies various resources when converting and deploying a VM to AWS.

    Attributes:
        instance_id (long|int): Specfies id of the AWS instance type in which
            to deploy the VM.
        network_security_group_ids (list of long|int): Specifies ids of the
            netwrok security groups within above VPC.
        region (long|int): Specifies id of the AWS region in which to deploy
            the VM.
        subnet_id (long|int): Specifies id of the subnet within above VPC.
        virtual_private_cloud_id (long|int): Specifies id of the Virtual
            Private Cloud to chose for the instance type.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "instance_id":'instanceId',
        "network_security_group_ids":'networkSecurityGroupIds',
        "region":'region',
        "subnet_id":'subnetId',
        "virtual_private_cloud_id":'virtualPrivateCloudId'
    }

    def __init__(self,
                 instance_id=None,
                 network_security_group_ids=None,
                 region=None,
                 subnet_id=None,
                 virtual_private_cloud_id=None):
        """Constructor for the AwsParams class"""

        # Initialize members of the class
        self.instance_id = instance_id
        self.network_security_group_ids = network_security_group_ids
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
        instance_id = dictionary.get('instanceId')
        network_security_group_ids = dictionary.get('networkSecurityGroupIds')
        region = dictionary.get('region')
        subnet_id = dictionary.get('subnetId')
        virtual_private_cloud_id = dictionary.get('virtualPrivateCloudId')

        # Return an object of this model
        return cls(instance_id,
                   network_security_group_ids,
                   region,
                   subnet_id,
                   virtual_private_cloud_id)


