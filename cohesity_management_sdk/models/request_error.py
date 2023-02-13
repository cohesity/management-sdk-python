# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class RequestError(object):

    """Implementation of the 'RequestError' model.

    Details about the Error.

    Attributes:
        error_code (long|int): Operation response error code.
        message (string): Description of the error.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "error_code":'errorCode',
        "message":'message'
    }

    def __init__(self,
                 error_code=None,
                 message=None):
        """Constructor for the RequestError class"""

        # Initialize members of the class
        self.error_code = error_code
        self.message = message


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
        error_code = dictionary.get('errorCode')
        message = dictionary.get('message')

        # Return an object of this model
        return cls(error_code,
                   message)


