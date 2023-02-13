# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class AccessEnum(object):

    """Implementation of the 'Access' enum.

    Specifies the read/write access to the SMB share.
    'kReadyOnly' indicates read only access to the SMB share.
    'kReadWrite' indicates read and write access to the SMB share.
    'kFullControl' indicates full administrative control of the SMB share.
    'kSpecialAccess' indicates custom permissions to the SMB share using
    access masks structures.

    Attributes:
        KREADONLY: TODO: type description here.
        KREADWRITE: TODO: type description here.
        KMODIFY: TODO: type description here.
        KFULLCONTROL: TODO: type description here.
        KSPECIALACCESS: TODO: type description here.

    """

    KREADONLY = 'kReadOnly'

    KREADWRITE = 'kReadWrite'

    KMODIFY = 'kModify'

    KFULLCONTROL = 'kFullControl'

    KSPECIALACCESS = 'kSpecialAccess'


