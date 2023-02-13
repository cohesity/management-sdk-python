# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.restore_object
import cohesity_management_sdk.models.restore_object_params

class AppOwnerRestoreInfo(object):

    """Implementation of the 'AppOwnerRestoreInfo' model.

    TODO: type model description here.

    Attributes:
        owner_object (RestoreObject): TODO: type description here.
        owner_restore_params (RestoreObjectParams): TODO: type description
            here.
        perform_restore (bool): If this is set to true, then the owner object
            needs to be restored. The restore options that follow only apply
            if this field is set to true. If this field is not set, then the
            application objects will be restored to the original owner from
            where they were backed up.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "owner_object":'ownerObject',
        "owner_restore_params":'ownerRestoreParams',
        "perform_restore":'performRestore'
    }

    def __init__(self,
                 owner_object=None,
                 owner_restore_params=None,
                 perform_restore=None):
        """Constructor for the AppOwnerRestoreInfo class"""

        # Initialize members of the class
        self.owner_object = owner_object
        self.owner_restore_params = owner_restore_params
        self.perform_restore = perform_restore


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
        owner_object = cohesity_management_sdk.models.restore_object.RestoreObject.from_dictionary(dictionary.get('ownerObject')) if dictionary.get('ownerObject') else None
        owner_restore_params = cohesity_management_sdk.models.restore_object_params.RestoreObjectParams.from_dictionary(dictionary.get('ownerRestoreParams')) if dictionary.get('ownerRestoreParams') else None
        perform_restore = dictionary.get('performRestore')

        # Return an object of this model
        return cls(owner_object,
                   owner_restore_params,
                   perform_restore)


