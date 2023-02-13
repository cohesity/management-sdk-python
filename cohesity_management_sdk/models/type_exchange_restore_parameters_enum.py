# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TypeExchangeRestoreParametersEnum(object):

    """Implementation of the 'Type_ExchangeRestoreParameters' enum.

    Specifies the Exchange restore type.
    Specifies the type of Exchange restore.

    'kNone' specifies no special behaviour.
    'kView' specifies the option to create a view which cann be used by the
    external tools like Kroll to perform mailbox or mail-item recovery.
    'kDatabase' specifies the option to restore an Exchange database.

    Attributes:
        KNONE: TODO: type description here.
        KVIEW: TODO: type description here.
        KDATABASE: TODO: type description here.

    """

    KNONE = 'kNone'

    KVIEW = 'kView'

    KDATABASE = 'kDatabase'

