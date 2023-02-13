# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class SnapshotLabel(object):

    """Implementation of the 'SnapshotLabel' model.

    Specifies the snapshot label for incremental and full backup
    of Secondary Netapp volumes (Data-Protect Volumes).

    Attributes:
        full_label (string): Specifies the full snapshot label value
        incremental_label (string) Specifies the incremental snapshot label
            value

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "full_label": 'fullLabel',
        "incremental_label": 'incrementalLabel'
    }

    def __init__(self,
                 full_label=None,
                 incremental_label=None):
        """Constructor for the SnapshotLabel class"""

        # Initialize members of the class
        self.full_label = full_label
        self.incremental_label = incremental_label


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
        full_label = dictionary.get('fullLabel', None)
        incremental_label = dictionary.get('incrementalLabel', None)

        # Return an object of this model
        return cls(full_label,
                   incremental_label)


