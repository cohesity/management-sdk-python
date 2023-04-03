# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.c_2_s_server_info


class AwsCredentials(object):

    """Implementation of the 'AwsCredentials' model.

    Specifies the credentials to authenticate with AWS Cloud Platform.


    Attributes:

        access_key (string): Specifies Access key of the AWS account.
        amazon_resource_name (string): Specifies Amazon Resource Name (owner
            ID) of the IAM user, act as an unique identifier of as AWS entity.
        auth_method (AuthMethodEnum): Specifies the authentication method to be
            used for API calls. Specifies the authentication method to be used
            for API calls. 'kUseIAMUser' indicates a user based authentication.
            'kUseIAMRole' indicates a role based authentication, used only for
            AWS CE. 'kUseHelios' indicates a Helios based authentication.
        aws_type (AwsTypeEnum): Specifies the entity type such as 'kIAMUser' if
            the environment is kAWS. Specifies the type of an AWS source
            entity. 'kIAMUser' indicates a unique user within an AWS account.
            'kRegion' indicates a geographical region in the global
            infrastructure. 'kAvailabilityZone' indicates an availability zone
            within a region. 'kEC2Instance' indicates a Virtual Machine running
            in AWS environment. 'kVPC' indicates a virtual private cloud (VPC)
            network within AWS. 'kSubnet' indicates a subnet inside the VPC.
            'kNetworkSecurityGroup' represents a network security group.
            'kInstanceType' represents various machine types. 'kKeyPair'
            represents a pair of public and private key used to login into a
            Virtual Machine. 'kTag' represents a tag attached to EC2 instance.
            'kRDSOptionGroup' represents a RDS option group for configuring
            database features. 'kRDSParameterGroup' represents a RDS parameter
            group. 'kRDSInstance' represents a RDS DB instance. 'kRDSSubnet'
            represents a RDS subnet. 'kRDSTag' represents a tag attached to RDS
            instance. 'kAuroraTag' represents a tag attached to an Aurora
            cluster. 'kAccount' represents an AWS account. 'kAuroraCluster'
            represents an Aurora cluster.
        c_2_s_server_info (C2SServerInfo): Specifies the C2S Access Portal
            (CAP) server info.
        iam_role_arn (string): Specifies the IAM role which will be used to
            access the security credentials required for API calls.
        secret_access_key (string): Specifies Secret Access key of the AWS
            account.
        subscription_type (SubscriptionTypeEnum): Specifies the subscription
            type of AWS such as 'kAWSCommercial' or 'kAWSGovCloud'. Specifies
            the subscription type of an AWS source entity. 'kAWSCommercial'
            indicates a standard AWS subscription. 'kAWSGovCloud' indicates a
            govt AWS subscription.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "access_key":'accessKey',
        "amazon_resource_name":'amazonResourceName',
        "auth_method":'authMethod',
        "aws_type":'awsType',
        "c_2_s_server_info":'c2sServerInfo',
        "iam_role_arn":'iamRoleArn',
        "secret_access_key":'secretAccessKey',
        "subscription_type":'subscriptionType',
    }
    def __init__(self,
                 access_key=None,
                 amazon_resource_name=None,
                 auth_method=None,
                 aws_type=None,
                 c_2_s_server_info=None,
                 iam_role_arn=None,
                 secret_access_key=None,
                 subscription_type=None,
            ):

        """Constructor for the AwsCredentials class"""

        # Initialize members of the class
        self.access_key = access_key
        self.amazon_resource_name = amazon_resource_name
        self.auth_method = auth_method
        self.aws_type = aws_type
        self.c_2_s_server_info = c_2_s_server_info
        self.iam_role_arn = iam_role_arn
        self.secret_access_key = secret_access_key
        self.subscription_type = subscription_type

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
        auth_method = dictionary.get('authMethod')
        aws_type = dictionary.get('awsType')
        c_2_s_server_info = cohesity_management_sdk.models.c_2_s_server_info.C2SServerInfo.from_dictionary(dictionary.get('c2sServerInfo')) if dictionary.get('c2sServerInfo') else None
        iam_role_arn = dictionary.get('iamRoleArn')
        secret_access_key = dictionary.get('secretAccessKey')
        subscription_type = dictionary.get('subscriptionType')

        # Return an object of this model
        return cls(
            access_key,
            amazon_resource_name,
            auth_method,
            aws_type,
            c_2_s_server_info,
            iam_role_arn,
            secret_access_key,
            subscription_type
)