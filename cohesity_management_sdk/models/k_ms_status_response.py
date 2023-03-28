# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class KMSStatusResponse(object):

    """Implementation of the 'KMSStatusResponse' model.

    TODO: type description here.


    Attributes:

        status (bool): Specifies the status of the kms server. If true,
            indicates KMS sever is reachable.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "status":'status',
    }
    def __init__(self,
                 status=None,
            ):

        """Constructor for the KMSStatusResponse class"""

        # Initialize members of the class
        self.status = status

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
        status = dictionary.get('status')

        # Return an object of this model
        return cls(
            status
)