# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.error_proto

class RunMapReduceInstanceResult(object):

    """Implementation of the 'RunMapReduceInstanceResult' model.

    Result of RunMapReduceInstance call.

    Attributes:
        error (ErrorProto): Status code of http rpc.
        map_reduce_instance_id (long|int): Return the ID of instance.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "error": 'error',
        "map_reduce_instance_id": 'mapReduceInstanceId'
    }

    def __init__(self,
                 error=None,
                 map_reduce_instance_id=None):
        """Constructor for the RunMapReduceInstanceResult class"""

        # Initialize members of the class
        self.error = error
        self.map_reduce_instance_id = map_reduce_instance_id


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
        error =  cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(dictionary.get('error')) if  dictionary.get('error') else None
        map_reduce_instance_id = dictionary.get('mapReduceInstanceId')

        # Return an object of this model
        return cls(error,
                   map_reduce_instance_id)


