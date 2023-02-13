# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TypeRestoreSourceSummaryByObjectTypeElementEnum(object):

    """Implementation of the 'Type_RestoreSourceSummaryByObjectTypeElement'
    enum.

    Specify the object type to filter with.
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
    'kDeployVolumes' specifies a Restore Task that deploys volumes to a target
    environment.
    'kDownloadFiles' specifies a Restore Task that downloads the requested
    files and folders in zip format.
    'kRecoverEmails' specifies a Restore Task that recovers the mailbox/email
    items.
    'kConvertToPst' specifies a PST conversion task for selected mailbox/email
    items.
    'kRecoverDisks' specifies a Restore Task that recovers the virtual disks.
    'kRecoverNamespaces' specifies a Restore Task that recovers Kubernetes
    namespaces.
    'kCloneVMsToView' specifies a Restore Task that clones VMs into a View.

    Attributes:
        KMOUNTVOLUMES: TODO: type description here.
        KRESTOREFILES: TODO: type description here.
        KREMOVERAPP: TODO: type description here.
        KCLONEAPP: TODO: type description here.
        KRECOVERSANVOLUME: TODO: type description here.
        KCONVERTANDDEPLOYVMS: TODO: type description here.
        KMOUNTFILEVOLUME: TODO: type description here.
        KDEPLOYVMS: TODO: type description here.
        KDOWNLOADFILES: TODO: type description here.
        KRECOVEREMAILS: TODO: type description here.
        KCONVERTTOPST: TODO: type description here.
        KRECOVERDISKS: TODO: type description here.
        KRECOVERNAMESPACES: TODO: type description here.
        KCLONEVMSTOVIEW: TODO: type description here.


    """

    KRECOVERVMS = "kRecoverVMs"

    KCLONEVMS = "kCloneVMs"

    KCLONEVIEW = "kCloneView"

    KMOUNTVOLUMES = "kMountVolumes"

    KRESTOREFILES = "kRestoreFiles"

    KREMOVERAPP = "kRecoverApp"

    KCLONEAPP = "kCloneApp"

    KRECOVERSANVOLUME = "kRecoverSanVolume"

    KCONVERTANDDEPLOYVMS = "kConvertAndDeployVMs"

    KMOUNTFILEVOLUME = "kMountFileVolume"

    KSYSTEM = "kSystem"

    KRECOVERVLOUMES = "kRecoverVolumes"

    KDEPLOYVMS = "kDeployVMs"

    KDOWNLOADFILES = "kDownloadFiles"

    KRECOVEREMAILS = "kRecoverEmails"

    KCONVERTTOPST = "kConvertToPst"

    KRECOVERDISKS = "kRecoverDisks"

    KRECOVERNAMESPACES = "kRecoverNamespaces"

    KCLONEVMSTOVIEW = "kCloneVMsToView"

