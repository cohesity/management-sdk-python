# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class StatusRestoreTaskEnum(object):

    """Implementation of the 'Status_RestoreTask' enum.

    Specifies the overall status of the Restore Task.
    'kReadyToSchedule' indicates the Restore Task is waiting to be scheduled.
    'kProgressMonitorCreated' indicates the progress monitor for the
    Restore Task has been created.
    'kRetrievedFromArchive' indicates that the objects to restore have been
    retrieved from the specified archive. A Task will only ever transition to
    this state if a retrieval is necessary.
    'kAdmitted' indicates the task has been admitted. After a task has been
    admitted, its status does not move back to 'kReadyToSchedule' state
    even if it is rescheduled.
    'kInProgress' indicates that the Restore Task is in progress.
    'kFinishingProgressMonitor' indicates that the Restore Task is
    finishing its progress monitoring.
    'kFinished' indicates that the Restore Task has finished.
    The status indicating success or failure is found in the error code that
    is stored with the Restore Task.
    'kInternalViewCreated' indicates that internal view for the task
    has been created.
    'kZipFileRequested' indicates that request has been sent to create zip
    files for the files to be downloaded. This state is only going to be
    present for kDownloadFiles Task.
    'kCancelled' indicates that task or jb has been cancelled.

    Attributes:
        KREADYTOSCHEDULE: TODO: type description here.
        KPROGRESSMONITORCREATED: TODO: type description here.
        KRETRIEVEDFROMARCHIVE: TODO: type description here.
        KADMITTED: TODO: type description here.
        KINPROGRESS: TODO: type description here.
        KFINISHINGPROGRESSMONITOR: TODO: type description here.
        KFINISHED: TODO: type description here.
        KINTERNALVIEWCREATED: TODO: type description here.
        KZIPFILEREQUESTED: TODO: type description here.
        KCANCELLED: TODO: type description here.

    """

    KREADYTOSCHEDULE = 'kReadyToSchedule'

    KPROGRESSMONITORCREATED = 'kProgressMonitorCreated'

    KRETRIEVEDFROMARCHIVE = 'kRetrievedFromArchive'

    KADMITTED = 'kAdmitted'

    KINPROGRESS = 'kInProgress'

    KFINISHINGPROGRESSMONITOR = 'kFinishingProgressMonitor'

    KFINISHED = 'kFinished'

    KINTERNALVIEWCREATED = 'kInternalViewCreated'

    KZIPFILEREQUESTED = 'kZipFileRequested'

    KCANCELLED = 'kCancelled'

