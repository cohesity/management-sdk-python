# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class FileTypeEnum(object):

    """Implementation of the 'FileType' enum.

    Specifies the format type of the file that SQL database stores the data.
    Specifies the format type of the file that SQL database stores the data.
    'kRows' refers to a data file
    'kLog' refers to a log file
    'kFileStream' refers to a directory containing FILESTREAM data
    'kNotSupportedType' is for information purposes only. Not supported.
    'kFullText' refers to a full-text catalog.

    Attributes:
        KROWS: TODO: type description here.
        KLOG: TODO: type description here.
        KFILESTREAM: TODO: type description here.
        KNOTSUPPORTEDTYPE: TODO: type description here.
        KFULLTEXT: TODO: type description here.

    """

    KROWS = 'kRows'

    KLOG = 'kLog'

    KFILESTREAM = 'kFileStream'

    KNOTSUPPORTEDTYPE = 'kNotSupportedType'

    KFULLTEXT = 'kFullText'

