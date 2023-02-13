# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class S3AccessEnum(object):

    """Implementation of the 'S3Access' enum.

    Specifies whether clients from this subnet can access using S3 protocol.
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

