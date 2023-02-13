# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TypeRunJobSnapshotTargetEnum(object):

    """Implementation of the 'Type_RunJobSnapshotTarget' enum.

    Specifies the type of a Snapshot target such as 'kLocal', 'kRemote' or
    'kArchival'.
    'kLocal' means the Snapshot is stored on a local Cohesity Cluster.
    'kRemote' means the Snapshot is stored on a Remote Cohesity Cluster.
    (It was copied to the Remote Cohesity Cluster using replication.)
    'kArchival' means the Snapshot is stored on a Archival External Target
    (such as Tape or AWS).
    'kCloudDeploy' means the Snapshot is stored on a Cloud platform.

    Attributes:
        KLOCAL: TODO: type description here.
        KREMOTE: TODO: type description here.
        KARCHIVAL: TODO: type description here.
        KCLOUDDEPLOY: TODO: type description here.
        KCLOUDREPLICATION: TODO: type description here.

    """

    KLOCAL = 'kLocal'

    KREMOTE = 'kRemote'

    KARCHIVAL = 'kArchival'

    KCLOUDDEPLOY = 'kCloudDeploy'

    KCLOUDREPLICATION =  'kCloudReplication'

