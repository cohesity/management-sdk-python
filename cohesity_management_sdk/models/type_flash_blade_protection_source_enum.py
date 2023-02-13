# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TypeFlashBladeProtectionSourceEnum(object):

    """Implementation of the 'Type_FlashBladeProtectionSource' enum.

    Specifies the type of managed object in a Pure Storage FlashBlade
    like 'kStorageArray' or 'kFileSystem'.
    'kStorageArray' indicates a top level Pure Storage FlashBlade array.
    'kFileSystem' indicates a Pure Storage FlashBlade file system within the
    array.

    Attributes:
        KSTORAGEARRAY: TODO: type description here.
        KFILESYSTEM: TODO: type description here.

    """

    KSTORAGEARRAY = 'kStorageArray'

    KFILESYSTEM = 'kFileSystem'

