# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ValueTypeEnum(object):

    """Implementation of the 'ValueType' enum.

    Specifies the type of the value contained here. All values are returned
    as
    pointers to strings, but they can be casted to the type indicated here.
    'kInt64' indicates that the value stored in the Task Attribute is
    a 64-bit integer.
    'kDouble' indicates that the value stored in the Task Attribute is
    a 64 bit floating point number.
    'kString' indicates that the value stored in the Task Attribute is
    a string.
    'kBytes' indicates that the value stored in the Task Attribute is
    an array of bytes.

    Attributes:
        KINT64: TODO: type description here.
        KDOUBLE: TODO: type description here.
        KSTRING: TODO: type description here.
        KBYTES: TODO: type description here.

    """

    KINT64 = 'kInt64'

    KDOUBLE = 'kDouble'

    KSTRING = 'kString'

    KBYTES = 'kBytes'

