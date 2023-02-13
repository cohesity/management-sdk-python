# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.aag_and_databases
import cohesity_management_sdk.models.protection_source_node
import cohesity_management_sdk.models.protection_source

class SqlAagHostAndDatabases(object):

    """Implementation of the 'SqlAagHostAndDatabases' model.

    Specifies AAGs and databases information on an SQL server. If AAGs exist
    on the server, specifies information about the AAG and databases in the
    group for each AAG found on the server.

    Attributes:
        aag_databases (list of AagAndDatabases): Specifies a list of AAGs and
            database members in each AAG.
        application_node (ProtectionSourceNode): Many different node types are
            supported such as 'kComputeResource' and 'kResourcePool'.
        databases (list of ProtectionSource): Specifies all database entities
            found on the server. Database may or may not be in an AAG.
        error_message (string): Specifies an error message when the host is
            not registered as an SQL host.
        unknown_host_name (string): Specifies the name of the host that is not
            registered as an SQL server on Cohesity Cluser.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "aag_databases":'aagDatabases',
        "application_node":'applicationNode',
        "databases":'databases',
        "error_message":'errorMessage',
        "unknown_host_name":'unknownHostName'
    }

    def __init__(self,
                 aag_databases=None,
                 application_node=None,
                 databases=None,
                 error_message=None,
                 unknown_host_name=None):
        """Constructor for the SqlAagHostAndDatabases class"""

        # Initialize members of the class
        self.aag_databases = aag_databases
        self.application_node = application_node
        self.databases = databases
        self.error_message = error_message
        self.unknown_host_name = unknown_host_name


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
        aag_databases = None
        if dictionary.get('aagDatabases') != None:
            aag_databases = list()
            for structure in dictionary.get('aagDatabases'):
                aag_databases.append(cohesity_management_sdk.models.aag_and_databases.AagAndDatabases.from_dictionary(structure))
        application_node = cohesity_management_sdk.models.protection_source_node.ProtectionSourceNode.from_dictionary(dictionary.get('applicationNode')) if dictionary.get('applicationNode') else None
        databases = None
        if dictionary.get('databases') != None:
            databases = list()
            for structure in dictionary.get('databases'):
                databases.append(cohesity_management_sdk.models.protection_source.ProtectionSource.from_dictionary(structure))
        error_message = dictionary.get('errorMessage')
        unknown_host_name = dictionary.get('unknownHostName')

        # Return an object of this model
        return cls(aag_databases,
                   application_node,
                   databases,
                   error_message,
                   unknown_host_name)


