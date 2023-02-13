# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.mapper_info

class MappersWrapper(object):

    """Implementation of the 'MappersWrapper' model.

    MappersWrapper is the struct to define the list of mappers.

    Attributes:
        mappers (list of MapperInfo): Mappers specifies the list of available
            mappers in analytics workbench.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mappers":'mappers'
    }

    def __init__(self,
                 mappers=None):
        """Constructor for the MappersWrapper class"""

        # Initialize members of the class
        self.mappers = mappers


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
        mapper_list = None
        if dictionary.get('mappers', None) != None:
            mapper_list = list()
            for mapper in dictionary.get('mappers'):
                mapper_list.append(cohesity_management_sdk.models.mapper_info.MapperInfo.from_dictionary(mapper))

        # Return an object of this model
        return cls(mapper_list)


