# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.error_proto

class AnalyseJarResult(object):

    """Implementation of the 'AnalyseJarResult' model.

    Attributes:
        error (ErrorProto): Status code of http rpc.
        mappers (list of string): Name of all mapper classes found in jar
            file.
        reducers (list of string): Name of all reducers classes found in jar
            file.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "error":'error',
        "mappers":'mappers',
        "reducers":'reducers'
    }

    def __init__(self,
                 error=None,
                 mappers=None,
                 reducers=None):
        """Constructor for the AnalyseJarResult class"""

        # Initialize members of the class
        self.error = error
        self.mappers = mappers
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
        error = cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(dictionary.get('error')) if dictionary.get('error') else None
        mappers = dictionary.get('mappers')
        reducers = dictionary.get('reducers')

        # Return an object of this model
        return cls(error,
                   mappers,
                   reducers)


