# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class StyleEnum(object):

    """Implementation of the 'Style' enum.

    Specifies the security style associated with this volume.
    Specifies the type of a NetApp Volume.
    'kUnix' indicates Unix-style security.
    'kNtfs' indicates Windows NTFS-style security.
    'kMixed' indicates mixed-style security.
    'kUnified' indicates Unified-style security.

    Attributes:
        KUNIX: TODO: type description here.
        KNTFS: TODO: type description here.
        KMIXED: TODO: type description here.
        KUNIFIED: TODO: type description here.

    """

    KUNIX = 'kUnix'

    KNTFS = 'kNtfs'

    KMIXED = 'kMixed'

    KUNIFIED = 'kUnified'

