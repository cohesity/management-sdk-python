# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class DistributionEnum(object):

    """Implementation of the 'Distribution' enum.
    Specifies the type of the entity in a Kubernetes environment. Determines
    the K8s distribution.


    Attributes:
        KMAINLINE: TODO: type description here.
        KOPENSHIFT: TODO: type description here.
        KRANCHER: TODO: type description here.
        KEKS: TODO: type description here.
        KGKE: TODO: type description here.
        KAKS: TODO: type description here.
        KVMWARETANZU: TODO: type description here.

    """

    KMAINLINE = 'kMainline'

    KOPENSHIFT = 'kOpenshift'

    KRANCHER = 'kRancher'

    KEKS = 'kEKS'

    KGKE = 'kGKE'

    KAKS = 'kAKS'

    KVMWARETANZU = 'kVMwareTanzu'
