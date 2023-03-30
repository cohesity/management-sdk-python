# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class DataProtocolsEnum(object):

    """Implementation of the 'DataProtocols' enum.
    Array of Data Protocols.  Specifies the set of data protocols supported by
    this interface. 'kNfs' indicates NFS connections. 'kCifs' indicates SMB
    (CIFS) connections. 'kIscsi' indicates iSCSI connections. 'kFc' indicates
    Fiber Channel connections. 'kFcache' indicates Flex Cache connections.
    'kHttp' indicates HTTP connections. 'kNdmp' indicates NDMP connections.
    'kManagement' indicates non-data connections used for management purposes.
    'kNvme' indicates NVMe connections.


    Attributes:
        KNFS: TODO: type description here.
        KCIFS: TODO: type description here.
        KISCSI: TODO: type description here.
        KFC: TODO: type description here.
        KFCACHE: TODO: type description here.
        KHTTP: TODO: type description here.
        KNDMP: TODO: type description here.
        KMANAGEMENT: TODO: type description here.
        KNVME: TODO: type description here.

    """

    KNFS = 'kNfs'

    KCIFS = 'kCifs'

    KISCSI = 'kIscsi'

    KFC = 'kFc'

    KFCACHE = 'kFcache'

    KHTTP = 'kHttp'

    KNDMP = 'kNdmp'

    KMANAGEMENT = 'kManagement'

    KNVME = 'kNvme'
