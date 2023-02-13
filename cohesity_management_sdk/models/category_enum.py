# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class CategoryEnum(object):

    """Implementation of the 'Category' enum.

    Specifies alert category.
    Specifies the category of an Alert.
    kDisk - Alerts that are related to Disk.
    kNode - Alerts that are related to Node.
    kCluster - Alerts that are related to Cluster.
    kNodeHealth - Alerts that are related to Node Health.
    kClusterHealth - Alerts that are related to Cluster Health.
    kBackupRestore - Alerts that are related to Backup/Restore.
    kEncryption - Alerts that are related to Encryption.
    kArchivalRestore - Alerts that are related to Archival/Restore.
    kRemoteReplication - Alerts that are related to Remote Replication.
    kQuota - Alerts that are related to Quota.
    kLicense - Alerts that are related to License.
    kHeliosProActiveWellness - Alerts that are related to Helios ProActive
    Wellness.
    kHeliosAnalyticsJobs - Alerts that are related to Helios Analytics Jobs.
    kHeliosSignatureJobs - Alerts that are related to Helios Signature Jobs.
    kSecurity - Alerts that are related to Security.
    kAppsInfra - Alerts that are related to applications infra.
    kAntivirus - Alerts that are related to antivirus.
    kArchivalCopy - Alerts that are related to archival copies.

    Attributes:
        KDISK: TODO: type description here.
        KNODE: TODO: type description here.
        KCLUSTER: TODO: type description here.
        KNODEHEALTH: TODO: type description here.
        KCLUSTERHEALTH: TODO: type description here.
        KBACKUPRESTORE: TODO: type description here.
        KENCRYPTION: TODO: type description here.
        KARCHIVALRESTORE: TODO: type description here.
        KREMOTEREPLICATION: TODO: type description here.
        KQUOTA: TODO: type description here.
        KLICENSE: TODO: type description here.
        KHELIOSPROACTIVEWELLNESS: TODO: type description here.
        KHELIOSANALYTICSJOBS: TODO: type description here.
        KHELIOSSIGNATUREJOBS: TODO: type description here.
        KSECURITY: TODO: type description here.
        KAPPSINFRA: TODO: type description here.
        KANTIVIRUS: TODO: type description here.
        KARCHIVALCOPY: TODO: type description here.

    """

    KDISK = 'kDisk'

    KNODE = 'kNode'

    KCLUSTER = 'kCluster'

    KNODEHEALTH = 'kNodeHealth'

    KCLUSTERHEALTH = 'kClusterHealth'

    KBACKUPRESTORE = 'kBackupRestore'

    KENCRYPTION = 'kEncryption'

    KARCHIVALRESTORE = 'kArchivalRestore'

    KREMOTEREPLICATION = 'kRemoteReplication'

    KQUOTA = 'kQuota'

    KLICENSE = 'kLicense'

    KHELIOSPROACTIVEWELLNESS = 'kHeliosProActiveWellness'

    KHELIOSANALYTICSJOBS = 'kHeliosAnalyticsJobs'

    KHELIOSSIGNATUREJOBS = 'kHeliosSignatureJobs'

    KSECURITY = 'kSecurity'

    KAPPSINFRA = 'kAppsInfra'

    KANTIVIRUS = 'kAntivirus'

    KARCHIVALCOPY = 'kArchivalCopy'

