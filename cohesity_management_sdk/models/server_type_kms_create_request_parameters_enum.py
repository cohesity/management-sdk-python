# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

class ServerTypeKmsCreateRequestParametersEnum(object):

    """Implementation of the 'ServerType_KmsCreateRequestParameters' enum.

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

