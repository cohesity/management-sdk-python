# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ServiceNameUpdateGflagParametersEnum(object):

    """Implementation of the 'ServiceName_UpdateGflagParameters' enum.

    Specifies the service name.
    'kApollo' is a service for reclaiming freed disk sectors on Nodes in the
    SnapFS distributed file system.
    'kBridge' is a service for managing the SnapFS distributed file system.
    'kGenie' is a service that is responsible for monitoring hardware health
    on the Cluster.
    'kGenieGofer' is a service that links the Genie service to other services
    on the Cluster.
    'kMagneto' is the data protection service of the Cohesity Data Platform.
    'kIris' is the service which serves REST API calls to the UI, CLI, and
    any
    scripts written by customers.
    'kIrisProxy' is a service that links the Iris service to other services
    on the Cluster.
    'kScribe' is the service responsible for storing filesystem metadata.
    'kStats' is the service that is responsible for retrieving and
    aggregating
    disk metrics across the Cluster.
    'kYoda' is an elastic search indexing service.
    'kAlerts' is a publisher and subscribing service for alerts.
    'kKeychain' is a service for managing disk encryption keys.
    'kLogWatcher' is a service that scans the log directory and reduces
    the number of logs if required.
    'kStatsCollector' is a service that periodically logs system stats.
    'kGandalf' is a distributed lock service and coordination manager.
    'kNexus' indicates the Nexus service. This is the service that is
    responsible for creation of Clusters and configuration of Nodes and
    networking.
    'kNexusProxy' is a service that links the Nexus service to other services
    on the Cluster.
    'kStorageProxy' is a service for accessing data on external entities.
    'kTricorder' is a diagnostic health testing service for Clusters.
    'kRtClient' is a reverse tunneling client service.
    'kVaultProxy' is a service for managing external targets that Clusters
    can be backed up to.
    'kSmbProxy' is an SMB protocol service.
    'kBridgeProxy' is the service that links the Bridge service to other
    services on the Cluster.
    'kLibrarian' is an elastic search indexing service.
    'kGroot' is a service for managing replication of SQL databases across
    multiple nodes in a Cluster.
    'kEagleAgent' is a service that is responsible for retrieving information
    on Cluster health.
    'kAthena' is a service for running distributed containerized applications
    on the Cohesity Data Platform.
    'kBifrostBroker' is a service for communicating with the Cohesity proxies
    for multitenancy.
    'kSmb2Proxy' is a new SMB protocol service.
    'kOs' can be specified in order to do a full reboot.
    'kAtom' is a service for receiving data for the Continuous Data Protection.
    'kPatch' is a service for downloading and applying patches.
    'kCompass' is a service for serving dns request for external and internal
    traffic.
    'kEtlServer' is a service responsible for ETling data for globalsearch.
    'kIcebox' is service that links Icebox service to other services on cluster.


    Attributes:
        KAPOLLO: TODO: type description here.
        KBRIDGE: TODO: type description here.
        KGENIE: TODO: type description here.
        KGENIEGOFER: TODO: type description here.
        KMAGNETO: TODO: type description here.
        KIRIS: TODO: type description here.
        KIRISPROXY: TODO: type description here.
        KSCRIBE: TODO: type description here.
        KSTATS: TODO: type description here.
        KYODA: TODO: type description here.
        KALERTS: TODO: type description here.
        KKEYCHAIN: TODO: type description here.
        KLOGWATCHER: TODO: type description here.
        KSTATSCOLLECTER: TODO: type description here.
        KGANDALF: TODO: type description here.
        KNEXUS: TODO: type description here.
        KNEXUSPROXY: TODO: type description here.
        KSTORAGEPROXY: TODO: type description here.
        KRTCLIENT: TODO: type description here.
        KVAULTPROXY: TODO: type description here.
        KSMBPROXY: TODO: type description here.
        KBRIDGEPROXY: TODO: type description here.
        KLIBRARIAN: TODO: type description here.
        KGROOT: TODO: type description here.
        KEAGLEAGENT: TODO: type description here.
        KATHENA: TODO: type description here.
        KBIFROSTBROKER: TODO: type description here.
        KSMB2PROXY: TODO: type description here.
        KOS: TODO: type description here.
        KATOM: TODO: type description here.
        KICEBOX: TODO: type description here.

    """

    KAPOLLO = 'kApollo'

    KBRIDGE = 'kBridge'

    KGENIE = 'kGenie'

    KGENIEGOFER = 'kGenieGofer'

    KMAGNETO = 'kMagneto'

    KIRIS = 'kIris'

    KIRISPROXY = 'kIrisProxy'

    KSCRIBE = 'kScribe'

    KSTATS = 'kStats'

    KYODA = 'kYoda'

    KALERTS = 'kAlerts'

    KKEYCHAIN = 'kKeychain'

    KLOGWATCHER = 'kLogWatcher'

    KSTATSCOLLECTER = 'kStatsCollecter'

    KGANDALF = 'kGandalf'

    KNEXUS = 'kNexus'

    KNEXUSPROXY = 'kNexusProxy'

    KSTORAGEPROXY = 'kStorageProxy'

    KRTCLIENT = 'kRtClient'

    KVAULTPROXY = 'kVaultProxy'

    KSMBPROXY = 'kSmbProxy'

    KBRIDGEPROXY = 'kBridgeProxy'

    KLIBRARIAN = 'kLibrarian'

    KGROOT = 'kGroot'

    KEAGLEAGENT = 'kEagleAgent'

    KATHENA = 'kAthena'

    KBIFROSTBROKER = 'kBifrostBroker'

    KSMB2PROXY = 'kSmb2Proxy'

    KOS = 'kOs'

    KATOM = 'kAtom'

    KICEBOX = 'kIcebox'

