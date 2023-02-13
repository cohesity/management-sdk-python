# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class GoogleAccountInfo(object):

    """Implementation of the 'GoogleAccountInfo' model.

    Google Account Information of a Helios BaaS user.

    Attributes:
        account_id (string): Specifies the Account Id assigned by Google.
        user_id (string): Specifies the User Id assigned by Google.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_id":'accountId',
        "user_id":'userId'
    }

    def __init__(self,
                 account_id=None,
                 user_id=None):
        """Constructor for the GoogleAccountInfo class"""

        # Initialize members of the class
        self.account_id = account_id
        self.user_id = user_id


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
        account_id = dictionary.get('accountId')
        user_id = dictionary.get('userId')

        # Return an object of this model
        return cls(account_id,
                   user_id)


