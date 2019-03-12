# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.source_for_principal_parameters

class UpdateSourcesForPrincipalParameters(object):

    """Implementation of the 'Update Sources for Principal Parameters.' model.

    Set Access Permissions for Principals.
    Specifies a list of principals to set access permissions for.
    For each principal, set the Protection Sources and View names
    that the specified principal has permissions to access.

    Attributes:
        sources_for_principals (list of SourceForPrincipalParameters): Array
            of Principals, Sources and Views.  Specifies a list of principals.
            For each principal, specify the Protection Sources and Views that
            the principal has permissions to access.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "sources_for_principals":'sourcesForPrincipals'
    }

    def __init__(self,
                 sources_for_principals=None):
        """Constructor for the UpdateSourcesForPrincipalParameters class"""

        # Initialize members of the class
        self.sources_for_principals = sources_for_principals


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
        sources_for_principals = None
        if dictionary.get('sourcesForPrincipals') != None:
            sources_for_principals = list()
            for structure in dictionary.get('sourcesForPrincipals'):
                sources_for_principals.append(cohesity_management_sdk.models.source_for_principal_parameters.SourceForPrincipalParameters.from_dictionary(structure))

        # Return an object of this model
        return cls(sources_for_principals)


