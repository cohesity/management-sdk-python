# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.infected_file

class InfectedFiles(object):

    """Implementation of the 'InfectedFiles' model.

    Specifies the Result parameters for all infected files.

    Attributes:
        infected_files (list of InfectedFile): Specifies the infected files.
        pagination_cookie (string): This cookie can be used in the succeeding
            call to list infected files to get the next set of infected files.
            If set to nil, it means that there's no more results that the
            server could provide.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "infected_files":'infectedFiles',
        "pagination_cookie":'paginationCookie'
    }

    def __init__(self,
                 infected_files=None,
                 pagination_cookie=None):
        """Constructor for the InfectedFiles class"""

        # Initialize members of the class
        self.infected_files = infected_files
        self.pagination_cookie = pagination_cookie


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
        infected_files = None
        if dictionary.get('infectedFiles') != None:
            infected_files = list()
            for structure in dictionary.get('infectedFiles'):
                infected_files.append(cohesity_management_sdk.models.infected_file.InfectedFile.from_dictionary(structure))
        pagination_cookie = dictionary.get('paginationCookie')

        # Return an object of this model
        return cls(infected_files,
                   pagination_cookie)


