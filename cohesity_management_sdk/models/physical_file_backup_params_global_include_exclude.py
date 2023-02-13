# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class PhysicalFileBackupParams_GlobalIncludeExclude(object):

    """Implementation of the 'PhysicalFileBackupParams_GlobalIncludeExclude'
    model.

    Descibes job level includes and excludes. Right now, only supports
    excludes but includes will be added in future.

    Attributes:
    exclude_vec (list of string): Describes exclude vec at job level used in
        combination with to exclude_paths to exclude files.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "exclude_vec":'excludeVec'
    }

    def __init__(self,
                 exclude_vec=None):
        """Constructor for the PhysicalFileBackupParams_GlobalIncludeExclude
        class"""

        # Initialize members of the class
        self.exclude_vec = exclude_vec


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        exclude_vec = dictionary.get('excludeVec')

        # Return an object of this model
        return cls(exclude_vec)


