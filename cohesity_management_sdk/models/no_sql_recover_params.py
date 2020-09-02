# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.no_sql_restore_object

class NoSqlRecoverParams(object):

    """Implementation of the 'NoSqlRecoverParams' model.

    TODO: Type model description here.

    Attributes:
        restore_objects (list of NoSqlRestoreObject): TODO: Type description
            here.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "restore_objects":'restoreObjects'
    }

    def __init__(self,
                 restore_objects=None):
        """Constructor for the NoSqlRecoverParams class"""

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
                restore_objects.append(cohesity_management_sdk.models.no_sql_restore_object.NoSqlRestoreObject.from_dictionary(structure))

        # Return an object of this model
        return cls(restore_objects)


