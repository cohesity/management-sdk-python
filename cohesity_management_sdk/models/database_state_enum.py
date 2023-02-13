# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class DatabaseStateEnum(object):

    """Implementation of the 'DatabaseState' enum.

    Specifies the state of the Exchange database copy.
    Specifies the state of Exchange Database Copy.


    'kUnknown' indicates the status is not known.
    'kMounted' indicates the exchange database copy is mounted and healthy.
    'kError' indicates  the  exchange  database  copy  is unmounted or
    partially mounted or is in error state.

    Attributes:
        KUNKNOWN: TODO: type description here.
        KMOUNTED: TODO: type description here.
        KERROR: TODO: type description here.

    """

    KUNKNOWN = 'kUnknown'

    KMOUNTED = 'kMounted'

    KERROR = 'kError'

