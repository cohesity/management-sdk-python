# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class Office365TypeEnum(object):

    """Implementation of the 'Office365Type' enum.

    Specifies the entity type such as 'kDomain', 'kOutlook', 'kMailbox', if
    the
    environment is kO365.
    Specifies the type of Office 365 entity
    'kDomain' indicates the O365 domain through which authentication occurs.
    'kOutlook' indicates the Exchange online entities.
    'kMailbox' indicates the user's mailbox account.

    Attributes:
        KDOMAIN: TODO: type description here.
        KOUTLOOK: TODO: type description here.
        KMAILBOX: TODO: type description here.

    """

    KDOMAIN = 'kDomain'

    KOUTLOOK = 'kOutlook'

    KMAILBOX = 'kMailbox'

