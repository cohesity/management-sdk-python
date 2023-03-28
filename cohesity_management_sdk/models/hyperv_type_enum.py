# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class HypervTypeEnum(object):

    """Implementation of the 'HypervType' enum.
    Specifies the entity type if the environment is kHyperV.
    overrideDescription: true


    Attributes:
        KSCVMMSERVER: TODO: type description here.
        KSTANDALONEHOST: TODO: type description here.
        KSTANDALONECLUSTER: TODO: type description here.

    """

    KSCVMMSERVER = 'kSCVMMServer'

    KSTANDALONEHOST = 'kStandaloneHost'

    KSTANDALONECLUSTER = 'kStandaloneCluster'
