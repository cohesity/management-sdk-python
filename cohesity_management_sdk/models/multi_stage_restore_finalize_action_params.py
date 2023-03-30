# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class MultiStageRestoreFinalizeActionParams(object):

    """Implementation of the 'MultiStageRestoreFinalizeActionParams' model.

    MultiStageRestoreFinalizeActionParams holds the parameters required for
    finalizing a multi-stage restore task.


    Attributes:

        power_on_target (bool): Specifies the power state of the recovered
            object at the end of the multi-stage restore.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "power_on_target":'powerOnTarget',
    }
    def __init__(self,
                 power_on_target=None,
            ):

        """Constructor for the MultiStageRestoreFinalizeActionParams class"""

        # Initialize members of the class
        self.power_on_target = power_on_target

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
        power_on_target = dictionary.get('powerOnTarget')

        # Return an object of this model
        return cls(
            power_on_target
)