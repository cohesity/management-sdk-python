# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class FleetSubnetTypeEnum(object):

    """Implementation of the 'FleetSubnetTypeEnum' enum.

    TODO: type enum description here.

    Attributes:
        Specifies the subnet type of the fleet.
          Specifies the type of the fleet subnet.
          'kCluster' implies same subnet as of Cluster, valid only for Cloud
          Edition cluster.
          'kSourceVM' implies same subnet as of source vm.
          'kCustom' implies the custome subnet.

    """

    K_CLUSTER = 'kCluster'

    K_SOURCE_VM = 'kSourceVM'

    K_CUSTOM = 'kCustom'

