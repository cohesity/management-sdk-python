# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ExchangeEnvJobParameters(object):

    """Implementation of the 'ExchangeEnvJobParameters' model.

    Specifies job parameters applicable for the Exchange Protection Jobs.

    Attributes:
    backups_copy_only (bool): Specifies whether the backups should be
        copy-only.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "backups_copy_only": 'backupsCopyOnly'
    }

    def __init__(self,
                 backups_copy_only=None):
        """Constructor for the ExchangeEnvJobParameters class"""

        # Initialize members of the class
        self.backups_copy_only = backups_copy_only


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
        backups_copy_only = dictionary.get('backupsCopyOnly')

        # Return an object of this model
        return cls(backups_copy_only)


