# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class UsersDiscoveryParams(object):

    """Implementation of the 'UsersDiscoveryParams' model.

    Specifies discovery params for kUser entities. It should only be populated
    when the 'DiscoveryParams.discoverableObjectTypeList' includes 'kUsers'.


    Attributes:

        discover_users_with_mailbox (bool): Specifies if office 365 users with
            valid mailboxes should be discovered or not.
        discover_users_with_onedrive (bool): Specifies if office 365 users with
            valid Onedrives should be discovered or not.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "discover_users_with_mailbox":'discoverUsersWithMailbox',
        "discover_users_with_onedrive":'discoverUsersWithOnedrive',
    }
    def __init__(self,
                 discover_users_with_mailbox=None,
                 discover_users_with_onedrive=None,
            ):

        """Constructor for the UsersDiscoveryParams class"""

        # Initialize members of the class
        self.discover_users_with_mailbox = discover_users_with_mailbox
        self.discover_users_with_onedrive = discover_users_with_onedrive

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
        discover_users_with_mailbox = dictionary.get('discoverUsersWithMailbox')
        discover_users_with_onedrive = dictionary.get('discoverUsersWithOnedrive')

        # Return an object of this model
        return cls(
            discover_users_with_mailbox,
            discover_users_with_onedrive
)