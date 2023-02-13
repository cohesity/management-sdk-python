# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TypeCloneTaskRequestEnum(object):

    """Implementation of the 'Type_CloneTaskRequest' enum.

    Specifies the type of Restore Task such as 'kCloneVMs' or 'kCloneView'.
    'kCloneVMs' specifies a Restore Task that clones VMs.
    'kCloneView' specifies a Restore Task that clones a View.

    Attributes:
        KCLONEVMS: TODO: type description here.
        KCLONEVIEW: TODO: type description here.

    """

    KCLONEVMS = 'kCloneVMs'

    KCLONEVIEW = 'kCloneView'

