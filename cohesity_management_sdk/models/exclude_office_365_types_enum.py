# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ExcludeOffice365TypesEnum(object):

    """Implementation of the 'excludeOffice365Types' enum.

    Specifies the Object types to be filtered out for Office 365 that match
    the passed in types such as 'kDomain', 'kOutlook', 'kMailbox', etc.
    For example, set this parameter to 'kMailbox' to exclude Mailbox Objects
    from being returned.

    Attributes:
        KDOMAIN: TODO: type description here.
        KOUTLOOK: TODO: type description here.
        KMAILBOX: TODO: type description here.
        KUSERS: TODO: type description here.
        KUSER: TODO: type description here.
        KGROUPS: TODO: type description here.
        KGROUP: TODO: type description here.
        KSITES: TODO: type description here.
        KSITE: TODO: type description here.

    """

    KDOMAIN = 'kDomain'

    KOUTLOOK = 'kOutlook'

    KMAILBOX = 'kMailbox'

    KUSERS = 'kUsers'

    KUSER = 'kUser'

    KGROUPS = 'kGroups'

    KGROUP = 'kGroup'

    KSITES = 'kSites'

    KSITE = 'kSite'
