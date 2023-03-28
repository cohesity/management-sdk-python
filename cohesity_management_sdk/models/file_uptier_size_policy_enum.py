# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class FileUptierSizePolicyEnum(object):

    """Implementation of the 'FileUptierSizePolicy' enum.
    Specifies policy to select a file to uptier based on its size. eg. A file
    can be selected to uptier if its size is greater than or smaller than the
    FileSizeBytes. enum: kGreaterThan, kSmallerThan. Specifies policy for file
    selection in data uptier jobs based on file size. 'kGreaterThan': Uptier
    the files having size greater than file_size. 'kSmallerThan': Uptier the
    files having size smaller than file_size.


    Attributes:
        KGREATERTHAN: TODO: type description here.
        KSMALLERTHAN: TODO: type description here.

    """

    KGREATERTHAN = 'kGreaterThan'

    KSMALLERTHAN = 'kSmallerThan'
