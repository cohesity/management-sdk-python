# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.mongoDB_additional_params

class MongoDBBackupJobParams(object):

    """Implementation of the 'MongoDBBackupJobParams' model.

    Contains any additional mongodb environment specific backup params at the
    job level.

    Attributes:
        mongodb_aditional_info (MongoDBAdditionalParams): Additional parameters
            required for Mongo backup
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mongodb_aditional_info":'mongodbAdditionalInfo'
    }

    def __init__(self,
                 mongodb_aditional_info=None):
        """Constructor for the MongoDBBackupJobParams class"""

        # Initialize members of the class
        self.mongodb_aditional_info = mongodb_aditional_info


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
        mongodb_aditional_info = cohesity_management_sdk.models.mongoDB_additional_params.MongoDBAdditionalParams.from_dictionary(dictionary.get('mongodbAdditionalInfo')) if dictionary.get('mongodbAdditionalInfo') else None

        # Return an object of this model
        return cls(mongodb_aditional_info)


