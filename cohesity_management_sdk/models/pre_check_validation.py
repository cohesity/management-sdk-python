# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class PreCheckValidation(object):

    """Implementation of the 'PreCheckValidation' model.

    PreCheckValidation specifies the validations with the pass/fail status


    Attributes:

        is_passed (bool): IsPassed indicates validation passed or failed
        message (string): Message specifies the validation failure message
        validation (string): Validation specifies the type of validation
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "is_passed":'isPassed',
        "message":'message',
        "validation":'validation',
    }
    def __init__(self,
                 is_passed=None,
                 message=None,
                 validation=None,
            ):

        """Constructor for the PreCheckValidation class"""

        # Initialize members of the class
        self.is_passed = is_passed
        self.message = message
        self.validation = validation

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
        is_passed = dictionary.get('isPassed')
        message = dictionary.get('message')
        validation = dictionary.get('validation')

        # Return an object of this model
        return cls(
            is_passed,
            message,
            validation
)