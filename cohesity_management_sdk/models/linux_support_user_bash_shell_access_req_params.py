# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class LinuxSupportUserBashShellAccessReqParams(object):

    """Implementation of the 'LinuxSupportUserBashShellAccessReqParams' model.

    Linux Support Bash Shell Access Req Params.

    Attributes:
        regenerate_token (bool): If RegenerateToken is set to true, the token
            would be regenerated and the new token will be returned.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "regenerate_token":'regenerateToken'
    }

    def __init__(self,
                 regenerate_token=None):
        """Constructor for the LinuxSupportUserBashShellAccessReqParams class"""

        # Initialize members of the class
        self.regenerate_token = regenerate_token


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
        regenerate_token = dictionary.get('regenerateToken')

        # Return an object of this model
        return cls(regenerate_token)


