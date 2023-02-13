# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class AagPreferenceEnum(object):

    """Implementation of the 'AagPreference' enum.

    Specifies the preference for backing up databases that are part of an
    AAG.
    Only applicable if 'aagPreferenceFromSqlServer' is set to false or not
    given.
    kPrimaryReplicaOnly implies backups should always occur on the primary
    replica.
    kSecondaryReplicaOnly implies backups should always occur on the secondary
    replica.
    kPreferSecondaryReplica implies secondary replica is preferred for
    backups.
    kAnyReplica implies no preference of about whether backups are performed
    on the primary replica or on a secondary replica. If no secondary replica
    is available, then performing backups on the primary replica is
    acceptable.

    Attributes:
        KPRIMARYREPLICAONLY: TODO: type description here.
        KSECONDARYREPLICAONLY: TODO: type description here.
        KPREFERSECONDARYREPLICA: TODO: type description here.
        KANYREPLICA: TODO: type description here.

    """

    KPRIMARYREPLICAONLY = 'kPrimaryReplicaOnly'

    KSECONDARYREPLICAONLY = 'kSecondaryReplicaOnly'

    KPREFERSECONDARYREPLICA = 'kPreferSecondaryReplica'

    KANYREPLICA = 'kAnyReplica'

