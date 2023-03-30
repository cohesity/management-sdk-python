# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class MfaInfo(object):

    """Implementation of the 'MfaInfo' model.

    Specifies information about MFA.


    Attributes:

        is_email_otp_setup_done (bool): Specifies if email OTP setup is done on
            the user.
        is_totp_setup_done (bool): Specifies if TOTP setup is done on the user.
        is_user_exempt_from_mfa (bool): Specifies if MFA is disabled on the
            user.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "is_email_otp_setup_done":'isEmailOtpSetupDone',
        "is_totp_setup_done":'isTotpSetupDone',
        "is_user_exempt_from_mfa":'isUserExemptFromMfa',
    }
    def __init__(self,
                 is_email_otp_setup_done=None,
                 is_totp_setup_done=None,
                 is_user_exempt_from_mfa=None,
            ):

        """Constructor for the MfaInfo class"""

        # Initialize members of the class
        self.is_email_otp_setup_done = is_email_otp_setup_done
        self.is_totp_setup_done = is_totp_setup_done
        self.is_user_exempt_from_mfa = is_user_exempt_from_mfa

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
        is_email_otp_setup_done = dictionary.get('isEmailOtpSetupDone')
        is_totp_setup_done = dictionary.get('isTotpSetupDone')
        is_user_exempt_from_mfa = dictionary.get('isUserExemptFromMfa')

        # Return an object of this model
        return cls(
            is_email_otp_setup_done,
            is_totp_setup_done,
            is_user_exempt_from_mfa
)