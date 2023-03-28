# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class OwnershipContextEnum(object):

    """Implementation of the 'OwnershipContext' enum.
    Specifies the ownership context for consumption. 'kOwnershipContextLocal'
    indicates the Vault is used for local consumption
    'kOwnershipContextFortKnox' indicates the Vault is used for Fortknox
    consumption


    Attributes:
        KOWNERSHIPCONTEXTLOCAL: TODO: type description here.
        KOWNERSHIPCONTEXTFORTKNOX: TODO: type description here.

    """

    KOWNERSHIPCONTEXTLOCAL = 'kOwnershipContextLocal'

    KOWNERSHIPCONTEXTFORTKNOX = 'kOwnershipContextFortKnox'
