# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class StorageTierEnum(object):

    """Implementation of the 'StorageTier' enum.

    StorageTier is the type of StorageTier.
    StorageTierType represents the various values for the Storage Tier.
    'kPCIeSSD' indicates storage tier type of Pci Solid State Drive.
    'kSATAHDD' indicates storage tier type of SATA Solid State Drive.
    'kSATAHDD' indicates storage tier type of SATA Hard Disk Drive.
    'kCLOUD' indicates storage tier type of Cloud.

    Attributes:
        KPCIESSD: TODO: type description here.
        KSATASSD: TODO: type description here.
        KSATAHDD: TODO: type description here.
        KCLOUD: TODO: type description here.

    """

    KPCIESSD = 'kPCIeSSD'

    KSATASSD = 'kSATASSD'

    KSATAHDD = 'kSATAHDD'

    KCLOUD = 'kCLOUD'

