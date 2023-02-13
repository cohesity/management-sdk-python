# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class FolderTypeEnum(object):

    """Implementation of the 'FolderType' enum.

    Specifies the folder type for the 'kFolder' Object.
    'kVMFolder' indicates folder can hold VMs or vApps.
    'kHostFolder' indicates folder can hold hosts and compute resources.
    'kDatastoreFolder' indicates folder can hold datastores and storage pods.
    'kNetworkFolder' indicates folder can hold networks and switches.
    'kRootFolder' indicates folder can hold datacenters.

    Attributes:
        KVMFOLDER: TODO: type description here.
        KHOSTFOLDER: TODO: type description here.
        KDATASTOREFOLDER: TODO: type description here.
        KNETWORKFOLDER: TODO: type description here.
        KROOTFOLDER: TODO: type description here.

    """

    KVMFOLDER = 'kVMFolder'

    KHOSTFOLDER = 'kHostFolder'

    KDATASTOREFOLDER = 'kDatastoreFolder'

    KNETWORKFOLDER = 'kNetworkFolder'

    KROOTFOLDER = 'kRootFolder'

