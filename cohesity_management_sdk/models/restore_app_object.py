# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.restore_task_additional_params
import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.restore_app_object_params

class RestoreAppObject(object):

    """Implementation of the 'RestoreAppObject' model.

    Message that captures information about an application object being
    restored.

    Attributes:
        additional_params (RestoreTaskAdditionalParams): Any additional
            parameters associated with a restore task.
        app_entity (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        display_name (string): The proper display name of this object in the
            UI, if app_entity is not empty. For example, for SQL databases the
            name should also include the instance name.
        restore_params (RestoreAppObjectParams): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "additional_params":'additionalParams',
        "app_entity":'appEntity',
        "display_name":'displayName',
        "restore_params":'restoreParams'
    }

    def __init__(self,
                 additional_params=None,
                 app_entity=None,
                 display_name=None,
                 restore_params=None):
        """Constructor for the RestoreAppObject class"""

        # Initialize members of the class
        self.additional_params = additional_params
        self.app_entity = app_entity
        self.display_name = display_name
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
        additional_params = cohesity_management_sdk.models.restore_task_additional_params.RestoreTaskAdditionalParams.from_dictionary(dictionary.get('additionalParams')) if dictionary.get('additionalParams') else None
        app_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('appEntity')) if dictionary.get('appEntity') else None
        display_name = dictionary.get('displayName')
        restore_params = cohesity_management_sdk.models.restore_app_object_params.RestoreAppObjectParams.from_dictionary(dictionary.get('restoreParams')) if dictionary.get('restoreParams') else None

        # Return an object of this model
        return cls(additional_params,
                   app_entity,
                   display_name,
                   restore_params)


