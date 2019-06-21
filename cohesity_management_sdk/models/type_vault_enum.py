# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

class TypeVaultEnum(object):

    """Implementation of the 'Type_Vault' enum.

    Specifies the type of Vault. This field is deprecated. This field is split
    into ExternalTargetType in and TierType in respective credentials.
    Initialize those fields instead. deprecated: true 'kNearline' indicates a
    Google Nearline Vault. 'kColdline' indicates a Google Coldline Vault.
    'kGlacier' indicates a AWS Glacier Vault. 'kS3' indicates a AWS S3 Vault.
    'kAzureStandard' indicates a Microsoft Azure Standard Vault.
    'kS3Compatible' indicates a AWS S3 Compatible Vault. (See the online help
    for supported types.) 'kQStarTape' indicates a QStar Tape Vault.
    'kGoogleStandard' indicates a Google Standard Vault. 'kGoogleDRA'
    indicates a Google DRA Vault. 'kAWSGovCloud' indicates a AWS Gov Cloud
    Vault. 'kNAS' indicates a NAS Vault. 'kAzureGovCloud' indicates an
    Microsoft Azure Gov Cloud Vault.

    Attributes:
        KNEARLINE: TODO: type description here.
        KCOLDLINE: TODO: type description here.
        KGLACIER: TODO: type description here.
        KS3: TODO: type description here.
        KAZURESTANDARD: TODO: type description here.
        KS3COMPATIBLE: TODO: type description here.
        KQSTARTAPE: TODO: type description here.
        KGOOGLESTANDARD: TODO: type description here.
        KGOOGLEDRA: TODO: type description here.
        KAWSGOVCLOUD: TODO: type description here.
        KNAS: TODO: type description here.
        KAZUREGOVCLOUD: TODO: type description here.

    """

    KNEARLINE = 'kNearline'

    KCOLDLINE = 'kColdline'

    KGLACIER = 'kGlacier'

    KS3 = 'kS3'

    KAZURESTANDARD = 'kAzureStandard'

    KS3COMPATIBLE = 'kS3Compatible'

    KQSTARTAPE = 'kQStarTape'

    KGOOGLESTANDARD = 'kGoogleStandard'

    KGOOGLEDRA = 'kGoogleDRA'

    KAWS_GO_VCLOUD = 'kAWSGovCloud'

    KNAS = 'kNAS'

    K_AZURE_GO_VCLOUD = 'kAzureGovCloud'

