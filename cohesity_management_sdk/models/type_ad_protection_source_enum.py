# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TypeAdProtectionSourceEnum(object):

    """Implementation of the 'Type_AdProtectionSource' enum.

    Specifies the type of the managed object in AD Protection Source.
    Specifies the kind of AD protection source.
    'kRootContainer' indicates the entity is a root container to an AD
    domain controller.
    'kDomainController' indicates the domain controller hosted in this
    physical
    server.

    Attributes:
        KROOTCONTAINER: TODO: type description here.
        KDOMAINCONTROLLER: TODO: type description here.

    """

    KROOTCONTAINER = 'kRootContainer'

    KDOMAINCONTROLLER = 'kDomainController'

