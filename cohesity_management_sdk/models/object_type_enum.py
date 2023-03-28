# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ObjectTypeEnum(object):

    """Implementation of the 'ObjectType' enum.
    Type of this object Specifies the type of an Universal Data Adapter source
    entity. 'kStandard' indicates a Universal Data Adapter source, possibly
    distributed over several physical nodes. 'kCustom' indicates a generic
    object within the UDA environment.


    Attributes:
        KSTANDARD: TODO: type description here.
        KCUSTOM: TODO: type description here.

    """

    KSTANDARD = 'kStandard'

    KCUSTOM = 'kCustom'
