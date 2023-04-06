# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class GcpFleetSubnetTypeEnum(object):

    """Implementation of the 'GcpFleetSubnetType' enum.
    Specifies the subnet type of the fleet. Specifies the type of the fleet
    subnet for GCP. 'kCluster' implies same subnet as of Cluster (for CE and
    NGCE cluster). 'kSourceVM' implies same subnet as of source vm. 'kCustom'
    implies the custome subnet.


    Attributes:
        KCLUSTER: TODO: type description here.
        KSOURCEVM: TODO: type description here.
        KCUSTOM: TODO: type description here.

    """

    KCLUSTER = 'kCluster'

    KSOURCEVM = 'kSourceVM'

    KCUSTOM = 'kCustom'
