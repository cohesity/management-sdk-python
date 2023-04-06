# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ComponentRemovalProgress(object):

    """Implementation of the 'ComponentRemovalProgress' model.

    ComponentRemovalProgress is the struct to define the removal progress of an
    entity w.r.t a given component.


    Attributes:

        is_removal_stuck (bool): If there is no progress for certain threshold
            time, set this flag to true
        progress_percentage (long|int): Progress percentage
        removal_progress (string): Removal progress details.
        service_name (string): Name of the component.
        time_remaining (long|int): Time remaining
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "is_removal_stuck":'isRemovalStuck',
        "progress_percentage":'progressPercentage',
        "removal_progress":'removalProgress',
        "service_name":'serviceName',
        "time_remaining":'timeRemaining',
    }
    def __init__(self,
                 is_removal_stuck=None,
                 progress_percentage=None,
                 removal_progress=None,
                 service_name=None,
                 time_remaining=None,
            ):

        """Constructor for the ComponentRemovalProgress class"""

        # Initialize members of the class
        self.is_removal_stuck = is_removal_stuck
        self.progress_percentage = progress_percentage
        self.removal_progress = removal_progress
        self.service_name = service_name
        self.time_remaining = time_remaining

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
        is_removal_stuck = dictionary.get('isRemovalStuck')
        progress_percentage = dictionary.get('progressPercentage')
        removal_progress = dictionary.get('removalProgress')
        service_name = dictionary.get('serviceName')
        time_remaining = dictionary.get('timeRemaining')

        # Return an object of this model
        return cls(
            is_removal_stuck,
            progress_percentage,
            removal_progress,
            service_name,
            time_remaining
)