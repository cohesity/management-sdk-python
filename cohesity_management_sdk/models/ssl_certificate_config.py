# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class SslCertificateConfig(object):

    """Implementation of the 'SslCertificateConfig' model.

    SslCertificateConfig represents the SSL certificate object exposed to the
    user.

    Attributes:
        certificate (string): Certificate is a SSL certificate used by Iris
            HTTPS webserver.
        last_update_time_msecs (long|int): LastUpdateTimeMsecs is a time in
            milliseconds at which certificate was last updated.
        private_key (string): PrivateKey is a matching private key of the
            above certificate.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "certificate":'certificate',
        "last_update_time_msecs":'lastUpdateTimeMsecs',
        "private_key":'privateKey'
    }

    def __init__(self,
                 certificate=None,
                 last_update_time_msecs=None,
                 private_key=None):
        """Constructor for the SslCertificateConfig class"""

        # Initialize members of the class
        self.certificate = certificate
        self.last_update_time_msecs = last_update_time_msecs
        self.private_key = private_key


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
        certificate = dictionary.get('certificate')
        last_update_time_msecs = dictionary.get('lastUpdateTimeMsecs')
        private_key = dictionary.get('privateKey')

        # Return an object of this model
        return cls(certificate,
                   last_update_time_msecs,
                   private_key)


