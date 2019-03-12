# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

class Type6Enum(object):

    """Implementation of the 'Type6' enum.

    Specifies the type of the datastore object like kFileShare or kVolume.
    overrideDescription: true
    Specifies the type of a HyperV datastore object.
    'kFileShare' indicates SMB file share datastore.
    'kVolume' indicates a volume which can a LUN.

    Attributes:
        KFILESHARE: TODO: type description here.
        KVOLUME: TODO: type description here.

    """

    KFILESHARE = 'kFileShare'

    KVOLUME = 'kVolume'

