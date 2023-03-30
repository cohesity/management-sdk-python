# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.protection_source


class AagAndDatabases(object):

    """Implementation of the 'AagAndDatabases' model.

    Specifies an AAG and the database members of the AAG.


    Attributes:

        aag (ProtectionSource): Specifies an AAG Protection Source object on a
            VM or a Physical host.
        databases (list of ProtectionSource): Specifies databases found that
            are members of the AAG.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "aag":'aag',
        "databases":'databases',
    }
    def __init__(self,
                 aag=None,
                 databases=None,
            ):

        """Constructor for the AagAndDatabases class"""

        # Initialize members of the class
        self.aag = aag
        self.databases = databases

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
        aag = cohesity_management_sdk.models.protection_source.ProtectionSource.from_dictionary(dictionary.get('aag')) if dictionary.get('aag') else None
        databases = None
        if dictionary.get('databases') != None:
            databases = list()
            for structure in dictionary.get('databases'):
                databases.append(cohesity_management_sdk.models.protection_source.ProtectionSource.from_dictionary(structure))

        # Return an object of this model
        return cls(
            aag,
            databases
)