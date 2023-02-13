# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class IdpReachabilityTestResult(object):

    """Implementation of the 'IdpReachabilityTestResult' model.

    Specifies the result of the reachability test done for an IdP.

    Attributes:
        reachable (bool): Specifies the flag for Idp reachability.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "reachable":'reachable'
    }

    def __init__(self,
                 reachable=None):
        """Constructor for the IdpReachabilityTestResult class"""

        # Initialize members of the class
        self.reachable = reachable


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
        reachable = dictionary.get('reachable')

        # Return an object of this model
        return cls(reachable)


