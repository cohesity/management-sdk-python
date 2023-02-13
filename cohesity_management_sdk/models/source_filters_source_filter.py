# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class SourceFilters_SourceFilter(object):

    """Implementation of the 'SourceFilters_SourceFilter' model.

    Plain text filter: { source_filter: "TestDatabase", is_regex: false}.
    Wildcard filter: { source_filter: "Test?Database*", is_regex: false}.
    Regex filter: { source_filter: "^Test.*Database$", is_regex: true}.

    Attributes:
        case_sensitive (bool): Determines if the filter is case sensitive or
            not. For some environments (e.g. SQL), there may be a flag
            controlled default if the field is not populated while for some
            environments (e.g. VMware), the default will be based on the default
            value for this field.
        is_regex (bool): If true, this implies 'source_filter' is a regex
            filter. If false, it will be treated as wildcard/plain text
            filter.
        source_filter (string): This contains the filter string.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "case_sensitive":'caseSensitive',
        "is_regex": 'isRegex',
        "source_filter": 'sourceFilter'
    }

    def __init__(self,
                 case_sensitive=None,
                 is_regex=None,
                 source_filter=None):
        """Constructor for the SourceFilters_SourceFilter class"""

        # Initialize members of the class
        self.case_sensitive = case_sensitive
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
        case_sensitive = dictionary.get('caseSensitive')
        is_regex = dictionary.get('isRegex', None)
        source_filter = dictionary.get('sourceFilter', None)

        # Return an object of this model
        return cls(case_sensitive,
                   is_regex,
                   source_filter)


