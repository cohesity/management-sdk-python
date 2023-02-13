# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class UpdateAppInstanceStateParameters(object):

    """Implementation of the 'UpdateAppInstanceStateParameters' model.

    Specifies update app instance state parameters.

    Attributes:
        state (StateUpdateAppInstanceStateParametersEnum):
            Specifies the desired app instance state type.
            Specifies operational status of an app instance.
            kInitializing - The app instance has been launched or resumed,
            but is not fully running yet.
            kRunning - The app instance is running. Check health_status for
            the actual health.
            kPausing - The app instance is being paused.
            kPaused - The app instance has been paused.
            kTerminating - The app instance is being terminated.
            kTerminated -  The app instance has been terminated.
            kFailed - The app instance has failed due to an unrecoverable error.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "state":'state'
    }

    def __init__(self,
                 state=None):
        """Constructor for the UpdateAppInstanceStateParameters class"""

        # Initialize members of the class
        self.state = state


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
        state = dictionary.get('state')

        # Return an object of this model
        return cls(state)


