# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class AwsCredentials(object):

    """Implementation of the 'AwsCredentials' model.

    Specifies the credentials to authenticate with AWS Cloud Platform.

    Attributes:
        access_key (string): Specifies Access key of the AWS account.
        amazon_resource_name (string): Specifies Amazon Resource Name (owner
            ID) of the IAM user, act as an unique identifier of as AWS
            entity.
        aws_type (AwsTypeEnum): Specifies the entity type such as 'kIAMUser'
            if the environment is kAWS. Specifies the type of an AWS source
            entity. 'kIAMUser' indicates a unique user within an AWS account.
            'kRegion' indicates a geographical region in the global
            infrastructure. 'kAvailabilityZone' indicates an availability zone
            within a region. 'kEC2Instance' indicates a Virtual Machine
            running in AWS environment. 'kVPC' indicates a virtual private
            cloud (VPC) network within AWS. 'kSubnet' indicates a subnet
            inside the VPC. 'kNetworkSecurityGroup' represents a network
            security group. 'kInstanceType' represents various machine types.
            'kKeyPair' represents a pair of public and private key used to
            login into a Virtual Machine.
        secret_access_key (string): Specifies Secret Access key of the AWS
            account.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "access_key":'accessKey',
        "amazon_resource_name":'amazonResourceName',
        "aws_type":'awsType',
        "secret_access_key":'secretAccessKey'
    }

    def __init__(self,
                 access_key=None,
                 amazon_resource_name=None,
                 aws_type=None,
                 secret_access_key=None):
        """Constructor for the AwsCredentials class"""

        # Initialize members of the class
        self.access_key = access_key
        self.amazon_resource_name = amazon_resource_name
        self.aws_type = aws_type
        self.secret_access_key = secret_access_key


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
        access_key = dictionary.get('accessKey')
        amazon_resource_name = dictionary.get('amazonResourceName')
        aws_type = dictionary.get('awsType')
        secret_access_key = dictionary.get('secretAccessKey')

        # Return an object of this model
        return cls(access_key,
                   amazon_resource_name,
                   aws_type,
                   secret_access_key)


