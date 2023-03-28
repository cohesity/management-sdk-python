# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class VMwareTypeEnum(object):

    """Implementation of the 'VMwareType' enum.
    Specifies the entity type such as 'kVCenter' if the environment is kKMware.
    overrideDescription: true


    Attributes:
        KVCENTER: TODO: type description here.
        KSTANDALONEHOST: TODO: type description here.
        KVCLOUDDIRECTOR: TODO: type description here.

    """

    KVCENTER = 'kVCenter'

    KSTANDALONEHOST = 'kStandaloneHost'

    KVCLOUDDIRECTOR = 'kvCloudDirector'
