# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class SearchProductionAdObjectsRequest(object):

    """Implementation of the 'SearchProductionAdObjectsRequest' model.

    Specifies the request to search AD objects from Production AD.

    Attributes:
        distinguished_names (list of string): Specifies the list of the
            distinguished names of the AD objects.
        object_guids (list of string): Specifies the list of the guids of the
            AD objects.
        protection_source_id (long|int): ProtectionSourceId is the Id of the
            Domain Controller host on which we want to search for AD objects.
        sam_account_names (list of string): Specifies the list of the sam
            account names of the AD objects.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "distinguished_names":'distinguishedNames',
        "object_guids":'objectGuids',
        "protection_source_id":'protectionSourceId',
        "sam_account_names":'samAccountNames'
    }

    def __init__(self,
                 distinguished_names=None,
                 object_guids=None,
                 protection_source_id=None,
                 sam_account_names=None):
        """Constructor for the SearchProductionAdObjectsRequest class"""

        # Initialize members of the class
        self.distinguished_names = distinguished_names
        self.object_guids = object_guids
        self.protection_source_id = protection_source_id
        self.sam_account_names = sam_account_names


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
        distinguished_names = dictionary.get('distinguishedNames')
        object_guids = dictionary.get('objectGuids')
        protection_source_id = dictionary.get('protectionSourceId')
        sam_account_names = dictionary.get('samAccountNames')

        # Return an object of this model
        return cls(distinguished_names,
                   object_guids,
                   protection_source_id,
                   sam_account_names)


