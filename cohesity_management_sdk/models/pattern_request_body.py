# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.supported_pattern

class PatternRequestBody(object):

    """Implementation of the 'Pattern Request Body.' model.

    Specifies details about the pattern which has to be saved.

    Attributes:
        application_data_type (int): Specifies the data type for which
            suppprted patterns can be fetched.
        application_id (long|int): Specifies AWB Application ID.
        user_pattern (SupportedPattern): Specifies details of the pattern
            available for search available in an application such as Pattern
            Finder within Analytics Work Bench.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "application_data_type":'applicationDataType',
        "application_id":'applicationId',
        "user_pattern":'userPattern'
    }

    def __init__(self,
                 application_data_type=None,
                 application_id=None,
                 user_pattern=None):
        """Constructor for the PatternRequestBody class"""

        # Initialize members of the class
        self.application_data_type = application_data_type
        self.application_id = application_id
        self.user_pattern = user_pattern


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
        application_data_type = dictionary.get('applicationDataType')
        application_id = dictionary.get('applicationId')
        user_pattern = cohesity_management_sdk.models.supported_pattern.SupportedPattern.from_dictionary(dictionary.get('userPattern')) if dictionary.get('userPattern') else None

        # Return an object of this model
        return cls(application_data_type,
                   application_id,
                   user_pattern)


