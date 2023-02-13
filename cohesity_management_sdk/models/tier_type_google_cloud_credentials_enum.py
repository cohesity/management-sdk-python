# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class TierTypeGoogleCloudCredentialsEnum(object):

    """Implementation of the 'TierType_GoogleCloudCredentials' enum.

    Specifies the storage class of GCP.
    GoogleTierType specifies the storage class for Google.
    'kGoogleStandard' indicates a tier type of Google properties.
    'kGoogleNearline' indicates a tier type of Google properties that is not
    accessed frequently.
    'kGoogleColdline' indicates a tier type of Google properties that is
    rarely
    accessed.
    'kGoogleRegional' indicates a tier type of Google properties that stores
    frequently accessed data in the same region.
    'kGoogleMultiRegional' indicates a tier type of Google properties that is
    frequently accessed ("hot" objects) around the world.

    Attributes:
        KGOOGLESTANDARD: TODO: type description here.
        KGOOGLENEARLINE: TODO: type description here.
        KGOOGLECOLDLINE: TODO: type description here.
        KGOOGLEREGIONAL: TODO: type description here.
        KGOOGLEMULTIREGIONAL: TODO: type description here.

    """

    KGOOGLESTANDARD = 'kGoogleStandard'

    KGOOGLENEARLINE = 'kGoogleNearline'

    KGOOGLECOLDLINE = 'kGoogleColdline'

    KGOOGLEREGIONAL = 'kGoogleRegional'

    KGOOGLEMULTIREGIONAL = 'kGoogleMultiRegional'

