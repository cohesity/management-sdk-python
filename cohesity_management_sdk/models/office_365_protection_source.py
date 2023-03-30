# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.office_365_user_info
import cohesity_management_sdk.models.office_365_site_info

class Office365ProtectionSource(object):

    """Implementation of the 'Office365ProtectionSource' model.

    Specifies a Protection Source in Office 365 environment.

    Attributes:
        description (string): Specifies the description of the Office 365
            entity.
        name (string): Specifies the name of the office 365 entity.
        proxy_host_source_id_list (list of long|int): Specifies the list of the
            protection source id of the windows physical host which will be
            used during the protection and recovery of the sites that belong
            to an office365 domain. This will be used for Exchange Online PST
            download as well.
        primary_smtp_address (string): Specifies the SMTP address for the
            Outlook source.
        site_info (Office365SiteInfo): Specifies the information about
            Office365 site.
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
        web_url (string): URL that displays the site in the browser. This is
            applicable for Sharepoint entity.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description":'description',
        "name":'name',
        "proxy_host_source_id_list":'proxyHostSourceIdList',
        "primary_smtp_address":'primarySMTPAddress',
        "site_info":'siteInfo',
        "mtype":'type',
        "user_info":'userInfo',
        "uuid":'uuid',
        "web_url":'webUrl'
    }

    def __init__(self,
                 description=None,
                 name=None,
                 proxy_host_source_id_list=None,
                 primary_smtp_address=None,
                 mtype=None,
                 site_info=None,
                 user_info=None,
                 uuid=None,
                 web_url=None):
        """Constructor for the Office365ProtectionSource class"""

        # Initialize members of the class
        self.description = description
        self.name = name
        self.proxy_host_source_id_list = proxy_host_source_id_list
        self.primary_smtp_address = primary_smtp_address
        self.mtype = mtype
        self.site_info = site_info
        self.user_info = user_info
        self.uuid = uuid
        self.web_url = web_url


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
        proxy_host_source_id_list = dictionary.get('proxyHostSourceIdList')
        primary_smtp_address = dictionary.get('primarySMTPAddress')
        mtype = dictionary.get('type')
        site_info = cohesity_management_sdk.models.office_365_site_info.Office365SiteInfo.from_dictionary(dictionary.get('siteInfo')) if dictionary.get('siteInfo') else None
        user_info = cohesity_management_sdk.models.office_365_user_info.Office365UserInfo.from_dictionary(dictionary.get('userInfo')) if dictionary.get('userInfo') else None
        uuid = dictionary.get('uuid')
        web_url = dictionary.get('webUrl')

        # Return an object of this model
        return cls(description,
                   name,
                   proxy_host_source_id_list,
                   primary_smtp_address,
                   mtype,
                   site_info,
                   user_info,
                   uuid,
                   web_url)


