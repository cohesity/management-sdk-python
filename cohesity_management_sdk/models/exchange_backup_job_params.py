# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ExchangeBackupJobParams(object):

    """Implementation of the 'ExchangeBackupJobParams' model.

    Message to capture additional backup job params specific to Exchange.

    Attributes:
        is_copy_only_full (bool): Whether the backups should be copy-only.
            If this is set to true, then Exchange server will not truncate
            logs after backup.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "is_copy_only_full": 'isCopyOnlyFull'
    }

    def __init__(self,
                 is_copy_only_full=None):
        """Constructor for the ExchangeBackupJobParams class"""

        # Initialize members of the class
        self.is_copy_only_full = is_copy_only_full


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
        is_copy_only_full = dictionary.get('isCopyOnlyFull')

        # Return an object of this model
        return cls(is_copy_only_full)


