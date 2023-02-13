# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.site_drive_info
import cohesity_management_sdk.models.restore_object_details

class SiteOwner(object):

    """Implementation of the 'SiteOwner' model.

    Specifies the details about a SharePoint Site owner.

    Attributes:
        drive_info_list (list of SiteDriveInfo): Specifies the Document
            Libraries within a Site which are to be restored.
        site_detail_object (RestoreObjectDetails): Specifies the details about
            the SharePoint Site to which drives belong.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "drive_info_list": 'driveInfoList',
        "site_detail_object": 'siteDetailObject'
    }

    def __init__(self,
                 drive_info_list=None,
                 site_detail_object=None):
        """Constructor for the SiteOwner class"""

        # Initialize members of the class
        self.drive_info_list = drive_info_list
        self.site_detail_object = site_detail_object


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
        drive_info_list = None
        if dictionary.get('driveInfoList') != None:
            drive_info_list = list()
            for structure in dictionary.get('driveInfoList'):
                drive_info_list.append(cohesity_management_sdk.models.site_drive_info.SiteDriveInfo.from_dictionary(structure))
        site_detail_object = cohesity_management_sdk.models.restore_object_details.RestoreObjectDetails.from_dictionary(dictionary.get('siteDetailObject')) if dictionary.get('siteDetailObject') else None

        # Return an object of this model
        return cls(drive_info_list,
                   site_detail_object)

