# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class CloneAppViewInfoOracle(object):

    """Implementation of the 'CloneAppViewInfoOracle' model.

    This message encapsulates backup view Clone operation information of a
    Oracle DB.

    Attributes:
        mount_path_info_vec (list of string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mount_path_info_vec":'mountPathInfoVec'
    }

    def __init__(self,
                 mount_path_info_vec=None):
        """Constructor for the CloneAppViewInfoOracle class"""

        # Initialize members of the class
        self.mount_path_info_vec = mount_path_info_vec


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
        mount_path_info_vec = dictionary.get('mountPathInfoVec')

        # Return an object of this model
        return cls(mount_path_info_vec)


