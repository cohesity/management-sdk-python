# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ServerTypeEnum(object):

    """Implementation of the 'ServerType' enum.
    Specifies the type of key mangement system. 'kInternalKMS' indicates an
    internal KMS object. 'kAwsKMS' indicates an Aws KMS object. 'kCryptsoftKMS'
    indicates a Cryptsoft KMS object. 'kAzureKMS' indicates a Azure KMS object.


    Attributes:
        KINTERNALKMS: TODO: type description here.
        KAWSKMS: TODO: type description here.
        KCRYPTSOFTKMS: TODO: type description here.
        KAZUREKMS: TODO: type description here.

    """

    KINTERNALKMS = 'kInternalKMS'

    KAWSKMS = 'kAwsKMS'

    KCRYPTSOFTKMS = 'kCryptsoftKMS'

    KAZUREKMS = 'kAzureKMS'
