# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class EncryptionPolicyEnum(object):

    """Implementation of the 'EncryptionPolicy' enum.

    Specifies the encryption setting for the Storage Domain (View Box).
    'kEncryptionNone' indicates the data is not encrypted.
    'kEncryptionStrong' indicates the data is encrypted.

    Attributes:
        KENCRYPTIONNONE: TODO: type description here.
        KENCRYPTIONSTRONG: TODO: type description here.
        KENCRYPTIONWEAK: TODO: type description here.

    """

    KENCRYPTIONNONE = 'kEncryptionNone'

    KENCRYPTIONSTRONG = 'kEncryptionStrong'

    KENCRYPTIONWEAK = 'kEncryptionWeak'

