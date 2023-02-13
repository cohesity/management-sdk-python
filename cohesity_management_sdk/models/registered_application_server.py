# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.protection_source_node
import cohesity_management_sdk.models.protection_source

class RegisteredApplicationServer(object):

    """Implementation of the 'RegisteredApplicationServer' model.

    Specifies an Application Server and the Protection Source that registered
    the Application Server.

    Attributes:
        application_server (ProtectionSourceNode): Specifies the child subtree
            used to store additional application-level Objects. Different
            environments use the subtree to store application-level
            information. For example for SQL Server, this subtree stores the
            SQL Server instances running on a VM.
        registered_protection_source (ProtectionSource): Specifies the
            Protection Source like a VM or Physical Server that registered the
            Application Server.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "application_server":'applicationServer',
        "registered_protection_source":'registeredProtectionSource'
    }

    def __init__(self,
                 application_server=None,
                 registered_protection_source=None):
        """Constructor for the RegisteredApplicationServer class"""

        # Initialize members of the class
        self.application_server = application_server
        self.registered_protection_source = registered_protection_source


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
        application_server = cohesity_management_sdk.models.protection_source_node.ProtectionSourceNode.from_dictionary(dictionary.get('applicationServer')) if dictionary.get('applicationServer') else None
        registered_protection_source = cohesity_management_sdk.models.protection_source.ProtectionSource.from_dictionary(dictionary.get('registeredProtectionSource')) if dictionary.get('registeredProtectionSource') else None

        # Return an object of this model
        return cls(application_server,
                   registered_protection_source)


