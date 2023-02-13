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
        mailbox_size (long|int): Specifies the size of the Outlook Mailbox
            associated with this Office365 entity.
        one_drive_id (string): Specifies the Id of the OneDrive associated
            with the this Office 365 entity.
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
        "mailbox_size":'mailboxSize',
        "one_drive_id":'oneDriveId',
        "one_drive_size":'oneDriveSize'
    }

    def __init__(self,
                 city=None,
                 country=None,
                 department=None,
                 designation=None,
                 graph_uuid=None,
                 mailbox_size=None,
                 one_drive_id=None,
                 one_drive_size=None):
        """Constructor for the Office365UserInfo class"""

        # Initialize members of the class
        self.city = city
        self.country = country
        self.department = department
        self.designation = designation
        self.graph_uuid = graph_uuid
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
        city = dictionary.get('city')
        country = dictionary.get('country')
        department = dictionary.get('department')
        designation = dictionary.get('designation')
        graph_uuid = dictionary.get('graphUuid')
        mailbox_size = dictionary.get('mailboxSize')
        one_drive_id = dictionary.get('oneDriveId')
        one_drive_size = dictionary.get('oneDriveSize')

        # Return an object of this model
        return cls(city,
                   country,
                   department,
                   designation,
                   graph_uuid,
                   mailbox_size,
                   one_drive_id,
                   one_drive_size)


