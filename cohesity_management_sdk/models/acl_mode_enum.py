# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class AclModeEnum(object):

    """Implementation of the 'AclMode' enum.

    ACL mode for this SMB share.
    'kNative' specifies native ACL mode supports UNIX-like ACLs and Windows
    ACLs. In native mode, because SMB natively supports both ACLs while NFS
    only supports UNIX ACLs, ACLs will not be shared between SMB and NFS.
    'kShared' shares UNIX-like ACL permissions with the NFS protocol.
    In shared mode both protocol ACL permissions are required to match.
    When one protocol creates files or modifies permissions, they must comply
    with the permission settings of the other protocol.

    Attributes:
        KSHARED: TODO: type description here.
        KNATIVE: TODO: type description here.

    """

    KSHARED = 'kShared'

    KNATIVE = 'kNative'

