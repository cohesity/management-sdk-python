# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class SupportedPattern(object):

    """Implementation of the 'SupportedPattern' model.

    Specifies details of the pattern available for search available in an
    application such as Pattern Finder within Analytics Work Bench.

    Attributes:
        is_system_defined (bool): Specifies the Authenticating
            Database for this MongoDB cluster.
        name (string): Specifies the name of the Pattern.
        pattern (string): Specifies the value of the pattern(Regex).
            SSL only in this cluster.
        pattern_type (PatternTypeSupportedPatternEnum): Specifies the Pattern type.
            'REGULAR' indicates that the pattern contains a regular
            expression.
            'TEMPLATE' indicates that the pattern has a pre defined input
            pattern such as date of the form 'DD-MM-YYYY'.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "is_system_defined":'isSystemDefined',
        "name":'name',
        "pattern":'pattern',
        "pattern_type":'patternType'
    }

    def __init__(self,
                 is_system_defined=None,
                 name=None,
                 pattern=None,
                 pattern_type=None):
        """Constructor for the SupportedPattern class"""

        # Initialize members of the class
        self.is_system_defined = is_system_defined
        self.name = name
        self.pattern = pattern
        self.pattern_type = pattern_type


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
        is_system_defined = dictionary.get('isSystemDefined')
        name = dictionary.get('name')
        pattern = dictionary.get('pattern')
        pattern_type = dictionary.get('patternType')

        # Return an object of this model
        return cls(is_system_defined,
                   name,
                   pattern,
                   pattern_type)


