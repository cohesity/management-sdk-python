# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.uda_restore_object_params


class UdaRestoreObject(object):

    """Implementation of the 'UdaRestoreObject' model.

    TODO: type description here.


    Attributes:

        entity_id (long|int): Magneto Entity id. If this is set,
            object_name/object_uuid should be empty.
        object_name (string): The original name of the object to be restored.
        object_uuid (string): The UUID of the object to be restored.
        restore_params (UdaRestoreObjectParams): The specific params related to
            the object to be restored.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "entity_id":'entityId',
        "object_name":'objectName',
        "object_uuid":'objectUuid',
        "restore_params":'restoreParams',
    }
    def __init__(self,
                 entity_id=None,
                 object_name=None,
                 object_uuid=None,
                 restore_params=None,
            ):

        """Constructor for the UdaRestoreObject class"""

        # Initialize members of the class
        self.entity_id = entity_id
        self.object_name = object_name
        self.object_uuid = object_uuid
        self.restore_params = restore_params

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
        object_name = dictionary.get('objectName')
        object_uuid = dictionary.get('objectUuid')
        restore_params = cohesity_management_sdk.models.uda_restore_object_params.UdaRestoreObjectParams.from_dictionary(dictionary.get('restoreParams')) if dictionary.get('restoreParams') else None

        # Return an object of this model
        return cls(
            entity_id,
            object_name,
            object_uuid,
            restore_params
)