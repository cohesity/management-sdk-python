# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ChangesEnum(object):

    """Implementation of the 'Changes' enum.
    Specifies the list of changed values in a Protection Job.
    kProtectionJobName implies that protection job has change in the name field
    kProtectionJobDescription implies that protection job has change in the
    description field. kProtectionJobSources implies that protection job has
    change in the source field. kProtectionJobSchedule implies that protection
    job has change in the schedule field. kProtectionJobFullSchedule implies
    that protection job has change in the full schedule field.
    kProtectionJobRetrySettings implies that protection job has change in the
    retry settings. kProtectionJobRetentionPolicy implies that protection job
    has change in the retention policy. kProtectionJobIndexingPolicy implies
    that protection job has change in the indexing policy.
    kProtectionJobAlertingPolicy implies that protection job has change in the
    alerting policy. kProtectionJobPriority implies that protection job has
    change in the alerting policy. kProtectionJobQuiesce implies that
    protection job has change in the Quiesce. kProtectionJobSla implies that
    protection job has change in the SLA settings. kProtectionJobPolicyId
    implies that protection job has change in the poilcy Id settings.
    kProtectionJobTimezone implies that protection job has change in the
    timezone settings. kProtectionJobFutureRunsPaused implies that protection
    job has change in the future run settings. kProtectionJobFutureRunsResumed
    implies that protection job has change in the future run resume settings.
    kSnapshotTargetPolicy implies that protection job has change in the
    snapshot target policy settings. kProtectionJobQOS implies that protection
    job has change in QOS settings. kProtectionJobInvalidField implies that the
    changed field is invalid.


    Attributes:
        KPROTECTIONJOBNAME: TODO: type description here.
        KPROTECTIONJOBDESCRIPTION: TODO: type description here.
        KPROTECTIONJOBSOURCES: TODO: type description here.
        KPROTECTIONJOBSCHEDULE: TODO: type description here.
        KPROTECTIONJOBFULLSCHEDULE: TODO: type description here.
        KPROTECTIONJOBRETRYSETTINGS: TODO: type description here.
        KPROTECTIONJOBRETENTIONPOLICY: TODO: type description here.
        KPROTECTIONJOBINDEXINGPOLICY: TODO: type description here.
        KPROTECTIONJOBALERTINGPOLICY: TODO: type description here.
        KPROTECTIONJOBPRIORITY: TODO: type description here.
        KPROTECTIONJOBQUIESCE: TODO: type description here.
        KPROTECTIONJOBSLA: TODO: type description here.
        KPROTECTIONJOBPOLICYID: TODO: type description here.
        KPROTECTIONJOBTIMEZONE: TODO: type description here.
        KPROTECTIONJOBFUTURERUNSPAUSED: TODO: type description here.
        KPROTECTIONJOBFUTURERUNSRESUMED: TODO: type description here.
        KSNAPSHOTTARGETPOLICY: TODO: type description here.
        KPROTECTIONJOBBLACKOUTWINDOW: TODO: type description here.
        KPROTECTIONJOBQOS: TODO: type description here.
        KPROTECTIONJOBINVALIDFIELD: TODO: type description here.

    """

    KPROTECTIONJOBNAME = 'kProtectionJobName'

    KPROTECTIONJOBDESCRIPTION = 'kProtectionJobDescription'

    KPROTECTIONJOBSOURCES = 'kProtectionJobSources'

    KPROTECTIONJOBSCHEDULE = 'kProtectionJobSchedule'

    KPROTECTIONJOBFULLSCHEDULE = 'kProtectionJobFullSchedule'

    KPROTECTIONJOBRETRYSETTINGS = 'kProtectionJobRetrySettings'

    KPROTECTIONJOBRETENTIONPOLICY = 'kProtectionJobRetentionPolicy'

    KPROTECTIONJOBINDEXINGPOLICY = 'kProtectionJobIndexingPolicy'

    KPROTECTIONJOBALERTINGPOLICY = 'kProtectionJobAlertingPolicy'

    KPROTECTIONJOBPRIORITY = 'kProtectionJobPriority'

    KPROTECTIONJOBQUIESCE = 'kProtectionJobQuiesce'

    KPROTECTIONJOBSLA = 'kProtectionJobSla'

    KPROTECTIONJOBPOLICYID = 'kProtectionJobPolicyId'

    KPROTECTIONJOBTIMEZONE = 'kProtectionJobTimezone'

    KPROTECTIONJOBFUTURERUNSPAUSED = 'kProtectionJobFutureRunsPaused'

    KPROTECTIONJOBFUTURERUNSRESUMED = 'kProtectionJobFutureRunsResumed'

    KSNAPSHOTTARGETPOLICY = 'kSnapshotTargetPolicy'

    KPROTECTIONJOBBLACKOUTWINDOW = 'kProtectionJobBlackoutWindow'

    KPROTECTIONJOBQOS = 'kProtectionJobQOS'

    KPROTECTIONJOBINVALIDFIELD = 'kProtectionJobInvalidField'
