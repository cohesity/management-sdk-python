# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.reducer_info

class ReducersWrapper(object):

    """Implementation of the 'ReducersWrapper' model.

    ReducersWrapper is the struct to define the list of reducers.

    Attributes:
        reducers (list of ReducerInfo): Reducers specifies the list of
            available reducers in analytics workbench.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "reducers":'reducers'
    }

    def __init__(self,
                 reducers=None):
        """Constructor for the ReducersWrapper class"""

        # Initialize members of the class
        self.reducers = reducers


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
        reducer_list = None
        if dictionary.get('reducers', None) != None:
            reducer_list = list()
            for reducer in dictionary.get('reducers'):
                reducer_list.append(cohesity_management_sdk.models.reducer_info.ReducerInfo.from_dictionary(reducer))

        # Return an object of this model
        return cls(reducer_list)


