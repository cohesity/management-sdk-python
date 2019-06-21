# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

class ExternalTargetTypeEnum(object):

    """Implementation of the 'ExternalTargetType' enum.

    Specifies the type of Vault. 'kS3Compatible' indicates a AWS S3 Compatible
    Vault. 'kQStarTape' indicates a QStar Tape Vault. 'kAWSGovCloud' indicates
    a AWS Gov Cloud Vault. 'kNAS' indicates a NAS Vault. 'kAzureGovCloud'
    indicates an Microsoft Azure Gov Cloud Vault. 'kAzure' indiactes an Azure
    vault. 'kGoogle' indcates a Google vault. 'kAmazon' indicates an AWS
    vault. 'kOracle' indicates an Oracle vault. 'kAmazonC2S' indicates an AWS
    C2S vault.

    Attributes:
        KS3COMPATIBLE: TODO: type description here.
        KQSTARTAPE: TODO: type description here.
        KAWSGOVCLOUD: TODO: type description here.
        KNAS: TODO: type description here.
        KAZUREGOVCLOUD: TODO: type description here.
        KAZURE: TODO: type description here.
        KGOOGLE: TODO: type description here.
        KAMAZON: TODO: type description here.
        KORACLE: TODO: type description here.
        KAMAZONC2S: TODO: type description here.

    """

    KS3COMPATIBLE = 'kS3Compatible'

    KQSTARTAPE = 'kQStarTape'

    KAWS_GO_VCLOUD = 'kAWSGovCloud'

    KNAS = 'kNAS'

    K_AZURE_GO_VCLOUD = 'kAzureGovCloud'

    KAZURE = 'kAzure'

    KGOOGLE = 'kGoogle'

    KAMAZON = 'kAmazon'

    KORACLE = 'kOracle'

    KAMAZONC2S = 'kAmazonC2S'

