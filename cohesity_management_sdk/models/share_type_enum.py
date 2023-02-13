# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ShareTypeEnum(object):

    """Implementation of the 'ShareType' enum.

    Specifies the sharing protocol type used to mount the file system.
    Currently, only NFS is supported.
    'kNFS' indicates use the NFS protocol to mount the file system.
    'kCIFS' indicates use the CIFS protocol to mount the file system.

    Attributes:
        KNFS: TODO: type description here.
        KCIFS: TODO: type description here.

    """

    KNFS = 'kNFS'

    KCIFS = 'kCIFS'

