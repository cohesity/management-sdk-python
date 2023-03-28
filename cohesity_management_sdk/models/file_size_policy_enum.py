# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class FileSizePolicyEnum(object):

    """Implementation of the 'FileSizePolicy' enum.
    Specifies policy to select a file to migrate based on its size. eg. A file
    can be selected to migrate if its size is greater than or smaller than the
    FileSizeBytes. enum: kGreaterThan, kSmallerThan. Specifies policy for file
    selection in data migration jobs based on file size. 'kGreaterThan':
    Migrate the files whose size are greater than specified file size.
    'kSmallerThan': Migrate the files whose size are smaller than specified
    file size.


    Attributes:
        KGREATERTHAN: TODO: type description here.
        KSMALLERTHAN: TODO: type description here.

    """

    KGREATERTHAN = 'kGreaterThan'

    KSMALLERTHAN = 'kSmallerThan'
