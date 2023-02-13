# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class SanEnvJobParameters(object):

    """Implementation of the 'SanEnvJobParameters' model.

    Specifies job parameters applicable for all SAN Environment types
    Protection Sources in a Protection Job.

    Attributes:
        max_snapshots_on_primary (long|int): Specifies how many recent
            snapshots of each backed up entity to retain on the primary
            environment. If not specified, then snapshots will not be be
            deleted from the primary environment.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "max_snapshots_on_primary":'maxSnapshotsOnPrimary'
    }

    def __init__(self,
                 max_snapshots_on_primary=None):
        """Constructor for the SanEnvJobParameters class"""

        # Initialize members of the class
        self.max_snapshots_on_primary = max_snapshots_on_primary


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
        max_snapshots_on_primary = dictionary.get('maxSnapshotsOnPrimary')

        # Return an object of this model
        return cls(max_snapshots_on_primary)


