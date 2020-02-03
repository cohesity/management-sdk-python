# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

class AlertTypeBucketEnum(object):

    """Implementation of the 'AlertTypeBucket' enum.

    Specifies the Alert type bucket.
    Specifies the Alert type bucket.
    kSoftware - Alerts which are related to Cohesity services.
    kHardware - Alerts related to hardware on which Cohesity software is
    running.
    kService - Alerts related to other external services.
    kOther - Alerts not of one of above categories.

    Attributes:
        KSOFTWARE: TODO: type description here.
        KHARDWARE: TODO: type description here.
        KSERVICE: TODO: type description here.
        KOTHER: TODO: type description here.

    """

    KSOFTWARE = 'kSoftware'

    KHARDWARE = 'kHardware'

    KSERVICE = 'kService'

    KOTHER = 'kOther'

