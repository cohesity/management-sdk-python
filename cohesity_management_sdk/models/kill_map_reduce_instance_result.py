# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.error_proto

class KillMapReduceInstanceResult(object):

    """Implementation of the 'KillMapReduceInstanceResult' model.

    Attributes:
    error (ErrorProto):  Status code of http rpc.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "error":'error'
    }

    def __init__(self,
                 error=None):
        """Constructor for the KillMapReduceInstanceResult class"""

        # Initialize members of the class
        self.error = error


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

        # Return an object of this model
        return cls(error)


