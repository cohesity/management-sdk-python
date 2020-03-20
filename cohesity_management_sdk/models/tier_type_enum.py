# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

class TierTypeEnum(object):

    """Implementation of the 'TierType' enum.

    Specifies the storage class of AWS.
    AmazonTierType specifies the storage class for AWS.
    'kAmazonS3Standard' indicates a tier type of Amazon properties that is
    accessed frequently.
    'kAmazonS3StandardIA' indicates a tier type of Amazon properties that is
    accessed less frequently, but requires rapid access when needed.
    'kAmazonGlacier' indicates a tier type of Amazon properties that is
    accessed
    rarely.
    'kAmazonS3OneZoneIA' indicates a tier type of Amazon properties for
    long-lived, but less frequently accessed data.
    'kAmazonS3IntelligentTiering' indicates a tier type of Amazon properties
    for
    data with unknown or changing access patterns.

    Attributes:
        KAMAZONS3STANDARD: TODO: type description here.
        KAMAZONS3STANDARDIA: TODO: type description here.
        KAMAZONGLACIER: TODO: type description here.
        KAMAZONS3ONEZONEIA: TODO: type description here.
        KAMAZONS3INTELLIGENTTIERING: TODO: type description here.

    """

    KAMAZONS3STANDARD = 'kAmazonS3Standard'

    KAMAZONS3STANDARDIA = 'kAmazonS3StandardIA'

    KAMAZONGLACIER = 'kAmazonGlacier'

    KAMAZONS3ONEZONEIA = 'kAmazonS3OneZoneIA'

    KAMAZONS3INTELLIGENTTIERING = 'kAmazonS3IntelligentTiering'

