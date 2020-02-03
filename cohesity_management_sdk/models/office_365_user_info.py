# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class Office365UserInfo(object):

    """Implementation of the 'Office365UserInfo' model.

    Specifies information about an Office365 user.

    Attributes:
        mailbox_size (long|int): Specifies the size of the Outlook Mailbox
            associated with this Office365 entity.
        one_drive_id (string): Specifies the Id of the OneDrive associated
            with the this Office 365 entity.
        one_drive_size (long|int): Specifies the size of the OneDrive
            associated with this Office365 entity.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mailbox_size":'mailboxSize',
        "one_drive_id":'oneDriveId',
        "one_drive_size":'oneDriveSize'
    }

    def __init__(self,
                 mailbox_size=None,
                 one_drive_id=None,
                 one_drive_size=None):
        """Constructor for the Office365UserInfo class"""

        # Initialize members of the class
        self.mailbox_size = mailbox_size
        self.one_drive_id = one_drive_id
        self.one_drive_size = one_drive_size


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
        mailbox_size = dictionary.get('mailboxSize')
        one_drive_id = dictionary.get('oneDriveId')
        one_drive_size = dictionary.get('oneDriveSize')

        # Return an object of this model
        return cls(mailbox_size,
                   one_drive_id,
                   one_drive_size)


