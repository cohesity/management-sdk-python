# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class OriginEnum(object):

    """Implementation of the 'origin' enum.

    Specifies the origin of the protection policy.
    'kHelios' means a global policy which was created on Helios.
    'kLocal' means a local policy which was created on the cluster.

    Attributes:
        KHELIOS: TODO: type description here.
        KLOCAL: TODO: type description here.

    """

    KHELIOS = 'kHelios'

    KLOCAL = 'kLocal'

