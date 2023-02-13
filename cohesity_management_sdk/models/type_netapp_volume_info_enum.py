# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TypeNetappVolumeInfoEnum(object):

    """Implementation of the 'Type_NetappVolumeInfo' enum.

    Specifies the NetApp type of this volume.
    Specifies the type of a NetApp Volume.
    'kReadWrite' indicates read-write volume.
    'kLoadSharing' indicates load-sharing volume.
    'kDataProtection' indicates data-protection volume.
    'kDataCache' indicates data-cache volume.
    'kTmp' indicates temporaray purpose.
    'kUnknownType' indicates unknown type.

    Attributes:
        KREADWRITE: TODO: type description here.
        KLOADSHARING: TODO: type description here.
        KDATAPROTECTION: TODO: type description here.
        KDATACACHE: TODO: type description here.
        KTMP: TODO: type description here.
        KUNKNOWNTYPE: TODO: type description here.

    """

    KREADWRITE = 'kReadWrite'

    KLOADSHARING = 'kLoadSharing'

    KDATAPROTECTION = 'kDataProtection'

    KDATACACHE = 'kDataCache'

    KTMP = 'kTmp'

    KUNKNOWNTYPE = 'kUnknownType'

