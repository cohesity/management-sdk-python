# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class PutLinuxSupportUser2FAParamsWithTOTP(object):

    """Implementation of the 'PutLinuxSupportUser2FAParamsWithTOTP' model.

    IRIS will then send that information to the nexus to program in the
    backend.


    Attributes:

        totp_q_r_url (string): TODO: Type description here.
        totp_secret_key (string): TODO: Type description here.
        two_fa_mode (long|int): Value 0 means disable the 2FA. i.e., Password
            only authentication. Value 1 means TOTP 2FA. If the TOTP 2FA has
            already been configured then it'll be re-keyed. Value 2 means Email
            2FA. Request should have Email ID (or) The backend should already
            have the Email ID configured.
        email_id (string): Specify Email ID for the Email based OTP.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "totp_q_r_url":'TOTPQRUrl',
        "totp_secret_key":'TOTPSecretKey',
        "two_fa_mode":'TwoFAMode',
        "email_id":'emailID',
    }
    def __init__(self,
                 totp_q_r_url=None,
                 totp_secret_key=None,
                 two_fa_mode=None,
                 email_id=None,
            ):

        """Constructor for the PutLinuxSupportUser2FAParamsWithTOTP class"""

        # Initialize members of the class
        self.totp_q_r_url = totp_q_r_url
        self.totp_secret_key = totp_secret_key
        self.two_fa_mode = two_fa_mode
        self.email_id = email_id

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
        totp_q_r_url = dictionary.get('TOTPQRUrl')
        totp_secret_key = dictionary.get('TOTPSecretKey')
        two_fa_mode = dictionary.get('TwoFAMode')
        email_id = dictionary.get('emailID')

        # Return an object of this model
        return cls(
            totp_q_r_url,
            totp_secret_key,
            two_fa_mode,
            email_id
)