# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class VaultParamsRestoreParamsGlacier(object):

    """Implementation of the 'VaultParams_RestoreParams_Glacier' model.

    TODO: type model description here.

    Attributes:
        retrieval_type (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "retrieval_type":'retrievalType'
    }

    def __init__(self,
                 retrieval_type=None):
        """Constructor for the VaultParamsRestoreParamsGlacier class"""

        # Initialize members of the class
        self.retrieval_type = retrieval_type


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
        retrieval_type = dictionary.get('retrievalType')

        # Return an object of this model
        return cls(retrieval_type)


