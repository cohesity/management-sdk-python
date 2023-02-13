# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ObjectStatusEnum(object):

    """Implementation of the 'ObjectStatus' enum.

    Specifies the status of an object during a Restore Task.
    'kFilesCloned' indicates that the cloning has completed.
    'kFetchedEntityInfo' indicates that information about the object was
    fetched from the primary source.
    'kVMCreated' indicates that the new VM was created.
    'kRelocationStarted' indicates that restoring to a different
    resource pool has started.
    'kFinished' indicates that the Restore Task has finished.
    Whether it was successful or not is indicated by the error code that
    that is stored with the Restore Task.
    'kAborted' indicates that the Restore Task was aborted before
    trying to restore this object. This can happen if the
    Restore Task encounters a global error.
    For example during a 'kCloneVMs' Restore Task, the datastore
    could not be mounted. The entire Restore Task is aborted
    before trying to create VMs on the primary source.
    'kDataCopyStarted' indicates that the disk copy is started.
    'kInProgress' captures a generic in-progress state and can be used by
    restore
    operations that don't track individual states.

    Attributes:
        KFILESCLONED: TODO: type description here.
        KFETCHEDENTITYINFO: TODO: type description here.
        KVMCREATED: TODO: type description here.
        KRELOCATIONSTARTED: TODO: type description here.
        KFINISHED: TODO: type description here.
        KABORTED: TODO: type description here.
        KDATACOPYSTARTED: TODO: type description here.
        KINPROGRESS: TODO: type description here.

    """

    KFILESCLONED = 'kFilesCloned'

    KFETCHEDENTITYINFO = 'kFetchedEntityInfo'

    KVMCREATED = 'kVMCreated'

    KRELOCATIONSTARTED = 'kRelocationStarted'

    KFINISHED = 'kFinished'

    KABORTED = 'kAborted'

    KDATACOPYSTARTED = 'kDataCopyStarted'

    KINPROGRESS = 'kInProgress'

