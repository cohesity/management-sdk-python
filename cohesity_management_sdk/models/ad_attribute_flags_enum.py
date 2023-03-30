# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class AdAttributeFlagsEnum(object):

    """Implementation of the 'AdAttributeFlags' enum.
    Specifies the flags related to the attribute of the AD object. 'kEqual'
    indicates the attribute value of AD object from Snapshot and Production AD
    are equal. 'kNotEqual' indicates the attribute value of AD object from
    Snapshot and Production AD are not equal. 'kNotFound' indicates attribute
    of the AD object is missing from both Snapshot and Production AD. 'kSystem'
    indicates this is system attribute. This can only be updated by the AD
    internal component. 'kMultiValue' indicates that the attribute is
    mutli-value attribute. This attribute supports mutli-value merge during
    attribute restore operation.


    Attributes:
        KEQUAL: TODO: type description here.
        KNOTEQUAL: TODO: type description here.
        KNOTFOUND: TODO: type description here.
        KSYSTEM: TODO: type description here.
        KMULTIVALUE: TODO: type description here.

    """

    KEQUAL = 'kEqual'

    KNOTEQUAL = 'kNotEqual'

    KNOTFOUND = 'kNotFound'

    KSYSTEM = 'kSystem'

    KMULTIVALUE = 'kMultiValue'
