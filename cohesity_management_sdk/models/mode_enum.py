# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ModeEnum(object):

    """Implementation of the 'Mode' enum.

    Specifies how the permission should be applied to folders and/or files.
    'kFolderSubFoldersAndFiles' indicates that permissions are applied to a
    Folder
    and it's sub folders and files.
    'kFolderAndSubFolders' indicates that permissions are applied to a Folder
    and it's sub folders.
    'kFolderAndSubFiles' indicates that permissions are applied to a Folder
    and it's sub files.
    'kFolderOnly' indicates that permsission are applied to folder only.
    'kSubFoldersAndFilesOnly' indicates that permissions are applied to sub
    folders and files only.
    'kSubFoldersOnly' indicates that permissiona are applied to sub folders
    only.
    'kFilesOnly' indicates that permissions are applied to files only.

    Attributes:
        KFOLDERSUBFOLDERSANDFILES: TODO: type description here.
        KFOLDERANDSUBFOLDERS: TODO: type description here.
        KFOLDERANDFILES: TODO: type description here.
        KFOLDERONLY: TODO: type description here.
        KSUBFOLDERSANDFILESONLY: TODO: type description here.
        KSUBFOLDERSONLY: TODO: type description here.
        KFILESONLY: TODO: type description here.

    """

    KFOLDERSUBFOLDERSANDFILES = 'kFolderSubFoldersAndFiles'

    KFOLDERANDSUBFOLDERS = 'kFolderAndSubFolders'

    KFOLDERANDFILES = 'kFolderAndFiles'

    KFOLDERONLY = 'kFolderOnly'

    KSUBFOLDERSANDFILESONLY = 'kSubFoldersAndFilesOnly'

    KSUBFOLDERSONLY = 'kSubFoldersOnly'

    KFILESONLY = 'kFilesOnly'

