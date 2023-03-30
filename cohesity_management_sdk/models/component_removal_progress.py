# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ComponentRemovalProgress(object):

    """Implementation of the 'ComponentRemovalProgress' model.

    ComponentRemovalProgress is the struct to define the removal progress of an
    entity w.r.t a given component.


    Attributes:

        removal_progress (string): Removal progress details.
        service_name (string): Name of the component.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "removal_progress":'removalProgress',
        "service_name":'serviceName',
    }
    def __init__(self,
                 removal_progress=None,
                 service_name=None,
            ):

        """Constructor for the ComponentRemovalProgress class"""

        # Initialize members of the class
        self.removal_progress = removal_progress
        self.service_name = service_name

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
        removal_progress = dictionary.get('removalProgress')
        service_name = dictionary.get('serviceName')

        # Return an object of this model
        return cls(
            removal_progress,
            service_name
)