# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.aws_fleet_params
import cohesity_management_sdk.models.c_2_s_server_info
import cohesity_management_sdk.models.ebs_volume_info
import cohesity_management_sdk.models.fleet_network_params
import cohesity_management_sdk.models.tag_attribute


class AwsProtectionSource(object):

    """Implementation of the 'AwsProtectionSource' model.

    Specifies a Protection Source in AWS environment.


    Attributes:

        access_key (string): Specifies Access key of the AWS account.
        amazon_resource_name (string): Specifies Amazon Resource Name (owner
            ID) of the IAM user, act as an unique identifier of as AWS entity.
        auth_method (AuthMethodEnum): Specifies the authentication method to be
            used for API calls. Specifies the authentication method to be used
            for API calls. 'kUseIAMUser' indicates a user based authentication.
            'kUseIAMRole' indicates a role based authentication, used only for
            AWS CE. 'kUseHelios' indicates a Helios based authentication.
        aws_fleet_params (AwsFleetParams): Specifies information related to AWS
            fleets launched for various purposes. This will only be set for
            kIAMUser entity.
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
        cluster_network_info (FleetNetworkParams): Specifies information
            related to cluster. This is only valid for CE clusters. This is
            only populated for kIAMUser entity.
        db_engine_id (string): Specifies DB engine version info of the entity.
            This is populated only for RDSInstance, RDSOptionGroup and
            RDSParameterGroup entity types.
        host_type (HostTypeEnum): Specifies the OS type of the Protection
            Source of type 'kVirtualMachine' such as 'kWindows' or 'kLinux'.
            overrideDescription: true 'kLinux' indicates the Linux operating
            system. 'kWindows' indicates the Microsoft Windows operating
            system. 'kAix' indicates the IBM AIX operating system. 'kSolaris'
            indicates the Oracle Solaris operating system. 'kSapHana' indicates
            the Sap Hana database system developed by SAP SE. 'kSapOracle'
            indicates the Sap Oracle database system developed by SAP SE.
            'kCockroachDB' indicates the CockroachDB database system. 'kMySQL'
            indicates the MySQL database system. 'kOther' indicates the other
            types of operating system.
        iam_role_arn (string): Specifies the IAM role which will be used to
            access the security credentials required for API calls.
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
        region_id (string): Specifies the region Id of the entity if the entity
            is an EC2 instance.
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
        subscription_type (SubscriptionTypeEnum): Specifies the subscription
            type of AWS such as 'kAWSCommercial' or 'kAWSGovCloud'. Specifies
            the subscription type of an AWS source entity. 'kAWSCommercial'
            indicates a standard AWS subscription. 'kAWSGovCloud' indicates a
            govt AWS subscription.
        tag_attributes (list of TagAttribute): Specifies the list of AWS tag
            attributes.
        mtype (TypeAwsProtectionSourceEnum): Specifies the type of an AWS
            Protection Source Object such as 'kStorageContainer',
            'kVirtualMachine', 'kVirtualNetwork', etc. Specifies the type of an
            AWS source entity. 'kIAMUser' indicates a unique user within an AWS
            account. 'kRegion' indicates a geographical region in the global
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
        user_account_id (string): Specifies the account id derived from the ARN
            of the user.
        user_resource_name (string): Specifies the Amazon Resource Name (ARN)
            of the user.
        volumes (list of EbsVolumeInfo): Specified the list of EBS volumes
            attached to the entity if the entity is an EC2 instance.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "access_key":'accessKey',
        "amazon_resource_name":'amazonResourceName',
        "auth_method":'authMethod',
        "aws_fleet_params":'awsFleetParams',
        "aws_type":'awsType',
        "c_2_s_server_info":'c2sServerInfo',
        "cluster_network_info":'clusterNetworkInfo',
        "db_engine_id":'dbEngineId',
        "host_type":'hostType',
        "iam_role_arn":'iamRoleArn',
        "ip_addresses":'ipAddresses',
        "name":'name',
        "owner_id":'ownerId',
        "physical_source_id":'physicalSourceId',
        "region_id":'regionId',
        "resource_id":'resourceId',
        "restore_task_id":'restoreTaskId',
        "secret_access_key":'secretAccessKey',
        "subscription_type":'subscriptionType',
        "tag_attributes":'tagAttributes',
        "mtype":'type',
        "user_account_id":'userAccountId',
        "user_resource_name":'userResourceName',
        "volumes":'volumes',
    }
    def __init__(self,
                 access_key=None,
                 amazon_resource_name=None,
                 auth_method=None,
                 aws_fleet_params=None,
                 aws_type=None,
                 c_2_s_server_info=None,
                 cluster_network_info=None,
                 db_engine_id=None,
                 host_type=None,
                 iam_role_arn=None,
                 ip_addresses=None,
                 name=None,
                 owner_id=None,
                 physical_source_id=None,
                 region_id=None,
                 resource_id=None,
                 restore_task_id=None,
                 secret_access_key=None,
                 subscription_type=None,
                 tag_attributes=None,
                 mtype=None,
                 user_account_id=None,
                 user_resource_name=None,
                 volumes=None,
            ):

        """Constructor for the AwsProtectionSource class"""

        # Initialize members of the class
        self.access_key = access_key
        self.amazon_resource_name = amazon_resource_name
        self.auth_method = auth_method
        self.aws_fleet_params = aws_fleet_params
        self.aws_type = aws_type
        self.c_2_s_server_info = c_2_s_server_info
        self.cluster_network_info = cluster_network_info
        self.db_engine_id = db_engine_id
        self.host_type = host_type
        self.iam_role_arn = iam_role_arn
        self.ip_addresses = ip_addresses
        self.name = name
        self.owner_id = owner_id
        self.physical_source_id = physical_source_id
        self.region_id = region_id
        self.resource_id = resource_id
        self.restore_task_id = restore_task_id
        self.secret_access_key = secret_access_key
        self.subscription_type = subscription_type
        self.tag_attributes = tag_attributes
        self.mtype = mtype
        self.user_account_id = user_account_id
        self.user_resource_name = user_resource_name
        self.volumes = volumes

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
        aws_fleet_params = cohesity_management_sdk.models.aws_fleet_params.AwsFleetParams.from_dictionary(dictionary.get('awsFleetParams')) if dictionary.get('awsFleetParams') else None
        aws_type = dictionary.get('awsType')
        c_2_s_server_info = cohesity_management_sdk.models.c_2_s_server_info.C2SServerInfo.from_dictionary(dictionary.get('c2sServerInfo')) if dictionary.get('c2sServerInfo') else None
        cluster_network_info = cohesity_management_sdk.models.fleet_network_params.FleetNetworkParams.from_dictionary(dictionary.get('clusterNetworkInfo')) if dictionary.get('clusterNetworkInfo') else None
        db_engine_id = dictionary.get('dbEngineId')
        host_type = dictionary.get('hostType')
        iam_role_arn = dictionary.get('iamRoleArn')
        ip_addresses = dictionary.get('ipAddresses')
        name = dictionary.get('name')
        owner_id = dictionary.get('ownerId')
        physical_source_id = dictionary.get('physicalSourceId')
        region_id = dictionary.get('regionId')
        resource_id = dictionary.get('resourceId')
        restore_task_id = dictionary.get('restoreTaskId')
        secret_access_key = dictionary.get('secretAccessKey')
        subscription_type = dictionary.get('subscriptionType')
        tag_attributes = None
        if dictionary.get('tagAttributes') != None:
            tag_attributes = list()
            for structure in dictionary.get('tagAttributes'):
                tag_attributes.append(cohesity_management_sdk.models.tag_attribute.TagAttribute.from_dictionary(structure))
        mtype = dictionary.get('type')
        user_account_id = dictionary.get('userAccountId')
        user_resource_name = dictionary.get('userResourceName')
        volumes = None
        if dictionary.get('volumes') != None:
            volumes = list()
            for structure in dictionary.get('volumes'):
                volumes.append(cohesity_management_sdk.models.ebs_volume_info.EbsVolumeInfo.from_dictionary(structure))

        # Return an object of this model
        return cls(
            access_key,
            amazon_resource_name,
            auth_method,
            aws_fleet_params,
            aws_type,
            c_2_s_server_info,
            cluster_network_info,
            db_engine_id,
            host_type,
            iam_role_arn,
            ip_addresses,
            name,
            owner_id,
            physical_source_id,
            region_id,
            resource_id,
            restore_task_id,
            secret_access_key,
            subscription_type,
            tag_attributes,
            mtype,
            user_account_id,
            user_resource_name,
            volumes
)