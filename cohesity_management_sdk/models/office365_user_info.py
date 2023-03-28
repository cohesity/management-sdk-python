# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class Office365UserInfo(object):

    """Implementation of the 'Office365UserInfo' model.

    Specifies information about an Office365 user.


    Attributes:

        city (string): Specifies the city in which the Office365 user is
            located.
        country (string): Specifies the country/region in which the Office365
            user is located.
        department (string): Specifies the department within the enterprise of
            the Office365 user.
        designation (string): Specifies the designation of the Office365 user.
        graph_uuid (string): Specifies the MS Graph UUID for the given user
            entity.
        is_mailbox_enabled (bool): Specifies whether the Office365 user has a
            mailbox associated.
        is_one_drive_enabled (bool): Specifies whether the Office365 user has a
            OneDrive associated.
        mailbox_size (long|int): Specifies the size of the Outlook Mailbox
            associated with this Office365 entity.
        mailbox_type (MailboxTypeEnum): Specifies the type of mailbox
            associated Specifies the type of user mailbox. 'kUserMailbox'
            indicates that the user has been assigned an individual mailbox.
            'kSharedMailbox' indicates that the user has been assigned a shared
            mailbox.
        one_drive_id (string): Specifies the Id of the OneDrive associated with
            the this Office 365 entity.
        one_drive_size (long|int): Specifies the size of the OneDrive
            associated with this Office365 entity.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "city":'city',
        "country":'country',
        "department":'department',
        "designation":'designation',
        "graph_uuid":'graphUuid',
        "is_mailbox_enabled":'isMailboxEnabled',
        "is_one_drive_enabled":'isOneDriveEnabled',
        "mailbox_size":'mailboxSize',
        "mailbox_type":'mailboxType',
        "one_drive_id":'oneDriveId',
        "one_drive_size":'oneDriveSize',
    }
    def __init__(self,
                 city=None,
                 country=None,
                 department=None,
                 designation=None,
                 graph_uuid=None,
                 is_mailbox_enabled=None,
                 is_one_drive_enabled=None,
                 mailbox_size=None,
                 mailbox_type=None,
                 one_drive_id=None,
                 one_drive_size=None,
            ):

        """Constructor for the Office365UserInfo class"""

        # Initialize members of the class
        self.city = city
        self.country = country
        self.department = department
        self.designation = designation
        self.graph_uuid = graph_uuid
        self.is_mailbox_enabled = is_mailbox_enabled
        self.is_one_drive_enabled = is_one_drive_enabled
        self.mailbox_size = mailbox_size
        self.mailbox_type = mailbox_type
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
        city = dictionary.get('city')
        country = dictionary.get('country')
        department = dictionary.get('department')
        designation = dictionary.get('designation')
        graph_uuid = dictionary.get('graphUuid')
        is_mailbox_enabled = dictionary.get('isMailboxEnabled')
        is_one_drive_enabled = dictionary.get('isOneDriveEnabled')
        mailbox_size = dictionary.get('mailboxSize')
        mailbox_type = dictionary.get('mailboxType')
        one_drive_id = dictionary.get('oneDriveId')
        one_drive_size = dictionary.get('oneDriveSize')

        # Return an object of this model
        return cls(
            city,
            country,
            department,
            designation,
            graph_uuid,
            is_mailbox_enabled,
            is_one_drive_enabled,
            mailbox_size,
            mailbox_type,
            one_drive_id,
            one_drive_size
)