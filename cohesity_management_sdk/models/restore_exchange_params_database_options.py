# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class RestoreExchangeParams_DatabaseOptions(object):

    """Implementation of the 'RestoreExchangeParams_DatabaseOptions' model.

    Attributes:
        entity_id (int): The windows machine to which the
            database will be restored.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "entity_id":'entityId'
    }

    def __init__(self,
                 entity_id=None):
        """Constructor for the RestoreExchangeParams_DatabaseOptions class"""

        # Initialize members of the class
        self.entity_id = entity_id


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
        entity_id = dictionary.get('entityId')

        # Return an object of this model
        return cls(entity_id)


