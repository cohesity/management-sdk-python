# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class SharepointBackupSourceParams(object):

    """Implementation of the 'SharepointBackupSourceParams' model.

    TODO: type description here.


    Attributes:

        autoprotect_entity (bool): Specifies to whether autoprotect the site
            entity  or not. If this is set to true, the site entity and
            subsites of it are protected. If this is set to false, only the
            site entity is protected.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "autoprotect_entity":'autoprotectEntity',
    }
    def __init__(self,
                 autoprotect_entity=None,
            ):

        """Constructor for the SharepointBackupSourceParams class"""

        # Initialize members of the class
        self.autoprotect_entity = autoprotect_entity

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
        autoprotect_entity = dictionary.get('autoprotectEntity')

        # Return an object of this model
        return cls(
            autoprotect_entity
)