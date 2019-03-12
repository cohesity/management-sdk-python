# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

class Type30Enum(object):

    """Implementation of the 'Type30' enum.

    Specifies the type of Restore Task such as 'kRecoverVMs' or
    'kMountVolumes'.
    'kRecoverVMs' specifies a Restore Task that recovers VMs.
    'kMountVolumes' specifies a Restore Task that mounts volumes to mount
    points.

    Attributes:
        KRECOVERVMS: TODO: type description here.
        KMOUNTVOLUMES: TODO: type description here.

    """

    KRECOVERVMS = 'kRecoverVMs'

    KMOUNTVOLUMES = 'kMountVolumes'

