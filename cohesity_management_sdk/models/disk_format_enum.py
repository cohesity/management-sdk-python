# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class DiskFormatEnum(object):

    """Implementation of the 'DiskFormat' enum.

    Specifies the format of the virtual disk.
    'kVMDK' indicates VMware's Virtual Disk format.
    'kVHD' indicates Microsoft's Virtual Hard Drive format.
    'kVHDx' indicates Microsoft's Hyper-V Virtual Hard Drive format.
    'kRaw' indicates Raw disk format used by KVM, Acropolis.
    'kUnknow' indicates Unknown disk format.

    Attributes:
        KVMDK: TODO: type description here.
        KVHD: TODO: type description here.
        KVHDX: TODO: type description here.
        KRAW: TODO: type description here.
        KUNKNOWN: TODO: type description here.

    """

    KVMDK = 'kVMDK'

    KVHD = 'kVHD'

    KVHDX = 'kVHDx'

    KRAW = 'kRaw'

    KUNKNOWN = 'kUnknown'

