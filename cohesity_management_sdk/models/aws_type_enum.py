# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

class AwsTypeEnum(object):

    """Implementation of the 'AwsType' enum.

    Specifies the entity type such as 'kIAMUser' if the environment is kAWS.
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

