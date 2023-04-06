# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class VersioningEnum(object):

    """Implementation of the 'Versioning' enum.
    Specifies the Versioning state of S3 bucket. Specifies the versioning state
    of S3 bucket. 'kUnversioned' implies versioning is not enabled. 'kEnabled'
    implies versioning is enabled. 'kSuspended' versioning is suspended.


    Attributes:
        KUNVERSIONED: TODO: type description here.
        KENABLED: TODO: type description here.
        KSUSPENDED: TODO: type description here.

    """

    KUNVERSIONED = 'kUnversioned'

    KENABLED = 'kEnabled'

    KSUSPENDED = 'kSuspended'
