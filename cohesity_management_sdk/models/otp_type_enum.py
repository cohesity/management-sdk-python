# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class OtpTypeEnum(object):

    """Implementation of the 'OtpType' enum.

    Specifies OTP type.
    'Totp' implies the code is TOTP.
    'Email' implies the code is email OTP.

    Attributes:
        TOTP: TODO: type description here.
        EMAIL: TODO: type description here.

    """

    TOTP = 'Totp'

    EMAIL = 'Email'
