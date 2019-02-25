# Copyright 2019 Cohesity Inc. # -*- coding: utf-8 -*-

class ClusterTypeEnum(object):

    """Implementation of the 'ClusterType' enum.

    Specifies the type of Cohesity Cluster.
    'kPhysical' indicates the Cohesity Cluster is hosted directly on
    hardware.
    'kVirtualRobo' indicates the Cohesity Cluster is hosted in a VM on
    a ESXi Host of a VMware vCenter Server using Cohesity's Virtual Edition.
    'kMicrosoftCloud' indicates the Cohesity Cluster is hosed in a VM
    on Microsoft Azure using Cohesity's Cloud Edition.
    'kAmazonCloud' indicates the Cohesity Cluster is hosed in a VM
    on Amazon S3 using Cohesity's Cloud Edition.
    'kGoogleCloud' indicates the Cohesity Cluster is hosed in a VM
    on Google Cloud Platform using Cohesity's Cloud Edition.

    Attributes:
        KPHYSICAL: TODO: type description here.
        KVIRTUALROBO: TODO: type description here.
        KMICROSOFTCLOUD: TODO: type description here.
        KAMAZONCLOUD: TODO: type description here.
        KGOOGLECLOUD: TODO: type description here.

    """

    KPHYSICAL = 'kPhysical'

    KVIRTUALROBO = 'kVirtualRobo'

    KMICROSOFTCLOUD = 'kMicrosoftCloud'

    KAMAZONCLOUD = 'kAmazonCloud'

    KGOOGLECLOUD = 'kGoogleCloud'

