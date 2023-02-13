# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class LogicalVolumeTypeEnum(object):

    """Implementation of the 'LogicalVolumeType' enum.

    Specifies the type of logical volume such as kSimpleVolume, kLVM or kLDM.
    'kSimpleVolume' indicates a simple volume. Data can be used by just
    mounting the only one partition present on the disk.
    'kLVM' indicates a logical volume on Linux managed by a Logical Volume
    Manager. In order to access the data, deviceTree must be created based
    on the specification in logicalVolume.deviceTree.
    'kLDM' indicates a logical volume on Windows managed by Logical Disk
    Manager.

    Attributes:
        KSIMPLEVOLUME: TODO: type description here.
        KLVM: TODO: type description here.
        KLDM: TODO: type description here.

    """

    KSIMPLEVOLUME = 'kSimpleVolume'

    KLVM = 'kLVM'

    KLDM = 'kLDM'

