# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class SslVerification(object):

    """Implementation of the 'SslVerification' model.

    Specifies information about SSL verification when registering certain
    sources.

    Attributes:
        ca_certificate (string): Contains the contents of CA cert/cert chain.
        is_enabled (bool): Whether SSL verification should be performed.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ca_certificate":'caCertificate',
        "is_enabled":'isEnabled'
    }

    def __init__(self,
                 ca_certificate=None,
                 is_enabled=None):
        """Constructor for the SslVerification class"""

        # Initialize members of the class
        self.ca_certificate = ca_certificate
        self.is_enabled = is_enabled


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
        ca_certificate = dictionary.get('caCertificate')
        is_enabled = dictionary.get('isEnabled')

        # Return an object of this model
        return cls(ca_certificate,
                   is_enabled)


