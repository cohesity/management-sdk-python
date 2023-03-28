# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.map_reduce_info


class ApplicationsWrapper(object):

    """Implementation of the 'ApplicationsWrapper' model.

    ApplicationsWrapper is the struct to define the list of map-reduce
    applications.


    Attributes:

        applications (list of MapReduceInfo): Applications specifies the list
            of available map-reduce applications in analytics workbench.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "applications":'applications',
    }
    def __init__(self,
                 applications=None,
            ):

        """Constructor for the ApplicationsWrapper class"""

        # Initialize members of the class
        self.applications = applications

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
        applications = None
        if dictionary.get('applications') != None:
            applications = list()
            for structure in dictionary.get('applications'):
                applications.append(cohesity_management_sdk.models.map_reduce_info.MapReduceInfo.from_dictionary(structure))

        # Return an object of this model
        return cls(
            applications
)