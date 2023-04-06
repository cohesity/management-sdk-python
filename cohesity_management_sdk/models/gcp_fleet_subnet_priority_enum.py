# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class GcpFleetSubnetPriorityEnum(object):

    """Implementation of the 'GcpFleetSubnetPriority' enum.
    Specifies the priority of the subnet type. Specifies the priority of the
    fleet subnet type for GCP. 'kPrimary' implies first priority to subnet
    type. 'kSecondary' implies second priority to subnet type. 'kTertiary'
    implies third priority to subnet type.


    Attributes:
        KCLUSTER: TODO: type description here.
        KSOURCEVM: TODO: type description here.
        KCUSTOM: TODO: type description here.

    """

    KCLUSTER = 'kCluster'

    KSOURCEVM = 'kSourceVM'

    KCUSTOM = 'kCustom'
