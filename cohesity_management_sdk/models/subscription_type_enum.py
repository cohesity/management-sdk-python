# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class SubscriptionTypeEnum(object):

    """Implementation of the 'SubscriptionType' enum.

    Specifies the subscription type of AWS such as 'kAWSCommercial' or
    'kAWSGovCloud'.
    Specifies the subscription type of an AWS source entity.
    'kAWSCommercial' indicates a standard AWS subscription.
    'kAWSGovCloud' indicates a govt AWS subscription.

    Attributes:
        KAWSCOMMERCIAL: TODO: type description here.
        KAWSGOVCLOUD: TODO: type description here.

    """

    KAWSCOMMERCIAL = 'kAWSCommercial'

    KAWS_GO_VCLOUD = 'kAWSGovCloud'

