# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class FlagsEnum(object):

    """Implementation of the 'Flags' enum.
    Specifies the flags related to the attribute values of the AD object.
    'kError' indicates error in conversion of AD Object value to string. The
    value in the AdAttributValue contains the error message. 'kTruncated'
    indicates the multi valued attribute is truncated when value exceeded
    'truncate_multivalues' value specified in the request. 'kCSV' indicates
    content in 'values' is a comma separated value (CSV) format of a complex
    object.


    Attributes:
        KERROR: TODO: type description here.
        KTRUNCATED: TODO: type description here.
        KCSV: TODO: type description here.

    """

    KERROR = 'kError'

    KTRUNCATED = 'kTruncated'

    KCSV = 'kCSV'
