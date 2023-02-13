# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class EncryptionConfiguration(object):

    """Implementation of the 'EncryptionConfiguration' model.

    Specifies the parameters the user wants to use when configuring
    encryption
    for the new Cluster.

    Attributes:
        enable_encryption (bool): Specifies whether or not to enable
            encryption. If encryption is enabled, all data on the Cluster will
            be encrypted. This can only be enabled at Cluster creation time
            and cannot be disabled later.
        enable_fips_mode (bool): Specifies whether or not to enable FIPS mode.
            EnableEncryption must be set to true in order to enable FIPS.
        rotation_period (int): Specifies the rotation period for encryption
            keys in days.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enable_encryption":'enableEncryption',
        "enable_fips_mode":'enableFipsMode',
        "rotation_period":'rotationPeriod'
    }

    def __init__(self,
                 enable_encryption=None,
                 enable_fips_mode=None,
                 rotation_period=None):
        """Constructor for the EncryptionConfiguration class"""

        # Initialize members of the class
        self.enable_encryption = enable_encryption
        self.enable_fips_mode = enable_fips_mode
        self.rotation_period = rotation_period


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
        enable_encryption = dictionary.get('enableEncryption')
        enable_fips_mode = dictionary.get('enableFipsMode')
        rotation_period = dictionary.get('rotationPeriod')

        # Return an object of this model
        return cls(enable_encryption,
                   enable_fips_mode,
                   rotation_period)


