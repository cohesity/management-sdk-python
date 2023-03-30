# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class SubscriptionTypeEnum(object):

    """Implementation of the 'SubscriptionType' enum.
    Specifies the subscription type of Azure such as 'kAzureCommercial',
    'kAzureGovCloud', 'kAzureStackCommercial' or 'kAzureStackADFS'. Specifies
    the subscription type of an Azure source entity. 'kAzureCommercial'
    indicates a standard Azure subscription. 'kAzureGovCloud' indicates a govt
    Azure subscription. 'kAzureStackCommercial' indicates a stack commercial
    Azure subscription. 'kAzureStackADFS' indicates a ADFS Azure subbscription.


    Attributes:
        KAZURECOMMERCIAL: TODO: type description here.
        KAZUREGOVCLOUD: TODO: type description here.
        KAZURESTACKCOMMERCIAL: TODO: type description here.
        KAZURESTACKADFS: TODO: type description here.

    """

    KAZURECOMMERCIAL = 'kAzureCommercial'

    K_AZURE_GOV_CLOUD = 'kAzureGovCloud'

    KAZURESTACKCOMMERCIAL = 'kAzureStackCommercial'

    KAZURESTACKADFS = 'kAzureStackADFS'
