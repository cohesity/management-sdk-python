# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class MSExchangeParams(object):

    """Implementation of the 'MSExchangeParams' model.

    All the params specific to MS exchange application.

    Attributes:
        perform_log_truncation (bool): If this is set to true, then an attempt
            will be made to truncate exchange logs.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "perform_log_truncation":'performLogTruncation'
    }

    def __init__(self,
                 perform_log_truncation=None):
        """Constructor for the MSExchangeParams class"""

        # Initialize members of the class
        self.perform_log_truncation = perform_log_truncation


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
        perform_log_truncation = dictionary.get('performLogTruncation')

        # Return an object of this model
        return cls(perform_log_truncation)


