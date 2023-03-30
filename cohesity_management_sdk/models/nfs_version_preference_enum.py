# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class NfsVersionPreferenceEnum(object):

    """Implementation of the 'NfsVersionPreference' enum.
    Specifies the preferred NFS protocol to use for the backup when multiple
    NFS protocols are present on a single volume. Specifies the protocol used
    by a NAS server. 'kNfs3' indicates NFS v3 protocol. 'kCifs1' indicates CIFS
    v1.0 protocol.


    Attributes:
        KNFS3: TODO: type description here.
        KCIFS1: TODO: type description here.

    """

    KNFS3 = 'kNfs3'

    KCIFS1 = 'kCifs1'
