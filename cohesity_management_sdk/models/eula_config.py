# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class EulaConfig(object):

    """Implementation of the 'EulaConfig' model.

    Specifies the End User License Agreement acceptance information.

    Attributes:
        license_key (string): Specifies the license key.
        signed_by_user (string): Specifies the login account name for the
            Cohesity user who accepted the End User License Agreement.
        signed_time (long|int): Specifies the time that the End User License
            Agreement was accepted.
        signed_version (long|int): Specifies the version of the End User
            License Agreement that was accepted.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "license_key":'licenseKey',
        "signed_version":'signedVersion',
        "signed_by_user":'signedByUser',
        "signed_time":'signedTime'
    }

    def __init__(self,
                 license_key=None,
                 signed_version=None,
                 signed_by_user=None,
                 signed_time=None):
        """Constructor for the EulaConfig class"""

        # Initialize members of the class
        self.license_key = license_key
        self.signed_by_user = signed_by_user
        self.signed_time = signed_time
        self.signed_version = signed_version


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
        license_key = dictionary.get('licenseKey')
        signed_version = dictionary.get('signedVersion')
        signed_by_user = dictionary.get('signedByUser')
        signed_time = dictionary.get('signedTime')

        # Return an object of this model
        return cls(license_key,
                   signed_version,
                   signed_by_user,
                   signed_time)


