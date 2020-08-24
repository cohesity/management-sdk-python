# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class SourceFilters_SourceFilter(object):

    """Implementation of the 'SourceFilters_SourceFilter' model.

    Plain text filter: { source_filter: "TestDatabase", is_regex: false}.
    Wildcard filter: { source_filter: "Test?Database*", is_regex: false}.
    Regex filter: { source_filter: "^Test.*Database$", is_regex: true}.

    Attributes:
        is_regex (bool): If true, this implies 'source_filter' is a regex
            filter. If false, it will be treated as wildcard/plain text
            filter.
        source_filter (string): This contains the filter string.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "is_regex": 'isRegex',
        "source_filter": 'sourceFilter'
    }

    def __init__(self,
                 is_regex=None,
                 source_filter=None):
        """Constructor for the SourceFilters_SourceFilter class"""

        # Initialize members of the class
        self.is_regex = is_regex
        self.source_filter = source_filter


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
        is_regex = dictionary.get('isRegex', None)
        source_filter = dictionary.get('sourceFilter', None)

        # Return an object of this model
        return cls(is_regex,
                   source_filter)


