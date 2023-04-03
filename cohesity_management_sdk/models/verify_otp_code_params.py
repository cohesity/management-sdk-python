# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class VerifyOtpCodeParams(object):

    """Implementation of the 'VerifyOtpCodeParams' model.

    Specifies the parameters to verify OTP code.


    Attributes:

        otp_code (string, required): Specifies the OTP code.
        otp_type (OtpTypeEnum): Specifies OTP type. 'Totp' implies the code is
            TOTP. 'Email' implies the code is email OTP.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "otp_code":'otpCode',
        "otp_type":'otpType',
    }
    def __init__(self,
                 otp_code=None,
                 otp_type=None,
            ):

        """Constructor for the VerifyOtpCodeParams class"""

        # Initialize members of the class
        self.otp_code = otp_code
        self.otp_type = otp_type

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        otp_code = dictionary.get('otpCode')
        otp_type = dictionary.get('otpType')

        # Return an object of this model
        return cls(
            otp_code,
            otp_type
)