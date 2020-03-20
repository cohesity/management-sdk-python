# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.tag_attribute

class AwsProtectionSource(object):

    """Implementation of the 'AwsProtectionSource' model.

    Specifies a Protection Source in AWS environment.

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
        host_type (HostTypeEnum): Specifies the OS type of the Protection
            Source of type 'kVirtualMachine' such as 'kWindows' or 'kLinux'.
            overrideDescription: true 'kLinux' indicates the Linux operating
            system. 'kWindows' indicates the Microsoft Windows operating
            system. 'kAix' indicates the IBM AIX operating system. 'kSolaris'
            indicates the Oracle Solaris operating system.
        ip_addresses (string): Specifies the IP address of the entity of type
            'kVirtualMachine'.
        name (string): Specifies the name of the Object set by the Cloud
            Provider. If the provider did not set a name for the object, this
            field is not set.
        owner_id (string): Specifies the owner id of the resource in AWS
            environment. With type, name and ownerId gives a globally unique
            identity to the AWS entity.
        physical_source_id (long|int): Specifies the Protection Source id of
            the registered Physical Host. If the cloud entity is protected
            using a Physical Agent, it must be registered as a physical host.
        region_id (string): Specifies the region Id of the entity if the
            entity is an EC2 instance.
        resource_id (string): Specifies the unique Id of the resource given by
            the cloud provider.
        restore_task_id (long|int): Specifies the id of the "convert and
            deploy" restore task that created the entity in the cloud.  It is
            required to support the DR-to-cloud usecase where we replicate an
            on-prem entity to a cluster running in cloud, bring it up using
            "convert and deploy" mechanism, protect it using a cloud job that
            uses physical adapter, and convert it back to the on-prem format
            before replication.  Before replicating, we need to update the
            backup task state of the backed up entity using the on-prem entity
            and on-prem entity's parent. The id is used to lookup the restore
            entity that contains details about the on-prem entity.  It is set
            at the time of refreshing the cloud entity hierarchy if all the
            following conditions are met: Name of the current entity matches
            with name of any cloud entity deployed using the "convert and
            deploy" restore task. Restore entity associated with the above
            matched cloud entity has 'failed_over' flag set to true in its
            cloud extension.
        secret_access_key (string): Specifies Secret Access key of the AWS
            account.
        tag_attributes (list of TagAttribute): Specifies the list of AWS tag
            attributes.
        mtype (TypeAwsProtectionSourceEnum): Specifies the type of an AWS
            Protection Source Object such as 'kStorageContainer',
            'kVirtualMachine', 'kVirtualNetwork', etc. Specifies the type of
            an AWS source entity. 'kIAMUser' indicates a unique user within an
            AWS account. 'kRegion' indicates a geographical region in the
            global infrastructure. 'kAvailabilityZone' indicates an
            availability zone within a region. 'kEC2Instance' indicates a
            Virtual Machine running in AWS environment. 'kVPC' indicates a
            virtual private cloud (VPC) network within AWS. 'kSubnet'
            indicates a subnet inside the VPC. 'kNetworkSecurityGroup'
            represents a network security group. 'kInstanceType' represents
            various machine types. 'kKeyPair' represents a pair of public and
            private key used to login into a Virtual Machine.
        user_account_id (string): Specifies the account id derived from the
            ARN of the user.
        user_resource_name (string): Specifies the Amazon Resource Name (ARN)
            of the user.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "access_key":'accessKey',
        "amazon_resource_name":'amazonResourceName',
        "aws_type":'awsType',
        "host_type":'hostType',
        "ip_addresses":'ipAddresses',
        "name":'name',
        "owner_id":'ownerId',
        "physical_source_id":'physicalSourceId',
        "region_id":'regionId',
        "resource_id":'resourceId',
        "restore_task_id":'restoreTaskId',
        "secret_access_key":'secretAccessKey',
        "tag_attributes":'tagAttributes',
        "mtype":'type',
        "user_account_id":'userAccountId',
        "user_resource_name":'userResourceName'
    }

    def __init__(self,
                 access_key=None,
                 amazon_resource_name=None,
                 aws_type=None,
                 host_type=None,
                 ip_addresses=None,
                 name=None,
                 owner_id=None,
                 physical_source_id=None,
                 region_id=None,
                 resource_id=None,
                 restore_task_id=None,
                 secret_access_key=None,
                 tag_attributes=None,
                 mtype=None,
                 user_account_id=None,
                 user_resource_name=None):
        """Constructor for the AwsProtectionSource class"""

        # Initialize members of the class
        self.access_key = access_key
        self.amazon_resource_name = amazon_resource_name
        self.aws_type = aws_type
        self.host_type = host_type
        self.ip_addresses = ip_addresses
        self.name = name
        self.owner_id = owner_id
        self.physical_source_id = physical_source_id
        self.region_id = region_id
        self.resource_id = resource_id
        self.restore_task_id = restore_task_id
        self.secret_access_key = secret_access_key
        self.tag_attributes = tag_attributes
        self.mtype = mtype
        self.user_account_id = user_account_id
        self.user_resource_name = user_resource_name


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
        host_type = dictionary.get('hostType')
        ip_addresses = dictionary.get('ipAddresses')
        name = dictionary.get('name')
        owner_id = dictionary.get('ownerId')
        physical_source_id = dictionary.get('physicalSourceId')
        region_id = dictionary.get('regionId')
        resource_id = dictionary.get('resourceId')
        restore_task_id = dictionary.get('restoreTaskId')
        secret_access_key = dictionary.get('secretAccessKey')
        tag_attributes = None
        if dictionary.get('tagAttributes') != None:
            tag_attributes = list()
            for structure in dictionary.get('tagAttributes'):
                tag_attributes.append(cohesity_management_sdk.models.tag_attribute.TagAttribute.from_dictionary(structure))
        mtype = dictionary.get('type')
        user_account_id = dictionary.get('userAccountId')
        user_resource_name = dictionary.get('userResourceName')

        # Return an object of this model
        return cls(access_key,
                   amazon_resource_name,
                   aws_type,
                   host_type,
                   ip_addresses,
                   name,
                   owner_id,
                   physical_source_id,
                   region_id,
                   resource_id,
                   restore_task_id,
                   secret_access_key,
                   tag_attributes,
                   mtype,
                   user_account_id,
                   user_resource_name)


