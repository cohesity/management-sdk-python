# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.


class Office365ProtectionSource(object):

    """Implementation of the 'Office365ProtectionSource' model.

    Specifies a Protection Source in Office 365 environment.

    Attributes:
        description (string): Specifies the description of the Office 365
            entity.
        name (string): Specifies the name of the office 365 entity.
        primary_smtp_address (string): Specifies the SMTP address for the
            Outlook source.
        mtype (int): Specifies the type of the Office 365 entity.
        uuid (string): Specifies the UUID of the Office 365 entity.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description":'description',
        "name":'name',
        "primary_smtp_address":'primarySMTPAddress',
        "mtype":'type',
        "uuid":'uuid'
    }

    def __init__(self,
                 description=None,
                 name=None,
                 primary_smtp_address=None,
                 mtype=None,
                 uuid=None):
        """Constructor for the Office365ProtectionSource class"""

        # Initialize members of the class
        self.description = description
        self.name = name
        self.primary_smtp_address = primary_smtp_address
        self.mtype = mtype
        self.uuid = uuid


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
        description = dictionary.get('description')
        name = dictionary.get('name')
        primary_smtp_address = dictionary.get('primarySMTPAddress')
        mtype = dictionary.get('type')
        uuid = dictionary.get('uuid')

        # Return an object of this model
        return cls(description,
                   name,
                   primary_smtp_address,
                   mtype,
                   uuid)


