# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class K8SFilterParams_LabelVec(object):

    """Implementation of the 'K8SFilterParams_LabelVec' model.

    Represents a list of all Label entity IDs that need to be present to create
    a positive match for the candidate volume to include.


    Attributes:

        label_vec (list of long|int): Represents a list of all Labels that need
            to be present to create a positive match for the candidate volume
            to include.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "label_vec":'labelVec',
    }
    def __init__(self,
                 label_vec=None,
            ):

        """Constructor for the K8SFilterParams_LabelVec class"""

        # Initialize members of the class
        self.label_vec = label_vec

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
        label_vec = dictionary.get("labelVec")

        # Return an object of this model
        return cls(
            label_vec
)