# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class SmbAccessEnum(object):

    """Implementation of the 'SmbAccess' enum.

    Specifies whether clients from this subnet can mount using SMB protocol.
    Protocol access level.
    'kDisabled' indicates Protocol access level 'Disabled'
    'kReadOnly' indicates Protocol access level 'ReadOnly'
    'kReadWrite' indicates Protocol access level 'ReadWrite'

    Attributes:
        KDISABLED: TODO: type description here.
        KREADONLY: TODO: type description here.
        KREADWRITE: TODO: type description here.

    """

    KDISABLED = 'kDisabled'

    KREADONLY = 'kReadOnly'

    KREADWRITE = 'kReadWrite'

