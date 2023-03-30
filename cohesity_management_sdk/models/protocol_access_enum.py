# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ProtocolAccessEnum(object):

    """Implementation of the 'ProtocolAccess' enum.
    Specifies the supported Protocols for the View. 'kAll' enables protocol
    access to following three views: NFS, SMB and S3. 'kNFSOnly' enables
    protocol access to NFS only. 'kSMBOnly' enables protocol access to SMB
    only. 'kS3Only' enables protocol access to S3 only. 'kSwiftOnly' enables
    protocol access to Swift only. 'kUnknown' indicates that the protocol
    access of a view does not match any of the above. In this case, the
    constant is used as 'catch-all'.


    Attributes:
        KALL: TODO: type description here.
        KNFSONLY: TODO: type description here.
        KSMBONLY: TODO: type description here.
        KS3ONLY: TODO: type description here.
        KSWIFTONLY: TODO: type description here.
        KUNKNOWN: TODO: type description here.

    """

    KALL = 'kAll'

    KNFSONLY = 'kNFSOnly'

    KSMBONLY = 'kSMBOnly'

    KS3ONLY = 'kS3Only'

    KSWIFTONLY = 'kSwiftOnly'

    KUNKNOWN = 'kUnknown'
