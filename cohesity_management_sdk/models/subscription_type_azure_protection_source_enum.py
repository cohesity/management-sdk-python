# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class SubscriptionTypeAzureProtectionSourceEnum(object):

    """Implementation of the 'SubscriptionType_AzureProtectionSource' enum.
    Specifies the subscription type of Azure such as 'kAzureCommercial',
    'kAzureGovCloud' or 'kAzureStackCommercial'
    Specifies the subscription type of an Azure source entity.
    'kAzureCommercial' indicates a standard Azure subscription.
    'kAzureGovCloud' indicates a govt Azure subscription.
    'kAzureStackCommercial' indicates a stack commercial Azure subscription.
    'kAzureStackADFS' indicates a ADFS Azure subbscription.

    Attributes:
        KAZURECOMMERCIAL: TODO: type description here.
        KAZUREGOVCLOUD: TODO: type description here.
        KAZURESTACKCOMMERCIAL: TODO: type description here.
        KAZURESTACKADFS: TODO: type description here.

    """

    KAZURECOMMERCIAL = 'kAzureCommercial'

    K_AZURE_GO_VCLOUD = 'kAzureGovCloud'

    KAZURESTACKCOMMERCIAL = 'kAzureStackCommercial'

    KAZURESTACKADFS = 'kAzureStackADFS'
