# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TypeAdRestoreOptionsEnum(object):

    """Implementation of the 'Type_AdRestoreOptions' enum.

    Specifies the AD restore request type.
    Specifies the action type of AD restore.
    'kNone' specifies no special behaviour.
    'kObjects' specifies the user action to restore AD objects from a mounted
    AD snapshot database.
    'kObjectAttributes' specifies the user action to restore attributes of an
    AD object from a mounted AD snapshot database.

    Attributes:
        KNONE: TODO: type description here.
        KOBJECTS: TODO: type description here.
        KOBJECTATTRIBUTES: TODO: type description here.

    """

    KNONE = 'kNone'

    KOBJECTS = 'kObjects'

    KOBJECTATTRIBUTES = 'kObjectAttributes'

