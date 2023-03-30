# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.sfdc_restore_object


class SfdcRecoverParams(object):

    """Implementation of the 'SfdcRecoverParams' model.

    TODO: type description here.


    Attributes:

        restore_objects (list of SfdcRestoreObject): TODO: Type description
            here.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "restore_objects":'restoreObjects',
    }
    def __init__(self,
                 restore_objects=None,
            ):

        """Constructor for the SfdcRecoverParams class"""

        # Initialize members of the class
        self.restore_objects = restore_objects

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
        restore_objects = None
        if dictionary.get('restoreObjects') != None:
            restore_objects = list()
            for structure in dictionary.get('restoreObjects'):
                restore_objects.append(cohesity_management_sdk.models.sfdc_restore_object.SfdcRestoreObject.from_dictionary(structure))

        # Return an object of this model
        return cls(
            restore_objects
)