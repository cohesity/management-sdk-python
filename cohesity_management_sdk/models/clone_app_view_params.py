# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class CloneAppViewParams(object):

    """Implementation of the 'CloneAppViewParams' model.

    This message encapsulates the generic information required for cloning
    and
    App view.

    Attributes:
        mount_path_identifier (string): Mount path identifier, which
            identifies the sub-dir where the cohesity view for App recovery
            will be mounted.
        read_only_view_expose (bool): Read only view expose param, if this is
            set, the expose view will be mounted with read only.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mount_path_identifier":'mountPathIdentifier',
        "read_only_view_expose":'readOnlyViewExpose'
    }

    def __init__(self,
                 mount_path_identifier=None,
                 read_only_view_expose=None):
        """Constructor for the CloneAppViewParams class"""

        # Initialize members of the class
        self.mount_path_identifier = mount_path_identifier
        self.read_only_view_expose = read_only_view_expose


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
        read_only_view_expose = dictionary.get('readOnlyViewExpose')

        # Return an object of this model
        return cls(mount_path_identifier,
                   read_only_view_expose)


