# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class PutLinuxSupportUser2FAResult(object):

    """Implementation of the 'PutLinuxSupportUser2FAResult' model.

    IRIS will then send that information to the nexus to program
    in the backend.

    Attributes:
        email_id (string): TODO: Type Description here.
        to_tp_qr_url (string): TODO: Type Description here.
        to_tp_secret_key (string): TODO: Type Description here.
        two_fa_mode (long| int): Value 0 means disable the 2FA.
            i.e., Password only authentication.
            Value 1 means TOTP 2FA. If the TOTP 2FA has already been
            configured then it'll be re-keyed.
            Value 2 means Email 2FA.
            Request should have Email ID
            (or) The backend should already have the Email ID configured.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "email_id":'EmailID',
        "to_tp_qr_url":'TOTPQRUrl',
        "to_tp_secret_key":'TOTPSecretKey',
        "two_fa_mode":'TwoFAMode'
    }

    def __init__(self,
                 email_id=None,
                 to_tp_qr_url=None,
                 to_tp_secret_key=None,
                 two_fa_mode=None):
        """Constructor for the PutLinuxSupportUser2FAResult class"""

        # Initialize members of the class
        self.email_id = email_id
        self.to_tp_qr_url = to_tp_qr_url
        self.to_tp_secret_key = to_tp_secret_key
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
        to_tp_qr_url = dictionary.get('TOTPQRUrl')
        to_tp_secret_key = dictionary.get('TOTPSecretKey')
        two_fa_mode = dictionary.get('TwoFAMode')

        # Return an object of this model
        return cls(email_id,
                   to_tp_qr_url,
                   to_tp_secret_key,
                   two_fa_mode)


