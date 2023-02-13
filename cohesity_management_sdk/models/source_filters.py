# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.source_filters_source_filter

class SourceFilters(object):

    """Implementation of the 'SourceFilters' model.

    For SQL, this filters will be applicable only for auto protect sources and
    can be used at the host, instance level.

    Attributes:
        exclude_source_filter_vec (list of SourceFilters_SourceFilter): This
            contains the list of exclude filters to be applied on the entities
            in the backup source.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "exclude_source_filter_vec":'excludeSourceFilterVec'
    }

    def __init__(self,
                 exclude_source_filter_vec=None):
        """Constructor for the SourceFilters class"""

        # Initialize members of the class
        self.exclude_source_filter_vec = exclude_source_filter_vec


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
        exclude_source_filter_vec = None
        if dictionary.get('excludeSourceFilterVec') != None:
            exclude_source_filter_vec = list()
            for structure in dictionary.get('excludeSourceFilterVec'):
                exclude_source_filter_vec.append(cohesity_management_sdk.models.source_filters_source_filter.SourceFilters_SourceFilter.from_dictionary(structure))

        # Return an object of this model
        return cls(exclude_source_filter_vec)


