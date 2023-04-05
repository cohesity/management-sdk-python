# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class VmwareTypeEnum(object):

    """Implementation of the 'VmwareType' enum.
    Specifies the entity type such as 'kVCenter' if the environment is kKMware.
    overrideDescription: true


    Attributes:
        KVCENTER: TODO: type description here.
        KSTANDALONEHOST: TODO: type description here.
        KVCLOUDDIRECTOR: TODO: type description here.

    """

    KVCENTER = 'kVCenter'

    KSTANDALONEHOST = 'kStandaloneHost'

    K_VCLOUD_DIRECTOR = 'kvCloudDirector'
