# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class FileSelectionPolicyEnum(object):

    """Implementation of the 'FileSelectionPolicy' enum.
    Specifies policy to select a file to migrate based on its creation, last
    access or modification time. eg. A file can be selected to migrate if it
    has not been accessed/modified in the ColdFileWindow. enum: kOlderThan,
    kLastAccessed, kLastModified. Specifies policy for file selection in data
    migration jobs based on time. 'kOlderThan': Migrate the files that are
    older than cold file window. 'kLastAccessed': Migrate the files that are
    not accessed in cold file window. 'kLastModified': Migrate the files that
    have not been modified in cold file window.


    Attributes:
        KOLDERTHAN: TODO: type description here.
        KLASTACCESSED: TODO: type description here.
        KLASTMODIFIED: TODO: type description here.

    """

    KOLDERTHAN = 'kOlderThan'

    KLASTACCESSED = 'kLastAccessed'

    KLASTMODIFIED = 'kLastModified'
