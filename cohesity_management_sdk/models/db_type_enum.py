# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class DbTypeEnum(object):

    """Implementation of the 'DbType' enum.

    Specifies the type of the database in Oracle Protection Source.
    'kRACDatabase' indicates the database is a RAC DB.
    'kSingleInstance' indicates that the database is single instance.

    Attributes:
        KSINGLEINSTANCE: TODO: type description here.
        KRACDATABASE: TODO: type description here.

    """

    KSINGLEINSTANCE = 'kSingleInstance'

    KRACDATABASE = 'kRACDatabase'

