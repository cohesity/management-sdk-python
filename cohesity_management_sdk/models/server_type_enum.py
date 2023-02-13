# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ServerTypeEnum(object):

    """Implementation of the 'ServerType' enum.

    Specifies the type of key mangement system.
    'kInternalKms' indicates an internal KMS object.
    'kAwsKms' indicates an Aws KMS object.
    'kCryptsoftKms' indicates a Cryptsoft KMS object.

    Attributes:
        KINTERNALKMS: TODO: type description here.
        KAWSKMS: TODO: type description here.
        KCRYPTSOFTKMS: TODO: type description here.

    """

    KINTERNALKMS = 'kInternalKms'

    KAWSKMS = 'kAwsKms'

    KCRYPTSOFTKMS = 'kCryptsoftKms'

