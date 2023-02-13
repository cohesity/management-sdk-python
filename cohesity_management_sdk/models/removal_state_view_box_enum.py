# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class RemovalStateViewBoxEnum(object):

    """Implementation of the 'RemovalState_ViewBox' enum.

    Specifies the current removal state of the Storage Domain (View Box).
    'kDontRemove' means the state of object is functional and
    it is not being removed.
    'kMarkedForRemoval' means the object is being removed.
    'kOkToRemove' means the object has been removed on the Cohesity Cluster
    and
    if the object is physical, it can be removed from the Cohesity Cluster.

    Attributes:
        KDONTREMOVE: TODO: type description here.
        KMARKEDFORREMOVAL: TODO: type description here.
        KOKTOREMOVE: TODO: type description here.

    """

    KDONTREMOVE = 'kDontRemove'

    KMARKEDFORREMOVAL = 'kMarkedForRemoval'

    KOKTOREMOVE = 'kOkToRemove'

