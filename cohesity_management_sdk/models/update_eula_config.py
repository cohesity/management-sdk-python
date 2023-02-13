# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class UpdateEulaConfig(object):

    """Implementation of the 'UpdateEulaConfig' model.

    Specifies the update to the End User License Agreement information.

    Attributes:
        signed_version (long|int): Specifies the version of the End User
            License Agreement that was accepted.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "signed_version":'signedVersion'
    }

    def __init__(self,
                 signed_version=None):
        """Constructor for the UpdateEulaConfig class"""

        # Initialize members of the class
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
        signed_version = dictionary.get('signedVersion')

        # Return an object of this model
        return cls(signed_version)


