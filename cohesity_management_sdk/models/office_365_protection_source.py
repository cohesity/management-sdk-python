# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.office_365_group_info
import cohesity_management_sdk.models.office_365_site_info
import cohesity_management_sdk.models.office_365_team_info
import cohesity_management_sdk.models.office_365_user_info


class Office365ProtectionSource(object):

    """Implementation of the 'Office365ProtectionSource' model.

    Specifies a Protection Source in Office 365 environment.


    Attributes:

        description (string): Specifies the description of the Office 365
            entity.
        group_info (Office365GroupInfo): Specifies the information about
            Office365 group.
        name (string): Specifies the name of the office 365 entity.
        primary_s_m_t_p_address (string): Specifies the SMTP address for the
            Outlook source.
        proxy_host_source_id_list (list of long|int): Specifies the list of the
            protection source id of the windows physical host which will be
            used during the protection and recovery of the sites that belong to
            an office365 domain. This will be used for Exchange Online PST
            download as well.
        site_info (Office365SiteInfo): Specifies the information about
            Office365 site.
        team_info (Office365TeamInfo): Specifies the information about
            Office365 team.
        mtype (TypeOffice365ProtectionSourceEnum): Specifies the type of the
            Office 365 entity.
        user_info (Office365UserInfo): Specifies the information about
            Office365 user regarding its Mailbox & OneDrive. This is only
            present if the entity type is a User.
        uuid (string): Specifies the UUID of the Office 365 entity.
        web_url (string): URL that displays the site in the browser. This is
            applicable for Sharepoint entity.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "description":'description',
        "group_info":'groupInfo',
        "name":'name',
        "primary_s_m_t_p_address":'primarySMTPAddress',
        "proxy_host_source_id_list":'proxyHostSourceIdList',
        "site_info":'siteInfo',
        "team_info":'teamInfo',
        "mtype":'type',
        "user_info":'userInfo',
        "uuid":'uuid',
        "web_url":'webUrl',
    }
    def __init__(self,
                 description=None,
                 group_info=None,
                 name=None,
                 primary_s_m_t_p_address=None,
                 proxy_host_source_id_list=None,
                 site_info=None,
                 team_info=None,
                 mtype=None,
                 user_info=None,
                 uuid=None,
                 web_url=None,
            ):

        """Constructor for the Office365ProtectionSource class"""

        # Initialize members of the class
        self.description = description
        self.group_info = group_info
        self.name = name
        self.primary_s_m_t_p_address = primary_s_m_t_p_address
        self.proxy_host_source_id_list = proxy_host_source_id_list
        self.site_info = site_info
        self.team_info = team_info
        self.mtype = mtype
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
        group_info = cohesity_management_sdk.models.office_365_group_info.Office365GroupInfo.from_dictionary(dictionary.get('groupInfo')) if dictionary.get('groupInfo') else None
        name = dictionary.get('name')
        primary_s_m_t_p_address = dictionary.get('primarySMTPAddress')
        proxy_host_source_id_list = dictionary.get("proxyHostSourceIdList")
        site_info = cohesity_management_sdk.models.office_365_site_info.Office365SiteInfo.from_dictionary(dictionary.get('siteInfo')) if dictionary.get('siteInfo') else None
        team_info = cohesity_management_sdk.models.office_365_team_info.Office365TeamInfo.from_dictionary(dictionary.get('teamInfo')) if dictionary.get('teamInfo') else None
        mtype = dictionary.get('type')
        user_info = cohesity_management_sdk.models.office_365_user_info.Office365UserInfo.from_dictionary(dictionary.get('userInfo')) if dictionary.get('userInfo') else None
        uuid = dictionary.get('uuid')
        web_url = dictionary.get('webUrl')

        # Return an object of this model
        return cls(
            description,
            group_info,
            name,
            primary_s_m_t_p_address,
            proxy_host_source_id_list,
            site_info,
            team_info,
            mtype,
            user_info,
            uuid,
            web_url
)