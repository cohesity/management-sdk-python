# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TypeVmDirEntryEnum(object):

    """Implementation of the 'Type_VmDirEntry' enum.

    DirEntryType is the type of entry i.e. file/folder.
    Specifies the type of directory entry.
    'kFile' indicates that current entry is of file type.
    'kDirectory' indicates that current entry is of directory type.
    'kSymlink' indicates that current entry is of symbolic link.

    Attributes:
        KFILE: TODO: type description here.
        KDIRECTORY: TODO: type description here.
        KSYMLINK: TODO: type description here.

    """

    KFILE = 'kFile'

    KDIRECTORY = 'kDirectory'

    KSYMLINK = 'kSymlink'

