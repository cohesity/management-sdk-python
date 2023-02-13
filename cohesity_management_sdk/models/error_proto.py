# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ErrorProto(object):

    """Implementation of the 'ErrorProto' model.

    TODO: type model description here.

    Attributes:
        error_msg (string): An optional detail.
        mtype (int): Error.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "error_msg":'errorMsg',
        "mtype":'type'
    }

    def __init__(self,
                 error_msg=None,
                 mtype=None):
        """Constructor for the ErrorProto class"""

        # Initialize members of the class
        self.error_msg = error_msg
        self.mtype = mtype


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
        error_msg = dictionary.get('errorMsg')
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(error_msg,
                   mtype)


