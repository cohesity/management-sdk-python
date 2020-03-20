# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

class TypeRestoreTaskEnum(object):

    """Implementation of the 'Type_RestoreTask' enum.

    Specifies the type of Restore Task.
    'kRecoverVMs' specifies a Restore Task that recovers VMs.
    'kCloneVMs' specifies a Restore Task that clones VMs.
    'kCloneView' specifies a Restore Task that clones a View.
    'kMountVolumes' specifies a Restore Task that mounts volumes.
    'kRestoreFiles' specifies a Restore Task that recovers files and folders.
    'kRecoverApp' specifies a Restore Task that recovers app.
    'kCloneApp' specifies a Restore Task that clone app.
    'kRecoverSanVolume' specifies a Restore Task that recovers SAN volumes.
    'kConvertAndDeployVMs' specifies a Restore Task that converts and deploy
    VMs to a target environment.
    'kMountFileVolume' specifies a Restore Task that mounts a file volume.
    'kSystem' specifies a Restore Task that recovers a system.
    'kRecoverVolumes' specifies a Restore Task that recovers volumes via the
    physical agent.
    'kDeployVolumes' specifies a Restore Task that deployes volumes to a
    target environment.
    'kDownloadFiles' specifies a Restore Task that downloads the requested
    files and folders in zip format.
    'kRecoverEmails' specifies a Restore Task that recovers the mailbox/email
    items.
    'kRecoverDisks' specifies a Restore Task that recovers the virtual disks.

    Attributes:
        KRECOVERVMS: TODO: type description here.
        KCLONEVMS: TODO: type description here.
        KCLONEVIEW: TODO: type description here.
        KMOUNTVOLUMES: TODO: type description here.
        KRESTOREFILES: TODO: type description here.
        KRECOVERAPP: TODO: type description here.
        KCLONEAPP: TODO: type description here.
        KRECOVERSANVOLUME: TODO: type description here.
        KCONVERTANDDEPLOYVMS: TODO: type description here.
        KMOUNTFILEVOLUME: TODO: type description here.
        KSYSTEM: TODO: type description here.
        KRECOVERVOLUMES: TODO: type description here.
        KDEPLOYVMS: TODO: type description here.
        KDOWNLOADFILES: TODO: type description here.
        KRECOVEREMAILS: TODO: type description here.
        KRECOVERDISKS: TODO: type description here.

    """

    KRECOVERVMS = 'kRecoverVMs'

    KCLONEVMS = 'kCloneVMs'

    KCLONEVIEW = 'kCloneView'

    KMOUNTVOLUMES = 'kMountVolumes'

    KRESTOREFILES = 'kRestoreFiles'

    KRECOVERAPP = 'kRecoverApp'

    KCLONEAPP = 'kCloneApp'

    KRECOVERSANVOLUME = 'kRecoverSanVolume'

    KCONVERTANDDEPLOYVMS = 'kConvertAndDeployVMs'

    KMOUNTFILEVOLUME = 'kMountFileVolume'

    KSYSTEM = 'kSystem'

    KRECOVERVOLUMES = 'kRecoverVolumes'

    KDEPLOYVMS = 'kDeployVMs'

    KDOWNLOADFILES = 'kDownloadFiles'

    KRECOVEREMAILS = 'kRecoverEmails'

    KRECOVERDISKS = 'kRecoverDisks'

