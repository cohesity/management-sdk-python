# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.office_365_user_info

class Office365ProtectionSource(object):

    """Implementation of the 'Office365ProtectionSource' model.

    Specifies a Protection Source in Office 365 environment.

    Attributes:
        description (string): Specifies the description of the Office 365
            entity.
        name (string): Specifies the name of the office 365 entity.
        primary_smtp_address (string): Specifies the SMTP address for the
            Outlook source.
        mtype (TypeOffice365ProtectionSourceEnum): Specifies the type of the
            Office 365 entity. Specifies the type of Office 365 entity
            'kDomain' indicates the O365 domain through which authentication
            occurs. 'kOutlook' indicates the Exchange online entities.
            'kMailbox' indicates the user's mailbox account. 'kUsers'
            indicates the container for User entities. 'kGroups' indicates the
            container for Group entities. 'kSites' indicates the container for
            Site entities. 'kUser' indicates an Office365 User entity.
            'kGroup' indicates an Office365 Group entity. 'kSite' indicates an
            Office365 SharePoint Site entity.
        user_info (Office365UserInfo): Specifies information about an
            Office365 user.
        uuid (string): Specifies the UUID of the Office 365 entity.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description":'description',
        "name":'name',
        "primary_smtp_address":'primarySMTPAddress',
        "mtype":'type',
        "user_info":'userInfo',
        "uuid":'uuid'
    }

    def __init__(self,
                 description=None,
                 name=None,
                 primary_smtp_address=None,
                 mtype=None,
                 user_info=None,
                 uuid=None):
        """Constructor for the Office365ProtectionSource class"""

        # Initialize members of the class
        self.description = description
        self.name = name
        self.primary_smtp_address = primary_smtp_address
        self.mtype = mtype
        self.user_info = user_info
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
        user_info = cohesity_management_sdk.models.office_365_user_info.Office365UserInfo.from_dictionary(dictionary.get('userInfo')) if dictionary.get('userInfo') else None
        uuid = dictionary.get('uuid')

        # Return an object of this model
        return cls(description,
                   name,
                   primary_smtp_address,
                   mtype,
                   user_info,
                   uuid)


