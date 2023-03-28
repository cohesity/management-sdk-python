# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class AlertingPolicyEnum(object):

    """Implementation of the 'AlertingPolicy' enum.
    Array of Job Events.  During Job Runs, the following Job Events are
    generated: 1) Job succeeds 2) Job fails 3) Job violates the SLA These Job
    Events can cause Alerts to be generated. 'kSuccess' means the Protection
    Job succeeded. 'kFailure' means the Protection Job failed. 'kSlaViolation'
    means the Protection Job took longer than the time period specified in the
    SLA.


    Attributes:
        KSUCCESS: TODO: type description here.
        KFAILURE: TODO: type description here.
        KSLAVIOLATION: TODO: type description here.

    """

    KSUCCESS = 'kSuccess'

    KFAILURE = 'kFailure'

    KSLAVIOLATION = 'kSlaViolation'
