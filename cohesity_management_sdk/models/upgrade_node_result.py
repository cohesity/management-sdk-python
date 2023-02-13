# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class UpgradeNodeResult(object):

    """Implementation of the 'UpgradeNodeResult' model.

    Specifies the result returned from a request to upgrade a Node.

    Attributes:
        message (string): Specifies a message describing the result of the
            request.
        status_url (string): Specifies a URL that can be queried to get the
            status of the operation once it has begun.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "message":'message',
        "status_url":'statusUrl'
    }

    def __init__(self,
                 message=None,
                 status_url=None):
        """Constructor for the UpgradeNodeResult class"""

        # Initialize members of the class
        self.message = message
        self.status_url = status_url


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
        message = dictionary.get('message')
        status_url = dictionary.get('statusUrl')

        # Return an object of this model
        return cls(message,
                   status_url)


