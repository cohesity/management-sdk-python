# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class LinuxSupportUserBashShellAccessResult(object):

    """Implementation of the 'LinuxSupportUserBashShellAccessResult' model.

    Specifies the result returned after a successful request to get the linux
    'support' user bash shell access token,

    Attributes:
        support_user_token (string): SSH identity key to login as 'support'
            user.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "support_user_token":'supportUserToken'
    }

    def __init__(self,
                 support_user_token=None):
        """Constructor for the LinuxSupportUserBashShellAccessResult class"""

        # Initialize members of the class
        self.support_user_token = support_user_token


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
        support_user_token = dictionary.get('supportUserToken')

        # Return an object of this model
        return cls(support_user_token)


