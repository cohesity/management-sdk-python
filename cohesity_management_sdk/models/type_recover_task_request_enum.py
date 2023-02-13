# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TypeRecoverTaskRequestEnum(object):

    """Implementation of the 'Type_RecoverTaskRequest' enum.

    Specifies the type of Restore Task such as 'kRecoverVMs' or
    'kMountVolumes'.
    'kRecoverVMs' specifies a Restore Task that recovers VMs.
    'kMountVolumes' specifies a Restore Task that mounts volumes to mount
    points.
    'kRecoverNamespaces' specifies a Restore Task that recovers Kubernetes
    namespaces.
    'kMountFileVolume' specifies a Restore Task that mounts a file volume.

    Attributes:
        KRECOVERVMS: TODO: type description here.
        KMOUNTVOLUMES: TODO: type description here.
        KRECOVERNAMESPACES: TODO: type description here.
        KMOUNTFILEVOLUME: TODO: type description here.

    """

    KRECOVERVMS = 'kRecoverVMs'

    KMOUNTVOLUMES = 'kMountVolumes'

    KRECOVERNAMESPACES = 'kRecoverNamespaces'

    KMOUNTFILEVOLUME = 'kMountFileVolume'

