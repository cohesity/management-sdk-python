# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class CloneAppViewParams(object):

    """Implementation of the 'CloneAppViewParams' model.

    This message encapsulates the generic information required for cloning
    and
    App view.

    Attributes:
        mount_path_identifier (string): Mount path identifier, which
            identifies the sub-dir where the cohesity view for App recovery
            will be mounted.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mount_path_identifier":'mountPathIdentifier'
    }

    def __init__(self,
                 mount_path_identifier=None):
        """Constructor for the CloneAppViewParams class"""

        # Initialize members of the class
        self.mount_path_identifier = mount_path_identifier


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
        mount_path_identifier = dictionary.get('mountPathIdentifier')

        # Return an object of this model
        return cls(mount_path_identifier)


