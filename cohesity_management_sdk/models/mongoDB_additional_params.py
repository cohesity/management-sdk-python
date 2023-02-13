# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class MongoDBAdditionalParams(object):

    """Implementation of the 'MongoDBAdditionalParams' model.

    Contains additional  parameters required for taking backup from
    this Mongo cluster.

    Attributes:
    secondary_node_tag (list of string): The tag associated with the
        secondary nodes from which backups should be performed.
    use_secondary_for_backup (bool): Set to true if this cluster uses
        secondary nodes for backup.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "secondary_node_tag": 'secondaryNodeTag',
        "use_secondary_for_backup": 'useSecondaryForBackup'
    }

    def __init__(self,
                 secondary_node_tag=None,
                 use_secondary_for_backup=None):
        """Constructor for the MongoDBAdditionalParams class"""

        # Initialize members of the class
        self.secondary_node_tag = secondary_node_tag
        self.use_secondary_for_backup = use_secondary_for_backup


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
        secondary_node_tag = dictionary.get('secondaryNodeTag')
        use_secondary_for_backup = dictionary.get('useSecondaryForBackup')

        # Return an object of this model
        return cls(secondary_node_tag,
                   use_secondary_for_backup)


