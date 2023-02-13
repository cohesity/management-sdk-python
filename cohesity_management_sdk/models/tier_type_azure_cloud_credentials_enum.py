# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TierTypeAzureCloudCredentialsEnum(object):

    """Implementation of the 'TierType_AzureCloudCredentials' enum.

    Specifies the storage class of Azure.
    AzureTierType specifies the storage class for Azure.
    'kAzureTierHot' indicates a tier type of Azure properties that is
    accessed
    frequently.
    'kAzureTierCool' indicates a tier type of Azure properties that is
    accessed less frequently, and stored for at least 30 days.
    'kAzureTierArchive' indicates a tier type of Azure properties that is
    accessed rarely and stored for at least 180 days.

    Attributes:
        KAZURETIERHOT: TODO: type description here.
        KAZURETIERCOOL: TODO: type description here.
        KAZURETIERARCHIVE: TODO: type description here.

    """

    KAZURETIERHOT = 'kAzureTierHot'

    KAZURETIERCOOL = 'kAzureTierCool'

    KAZURETIERARCHIVE = 'kAzureTierArchive'

