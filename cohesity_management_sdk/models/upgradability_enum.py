# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class UpgradabilityEnum(object):

    """Implementation of the 'Upgradability' enum.

    Specifies the upgradability of the agent running on the physical server.
    Specifies the upgradability of the agent running on the physical server.
    'kUpgradable' indicates the Agent can be upgraded to the agent software
    version on the cluster.
    'kCurrent' indicates the Agent is running the latest version.
    'kUnknown' indicates the Agent's version is not known.
    'kNonUpgradableInvalidVersion' indicates the Agent's version is invalid.
    'kNonUpgradableAgentIsNewer' indicates the Agent's version is newer than
    the agent software version the cluster.
    'kNonUpgradableAgentIsOld' indicates the Agent's version is too old that
    does not support upgrades.

    Attributes:
        KUPGRADABLE: TODO: type description here.
        KCURRENT: TODO: type description here.
        KUNKNOWN: TODO: type description here.
        KNONUPGRADABLEINVALIDVERSION: TODO: type description here.
        KNONUPGRADABLEAGENTISNEWER: TODO: type description here.
        KNONUPGRADABLEAGENTISOLD: TODO: type description here.

    """

    KUPGRADABLE = 'kUpgradable'

    KCURRENT = 'kCurrent'

    KUNKNOWN = 'kUnknown'

    KNONUPGRADABLEINVALIDVERSION = 'kNonUpgradableInvalidVersion'

    KNONUPGRADABLEAGENTISNEWER = 'kNonUpgradableAgentIsNewer'

    KNONUPGRADABLEAGENTISOLD = 'kNonUpgradableAgentIsOld'

