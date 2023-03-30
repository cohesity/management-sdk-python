# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class S3KeyMappingConfigEnum(object):

    """Implementation of the 'S3KeyMappingConfig' enum.

    Specifies the S3 key mapping config of the view. This parameter can only
    be set during create and cannot be changed.
    Configuration of S3 key mapping.
    Specifies the type of S3 key mapping config.

    Attributes:
        KRANDOM: TODO: type description here.
        KSHORT: TODO: type description here.
        KLONG: TODO: type description here.
        KHIERARCHICAL: TODO: type description here.

    """

    KRANDOM = 'kRandom'

    KSHORT = 'kShort'

    KLONG = 'kLong'

    KHIERARCHICAL = 'kHierarchical'

