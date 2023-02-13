# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.restore_object
import cohesity_management_sdk.models.restore_site_params_site_owner_drive

class RestoreSiteParams_SiteOwner(object):

    """Implementation of the 'RestoreSiteParams_SiteOwner' model.

    TODO: Type model description here.

    Attributes:
        drive_vec (list of RestoreSiteParams_SiteOwner_Drive): The list of
            drives that are being restored.
        m_object (RestoreObject): This will store the details of the user whose
            drives is to be restored.
        parent_site (EntityProto): The entity representing the parent site if
            we are restoring a subsite.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "drive_vec": 'driveVec',
        "m_object": 'object',
        "parent_site":'parentSite'
    }

    def __init__(self,
                 drive_vec=None,
                 m_object=None,
                 parent_site=None):
        """Constructor for the RestoreSiteParams_SiteOwner class"""

        # Initialize members of the class
        self.drive_vec = drive_vec
        self.m_object = m_object
        self.parent_site = parent_site


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
        drive_vec = None
        if dictionary.get('driveVec') != None:
            drive_vec = list()
            for structure in dictionary.get('driveVec'):
                drive_vec.append(cohesity_management_sdk.models.restore_site_params_site_owner_drive.RestoreSiteParams_SiteOwner_Drive.from_dictionary(structure))
        m_object = cohesity_management_sdk.models.restore_object.RestoreObject.from_dictionary(dictionary.get('object')) if dictionary.get('object') else None
        parent_site = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('parentSite')) if dictionary.get('parentSite') else None

        # Return an object of this model
        return cls(drive_vec,
                   m_object,
                   parent_site)


