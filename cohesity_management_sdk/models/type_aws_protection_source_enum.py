# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

class TypeAwsProtectionSourceEnum(object):

    """Implementation of the 'Type_AwsProtectionSource' enum.

    Specifies the type of an AWS Protection Source Object such as
    'kStorageContainer', 'kVirtualMachine', 'kVirtualNetwork', etc.
    Specifies the type of an AWS source entity.
    'kIAMUser' indicates a unique user within an AWS account.
    'kRegion' indicates a geographical region in the global infrastructure.
    'kAvailabilityZone' indicates an availability zone within a region.
    'kEC2Instance' indicates a Virtual Machine running in AWS environment.
    'kVPC' indicates a virtual private cloud (VPC) network within AWS.
    'kSubnet' indicates a subnet inside the VPC.
    'kNetworkSecurityGroup' represents a network security group.
    'kInstanceType' represents various machine types.
    'kKeyPair' represents a pair of public and private key used to login into
    a Virtual Machine.
    'kTag' represents a tag attached to EC2 instance.
    'kRDSOptionGroup' represents a RDS option group for configuring database
    features.
    'kRDSParameterGroup' represents a RDS parameter group.
    'kRDSInstance' represents a RDS DB instance.
    'kRDSSubnet' represents a RDS subnet.
    'kRDSTag' represents a tag attached to RDS instance.

    Attributes:
        KIAMUSER: TODO: type description here.
        KREGION: TODO: type description here.
        KAVAILABILITYZONE: TODO: type description here.
        KEC2INSTANCE: TODO: type description here.
        KVPC: TODO: type description here.
        KSUBNET: TODO: type description here.
        KNETWORKSECURITYGROUP: TODO: type description here.
        KINSTANCETYPE: TODO: type description here.
        KKEYPAIR: TODO: type description here.
        KTAG: TODO: type description here.
        KRDSOPTIONGROUP: TODO: type description here.
        KRDSPARAMETERGROUP: TODO: type description here.
        KRDSINSTANCE: TODO: type description here.
        KRDSSUBNET: TODO: type description here.
        KRDSTAG: TODO: type description here.

    """

    KIAMUSER = 'kIAMUser'

    KREGION = 'kRegion'

    KAVAILABILITYZONE = 'kAvailabilityZone'

    KEC2INSTANCE = 'kEC2Instance'

    KVPC = 'kVPC'

    KSUBNET = 'kSubnet'

    KNETWORKSECURITYGROUP = 'kNetworkSecurityGroup'

    KINSTANCETYPE = 'kInstanceType'

    KKEYPAIR = 'kKeyPair'

    KTAG = 'kTag'

    KRDSOPTIONGROUP = 'kRDSOptionGroup'

    KRDSPARAMETERGROUP = 'kRDSParameterGroup'

    KRDSINSTANCE = 'kRDSInstance'

    KRDSSUBNET = 'kRDSSubnet'

    KRDSTAG = 'kRDSTag'

