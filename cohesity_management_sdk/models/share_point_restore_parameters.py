# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.site_owner
import cohesity_management_sdk.models.protection_source

class SharePointRestoreParameters(object):

    """Implementation of the 'SharePointRestoreParameters' model.

    Specifies information needed for recovering SharePoint Site and items.

    Attributes:
        restore_to_original_site (bool): Specifies whether the objects are to
            be restored to the original drive.
        site_owner_list (list of SiteOwner): Specifies the list of SharePoint
            Sites whose Document Repositories are being restored.
        target_document_library_name (string): Specifies the target document
            library name within the alternate site.
        target_document_library_prefix (string): Specifies a custom prefix for
            the document libraries when being restored to the original or an
            alternate site.
        target_site (ProtectionSource): Specifies the target site where the
            recovery of the entire Site or the Site items is to be done.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "restore_to_original_site": 'restoreToOriginalSite',
        "site_owner_list": 'siteOwnerList',
        "target_document_library_name": 'targetDocumentLibraryName',
        "target_document_library_prefix": 'targetDocumentLibraryPrefix',
        "target_site":'targetSite'
    }

    def __init__(self,
                 restore_to_original_site=None,
                 site_owner_list=None,
                 target_document_library_name=None,
                 target_document_library_prefix=None,
                 target_site=None):
        """Constructor for the SharePointRestoreParameters class"""

        # Initialize members of the class
        self.restore_to_original_site = restore_to_original_site
        self.site_owner_list = site_owner_list
        self.target_document_library_name = target_document_library_name
        self.target_document_library_prefix = target_document_library_prefix
        self.target_site = target_site

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
        restore_to_original_site = dictionary.get('restoreToOriginalSite')
        site_owner_list = None
        if dictionary.get('siteOwnerList') != None:
            site_owner_list = list()
            for structure in dictionary.get('siteOwnerList'):
                site_owner_list.append(cohesity_management_sdk.models.site_owner.SiteOwner.from_dictionary(structure))
        target_document_library_name = dictionary.get('targetDocumentLibraryName')
        target_document_library_prefix = dictionary.get('targetDocumentLibraryPrefix')
        target_site = cohesity_management_sdk.models.protection_source.ProtectionSource.from_dictionary(dictionary.get('targetSite')) if dictionary.get('targetSite') else None

        # Return an object of this model
        return cls(restore_to_original_site,
                   site_owner_list,
                   target_document_library_name,
                   target_document_library_prefix,
                   target_site)


