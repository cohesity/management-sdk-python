# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ThrottlingConfiguration(object):

    """Implementation of the 'ThrottlingConfiguration' model.

    Specifies the throttling configuration parameters.

    Attributes:
        fixed_threshold (long|int): Fixed baseline threshold for throttling. This is
            mandatory for any other throttling type than kNoThrottling.
        pattern_type (int): Type of the throttling pattern.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "fixed_threshold": 'fixedThreshold',
        "pattern_type": 'patternType'
    }

    def __init__(self,
                 fixed_threshold=None,
                 pattern_type=None):
        """Constructor for the ThrottlingConfiguration class"""

        # Initialize members of the class
        self.fixed_threshold = fixed_threshold
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
        fixed_threshold = dictionary.get('fixedThreshold', None)
        pattern_type = dictionary.get('patternType', None)

        # Return an object of this model
        return cls(fixed_threshold,
                   pattern_type)


