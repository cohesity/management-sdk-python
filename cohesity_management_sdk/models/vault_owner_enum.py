# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class VaultOwnerEnum(object):

    """Implementation of the 'VaultOwner' enum.
    Specifies if its a cohesity managed or customer managed key vault.
    'kCohesityManaged' indicates an internal KMS object. 'kCustomerManaged'
    indicates an Aws KMS object.


    Attributes:
        KCOHESITYMANAGED: TODO: type description here.
        KCUSTOMERMANAGED: TODO: type description here.

    """

    KCOHESITYMANAGED = 'kCohesityManaged'

    KCUSTOMERMANAGED = 'kCustomerManaged'
