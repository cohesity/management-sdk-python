# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.pattern

class MapReduceAuxData(object):

    """Implementation of the 'MapReduceAuxData' model.

    This message encapsulates auxillary data for a MapReduce. One example of
    such data is saved patterns for Pattern finder app.

    Attributes:
        pattern_vec (list of Pattern): Pattern auxiliary data for a
            MapReduce.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "pattern_vec":'patternVec'
    }

    def __init__(self,
                 pattern_vec=None):
        """Constructor for the MapReduceAuxData class"""

        # Initialize members of the class
        self.pattern_vec = pattern_vec


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
        pattern_vec = None
        if dictionary.get('patternVec') != None:
            pattern_vec = list()
            for structure in dictionary.get('patternVec'):
                pattern_vec.append(cohesity_management_sdk.models.pattern.Pattern.from_dictionary(structure))

        # Return an object of this model
        return cls(pattern_vec)


