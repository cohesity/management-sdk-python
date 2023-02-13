# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.protection_source
import cohesity_management_sdk.models.view

class SourcesForSid(object):

    """Implementation of the 'SourcesForSid' model.

    Protection Sources and Views With Access Permissions.
    Specifies the Protection Sources objects and Views that the specified
    principal has permissions to access. The principal is specified using
    a security identifier (SID).

    Attributes:
        protection_sources (list of ProtectionSource): Array of Protection
            Sources.  Specifies the Protection Source objects that the
            specified principal has permissions to access.
        sid (string): Specifies the security identifier (SID) of the
            principal.
        views (list of View): Array of View Names.  Specifies the names of the
            Views that the specified principal has permissions to access.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "protection_sources":'protectionSources',
        "sid":'sid',
        "views":'views'
    }

    def __init__(self,
                 protection_sources=None,
                 sid=None,
                 views=None):
        """Constructor for the SourcesForSid class"""

        # Initialize members of the class
        self.protection_sources = protection_sources
        self.sid = sid
        self.views = views


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
        protection_sources = None
        if dictionary.get('protectionSources') != None:
            protection_sources = list()
            for structure in dictionary.get('protectionSources'):
                protection_sources.append(cohesity_management_sdk.models.protection_source.ProtectionSource.from_dictionary(structure))
        sid = dictionary.get('sid')
        views = None
        if dictionary.get('views') != None:
            views = list()
            for structure in dictionary.get('views'):
                views.append(cohesity_management_sdk.models.view.View.from_dictionary(structure))

        # Return an object of this model
        return cls(protection_sources,
                   sid,
                   views)


