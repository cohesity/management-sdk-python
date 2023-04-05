# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class MicrosoftAuthMethodEnum(object):

    """Implementation of the 'MicrosoftAuthMethod' enum.
    Specifies Authentication method to be used for API calls. 'kAzureAuthNone'
    indicates no authentication. 'kAzureClientSecret' indicates a client
    authentication. 'kAzureManagedIdentity' indicates a Azure based
    authentication.


    Attributes:
        KAZUREAUTHNONE: TODO: type description here.
        KAZURECLIENTSECRET: TODO: type description here.
        KAZUREMANAGEDIDENTITY: TODO: type description here.

    """

    KAZUREAUTHNONE = 'kAzureAuthNone'

    KAZURECLIENTSECRET = 'kAzureClientSecret'

    KAZUREMANAGEDIDENTITY = 'kAzureManagedIdentity'
