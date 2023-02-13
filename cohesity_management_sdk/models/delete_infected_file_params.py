# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.infected_file_param

class DeleteInfectedFileParams(object):

    """Implementation of the 'DeleteInfectedFileParams' model.

    Specifies the parameters to delete the infected files.

    Attributes:
        infected_file_ids (list of InfectedFileParam): Specifies the list of
            infected file path.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "infected_file_ids":'infectedFileIds'
    }

    def __init__(self,
                 infected_file_ids=None):
        """Constructor for the DeleteInfectedFileParams class"""

        # Initialize members of the class
        self.infected_file_ids = infected_file_ids


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
        infected_file_ids = None
        if dictionary.get('infectedFileIds') != None:
            infected_file_ids = list()
            for structure in dictionary.get('infectedFileIds'):
                infected_file_ids.append(cohesity_management_sdk.models.infected_file_param.InfectedFileParam.from_dictionary(structure))

        # Return an object of this model
        return cls(infected_file_ids)


