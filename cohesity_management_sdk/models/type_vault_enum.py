# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TypeVaultEnum(object):

    """Implementation of the 'Type_Vault' enum.

    Specifies the type of Vault.
    This field is deprecated. This field is split into ExternalTargetType in
    and TierType in respective credentials. Initialize those
    fields instead.
    deprecated: true
    'kNearline' indicates a Google Nearline Vault.
    'kGlacier' indicates an AWS Glacier Vault.
    'kS3' indicates an AWS S3 Vault.
    'kAzureStandard' indicates a Microsoft Azure Standard Vault.
    'kS3Compatible' indicates an S3 Compatible Vault.
    (See the online help for supported types.)
    'kQStarTape' indicates a QStar Tape Vault.
    'kGoogleStandard' indicates a Google Standard Vault.
    'kGoogleDRA' indicates a Google DRA Vault.
    'kAmazonS3StandardIA' indicates an Amazon S3 Standard-IA Vault.
    'kAWSGovCloud' indicates an AWS Gov Cloud Vault.
    'kNAS' indicates a NAS Vault.
    'kColdline' indicates a Google Coldline Vault.
    'kAzureGovCloud' indicates a Microsoft Azure Gov Cloud Vault.
    'kAzureArchive' indicates an Azure Archive Vault.
    'kAzure' indicates an Azure Vault.
    'kGoogle' indicates a Google Vault.
    'kAmazon' indicates an Amazon Vault.
    'kOracle' indicates an Oracle Vault.
    'kOracleTierStandard' indicates an Oracle Tier Standard Vault.
    'kOracleTierArchive' indicates an Oracle Tier Archive Vault.
    'kAmazonC2S' indicates an Amazon Commercial Cloud Services Vault.

    Attributes:
        KNEARLINE: TODO: type description here.
        KGLACIER: TODO: type description here.
        KS3: TODO: type description here.
        KAZURESTANDARD: TODO: type description here.
        KS3COMPATIBLE: TODO: type description here.
        KQSTARTAPE: TODO: type description here.
        KGOOGLESTANDARD: TODO: type description here.
        KGOOGLEDRA: TODO: type description here.
        KAMAZONS3STANDARDIA: TODO: type description here.
        KAWSGOVCLOUD: TODO: type description here.
        KNAS: TODO: type description here.
        KCOLDLINE: TODO: type description here.
        KAZUREGOVCLOUD: TODO: type description here.
        KAZUREARCHIVE: TODO: type description here.
        KAZURE: TODO: type description here.
        KGOOGLE: TODO: type description here.
        KAMAZON: TODO: type description here.
        KORACLE: TODO: type description here.
        KORACLETIERSTANDARD: TODO: type description here.
        KORACLETIERARCHIVE: TODO: type description here.
        KAMAZONC2S: TODO: type description here.

    """

    KNEARLINE = 'kNearline'

    KGLACIER = 'kGlacier'

    KS3 = 'kS3'

    KAZURESTANDARD = 'kAzureStandard'

    KS3COMPATIBLE = 'kS3Compatible'

    KQSTARTAPE = 'kQStarTape'

    KGOOGLESTANDARD = 'kGoogleStandard'

    KGOOGLEDRA = 'kGoogleDRA'

    KAMAZONS3STANDARDIA = 'kAmazonS3StandardIA'

    KAWS_GO_VCLOUD = 'kAWSGovCloud'

    KNAS = 'kNAS'

    KCOLDLINE = 'kColdline'

    K_AZURE_GO_VCLOUD = 'kAzureGovCloud'

    KAZUREARCHIVE = 'kAzureArchive'

    KAZURE = 'kAzure'

    KGOOGLE = 'kGoogle'

    KAMAZON = 'kAmazon'

    KORACLE = 'kOracle'

    KORACLETIERSTANDARD = 'kOracleTierStandard'

    KORACLETIERARCHIVE = 'kOracleTierArchive'

    KAMAZONC2S = 'kAmazonC2S'

