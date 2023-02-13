# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.app_instance_settings

class UpdateAppInstanceSettingsParameters(object):

    """Implementation of the 'UpdateAppInstanceSettingsParameters' model.

    Specifies update app instance settings parameters.

    Attributes:
        description (string): Description of the app instance.
        settings (AppInstanceSettings): Specifies the desired app instance
            settings.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description": 'description',
        "settings": 'settings'
    }

    def __init__(self,
                 description=None,
                 settings=None):
        """Constructor for the UpdateAppInstanceSettingsParameters class"""

        # Initialize members of the class
        self.description = description
        self.settings = settings


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
        description = dictionary.get('description')
        settings = cohesity_management_sdk.models.app_instance_settings.AppInstanceSettings.from_dictionary(dictionary.get('settings')) if  dictionary.get('settings') else None

        # Return an object of this model
        return cls(description,
                   settings)


