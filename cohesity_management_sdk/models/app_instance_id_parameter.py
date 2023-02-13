# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class AppInstanceIdParameter(object):

    """Implementation of the 'AppInstanceIdParameter' model.

    AppInstanceIdParameter specifies app instance Id in path parameter.

    Attributes:
    app_instance_id (int|long): Specifies the app instance Id.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "app_instance_id":'appInstanceId'
    }

    def __init__(self,
                 app_instance_id=None):
        """Constructor for the AppInstanceIdParameter class"""

        # Initialize members of the class
        self.app_instance_id = app_instance_id


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
        app_instance_id = dictionary.get('appInstanceId')

        # Return an object of this model
        return cls(app_instance_id)


