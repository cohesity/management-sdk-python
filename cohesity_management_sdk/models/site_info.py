# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.site_identity
import cohesity_management_sdk.models.site_property


class SiteInfo(object):

    """Implementation of the 'SiteInfo' model.

    Information about the site backed up that is used to restore. For example
    we need to create the extract site type that was backed up if the site does
    not exist. All fields are case insensitive. This is an aggregation of all
    required and optional parameters in New-PnPSite/New-TenantSite/New-PnPWeb
    cmdlets.


    Attributes:

        classification (string): Site classification assigned by administrator.
        compatibility_level (int): Compatibility level . Its the site's
            compatibility to SPO server version.
        description (string): Admin entered description of this site.
        design (string): Needed for site collection create. Maps to
            CommunicationSiteDesign enum (Topic = 0,Showcase = 1,Blank = 2)
        design_id (string): Design template id.
        geolocation (string): Geo location of the site.
        group_id (string): Group Id to which this site belongs.
        hubsite_id (string): If it is a hub member site, the parent hub site
            id.
        hubsite_url (string): If it is a hub member site, the parent hub site
            url. This can be used to restore a hub site member to same hub site
            even when the site is deleted and recreated or across tenants.
        is_hubsite (bool): Is it a Hub? This will be false for a hub member.
        is_multilingual (bool): Site is multilingual, needs to get multilingual
            resource pages.
        is_personalsite (bool): Is this a personal site with
            'https://*-my.sharepoint.com/*' pattern.
        is_public (bool): Is this a public or private site?
        is_subsite (bool): Is this a subsite or root site? If this is a
            subsite, it will inherit the template of root site.
        lcid (int): Site LcId=1033 etc..
        locale_id (int): Locale id of the site. Normally 1033 for US English
            locale.
        owner_vec (list of string): Owner. This is an email. Note that across
            tenants, this email address may be invalid. user@tenant.com. At
            least one owner must be there.
        read_only (bool): Site is read-only, locked, and unavailable for write
            access.
        root_web_id (string): Rootwebid.
        site (SiteIdentity): Site identifier echo.
        siteprop_vec (list of SiteProperty): Vector of sites collection
            properties (for classic site collections). Got from Get-PnPSite.
        template (string): Site Template such as GROUP#0,
            POINTPUBLISHINGTOPIC#0,...
        tenantsiteprop_vec (list of SiteProperty): Vector of tenant sites
            collection properties (for modern site collections). Got from
            Get-PnPTenantSite.
        timezone_id (int): Timezone Id. This is needed to create a site
            collection(tenant site).
        webprop_vec (list of SiteProperty): Vector of sites collection
            properties (for subsites). Got from Get-PnPWeb.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "classification":'classification',
        "compatibility_level":'compatibilityLevel',
        "description":'description',
        "design":'design',
        "design_id":'designId',
        "geolocation":'geolocation',
        "group_id":'groupId',
        "hubsite_id":'hubsiteId',
        "hubsite_url":'hubsiteUrl',
        "is_hubsite":'isHubsite',
        "is_multilingual":'isMultilingual',
        "is_personalsite":'isPersonalsite',
        "is_public":'isPublic',
        "is_subsite":'isSubsite',
        "lcid":'lcid',
        "locale_id":'localeId',
        "owner_vec":'ownerVec',
        "read_only":'readOnly',
        "root_web_id":'rootWebId',
        "site":'site',
        "siteprop_vec":'sitepropVec',
        "template":'template',
        "tenantsiteprop_vec":'tenantsitepropVec',
        "timezone_id":'timezoneId',
        "webprop_vec":'webpropVec',
    }
    def __init__(self,
                 classification=None,
                 compatibility_level=None,
                 description=None,
                 design=None,
                 design_id=None,
                 geolocation=None,
                 group_id=None,
                 hubsite_id=None,
                 hubsite_url=None,
                 is_hubsite=None,
                 is_multilingual=None,
                 is_personalsite=None,
                 is_public=None,
                 is_subsite=None,
                 lcid=None,
                 locale_id=None,
                 owner_vec=None,
                 read_only=None,
                 root_web_id=None,
                 site=None,
                 siteprop_vec=None,
                 template=None,
                 tenantsiteprop_vec=None,
                 timezone_id=None,
                 webprop_vec=None,
            ):

        """Constructor for the SiteInfo class"""

        # Initialize members of the class
        self.classification = classification
        self.compatibility_level = compatibility_level
        self.description = description
        self.design = design
        self.design_id = design_id
        self.geolocation = geolocation
        self.group_id = group_id
        self.hubsite_id = hubsite_id
        self.hubsite_url = hubsite_url
        self.is_hubsite = is_hubsite
        self.is_multilingual = is_multilingual
        self.is_personalsite = is_personalsite
        self.is_public = is_public
        self.is_subsite = is_subsite
        self.lcid = lcid
        self.locale_id = locale_id
        self.owner_vec = owner_vec
        self.read_only = read_only
        self.root_web_id = root_web_id
        self.site = site
        self.siteprop_vec = siteprop_vec
        self.template = template
        self.tenantsiteprop_vec = tenantsiteprop_vec
        self.timezone_id = timezone_id
        self.webprop_vec = webprop_vec

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
        classification = dictionary.get('classification')
        compatibility_level = dictionary.get('compatibilityLevel')
        description = dictionary.get('description')
        design = dictionary.get('design')
        design_id = dictionary.get('designId')
        geolocation = dictionary.get('geolocation')
        group_id = dictionary.get('groupId')
        hubsite_id = dictionary.get('hubsiteId')
        hubsite_url = dictionary.get('hubsiteUrl')
        is_hubsite = dictionary.get('isHubsite')
        is_multilingual = dictionary.get('isMultilingual')
        is_personalsite = dictionary.get('isPersonalsite')
        is_public = dictionary.get('isPublic')
        is_subsite = dictionary.get('isSubsite')
        lcid = dictionary.get('lcid')
        locale_id = dictionary.get('localeId')
        owner_vec = dictionary.get("ownerVec")
        read_only = dictionary.get('readOnly')
        root_web_id = dictionary.get('rootWebId')
        site = cohesity_management_sdk.models.site_identity.SiteIdentity.from_dictionary(dictionary.get('site')) if dictionary.get('site') else None
        siteprop_vec = None
        if dictionary.get('sitepropVec') != None:
            siteprop_vec = list()
            for structure in dictionary.get('sitepropVec'):
                siteprop_vec.append(cohesity_management_sdk.models.site_property.SiteProperty.from_dictionary(structure))
        template = dictionary.get('template')
        tenantsiteprop_vec = None
        if dictionary.get('tenantsitepropVec') != None:
            tenantsiteprop_vec = list()
            for structure in dictionary.get('tenantsitepropVec'):
                tenantsiteprop_vec.append(cohesity_management_sdk.models.site_property.SiteProperty.from_dictionary(structure))
        timezone_id = dictionary.get('timezoneId')
        webprop_vec = None
        if dictionary.get('webpropVec') != None:
            webprop_vec = list()
            for structure in dictionary.get('webpropVec'):
                webprop_vec.append(cohesity_management_sdk.models.site_property.SiteProperty.from_dictionary(structure))

        # Return an object of this model
        return cls(
            classification,
            compatibility_level,
            description,
            design,
            design_id,
            geolocation,
            group_id,
            hubsite_id,
            hubsite_url,
            is_hubsite,
            is_multilingual,
            is_personalsite,
            is_public,
            is_subsite,
            lcid,
            locale_id,
            owner_vec,
            read_only,
            root_web_id,
            site,
            siteprop_vec,
            template,
            tenantsiteprop_vec,
            timezone_id,
            webprop_vec
)