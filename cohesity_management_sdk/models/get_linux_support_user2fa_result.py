# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class GetLinuxSupportUser2FAResult(object):

    """Implementation of the 'GetLinuxSupportUser2FAResult' model.

    TODO: type description here.


    Attributes:

        email_id (string): TODO: Type description here.
        totp_q_r_code_url (string): TODO: Type description here.
        totp_secret_key (string): TODO: Type description here.
        two_fa_mode (long|int): TODO: Type description here.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "email_id":'EmailID',
        "totp_q_r_code_url":'TOTPQRCodeUrl',
        "totp_secret_key":'TOTPSecretKey',
        "two_fa_mode":'TwoFAMode',
    }
    def __init__(self,
                 email_id=None,
                 totp_q_r_code_url=None,
                 totp_secret_key=None,
                 two_fa_mode=None,
            ):

        """Constructor for the GetLinuxSupportUser2FAResult class"""

        # Initialize members of the class
        self.email_id = email_id
        self.totp_q_r_code_url = totp_q_r_code_url
        self.totp_secret_key = totp_secret_key
        self.two_fa_mode = two_fa_mode

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
        email_id = dictionary.get('EmailID')
        totp_q_r_code_url = dictionary.get('TOTPQRCodeUrl')
        totp_secret_key = dictionary.get('TOTPSecretKey')
        two_fa_mode = dictionary.get('TwoFAMode')

        # Return an object of this model
        return cls(
            email_id,
            totp_q_r_code_url,
            totp_secret_key,
            two_fa_mode
)