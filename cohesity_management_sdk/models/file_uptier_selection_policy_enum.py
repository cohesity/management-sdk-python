# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class FileUptierSelectionPolicyEnum(object):

    """Implementation of the 'FileUptierSelectionPolicy' enum.
    Specifies policy to select a file to uptier based on file access or
    modification time. eg. A file can be selected to uptier if it has been
    accessed in the HotFileWindow or it is modified. enum: kLastAccessed,
    kLastModified. Specifies policy for file selection in data uptier jobs.
    'kLastAccessed': Uptier the files which are accessed for at least
    num_file_access in hot_file_window. 'kLastModified': Uptier the files which
    are modified.


    Attributes:
        KLASTACCESSED: TODO: type description here.
        KLASTMODIFIED: TODO: type description here.

    """

    KLASTACCESSED = 'kLastAccessed'

    KLASTMODIFIED = 'kLastModified'
