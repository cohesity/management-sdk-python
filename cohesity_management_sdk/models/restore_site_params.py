# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.error_proto
import cohesity_management_sdk.models.restore_site_params_site_owner

class RestoreSiteParams(object):

    """Implementation of the 'RestoreSiteParams' model.

    TODO: Type model description here.

    Attributes:
        restore_to_original (bool): Whether or not all sites are restored to
            original location.
        site_owner_vec (list of RestoreSiteParams_SiteOwner): The list of
            sites whose drives are being restored.
        target_doc_lib_name (string): Incase of alternate restore of granular
            items within document repositiories of sites to another site, a
            doc lib name has to be specified by the caller.
            NOTE: It can be safely assumed that this field will only be
            present in case of granular items restore only.
        target_doc_lib_prefix (string): If alternate site is provided,
            customer may want to provide a custom prefix to document libraries
            that we create. In any case we would also have to distinguish the
            newly created document library as the alternate site provided by
            the customer may as well turn out to be the original backup site.
        target_site (EntityProto):  This is the site in whose drive the items will be restored.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "restore_to_original": 'restoreToOriginal',
        "site_owner_vec": 'siteOwnerVec',
        "target_doc_lib_name": 'targetDocLibName',
        "target_doc_lib_prefix": 'targetDocLibPrefix',
        "target_site":'targetSite'
    }

    def __init__(self,
                 restore_to_original=None,
                 site_owner_vec=None,
                 target_doc_lib_name=None,
                 target_doc_lib_prefix=None,
                 target_site=None):
        """Constructor for the RestoreSiteParams class"""

        # Initialize members of the class
        self.restore_to_original = restore_to_original
        self.site_owner_vec = site_owner_vec
        self.target_doc_lib_name = target_doc_lib_name
        self.target_doc_lib_prefix = target_doc_lib_prefix
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
        restore_to_original = dictionary.get('restoreToOriginal')
        site_owner_vec = None
        if dictionary.get('siteOwnerVec') != None:
            site_owner_vec = list()
            for structure in dictionary.get('siteOwnerVec'):
                site_owner_vec.append(cohesity_management_sdk.models.restore_site_params_site_owner.RestoreSiteParams_SiteOwner.from_dictionary(structure))
        target_doc_lib_name = dictionary.get('targetDocLibName')
        target_doc_lib_prefix = dictionary.get('targetDocLibPrefix')
        target_site = cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(dictionary.get('targetSite')) if dictionary.get('targetSite') else None

        # Return an object of this model
        return cls(restore_to_original,
                   site_owner_vec,
                   target_doc_lib_name,
                   target_doc_lib_prefix,
                   target_site)


