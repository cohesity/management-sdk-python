# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.oracle_pluggable_database_info

class OracleContainerDatabaseInfo(object):

    """Implementation of the 'OracleContainerDatabaseInfo' model.

    Specifies the Container Database information along with the Pluggable DBs
    within the container.
    The multitenant architecture enables an Oracle database to function as a
    multitenant container database (CDB). A CDB includes zero, one, or many
    customer-created pluggable databases (PDBs).

    Attributes:
        pluggable_database_info_list (list of OraclePluggableDatabaseInfo):
            Specifies the list of Pluggable databases within this Container
            Database.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "pluggable_database_info_list":'pluggableDatabaseInfoList'
    }

    def __init__(self,
                 pluggable_database_info_list=None):
        """Constructor for the OracleContainerDatabaseInfo class"""

        # Initialize members of the class
        self.pluggable_database_info_list = pluggable_database_info_list


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
        pluggable_database_info_list = None
        if dictionary.get('pluggableDatabaseInfoList') != None:
            pluggable_database_info_list = list()
            for structure in dictionary.get('pluggableDatabaseInfoList'):
                pluggable_database_info_list.append(cohesity_management_sdk.models.oracle_pluggable_database_info.OraclePluggableDatabaseInfo.from_dictionary(structure))

        # Return an object of this model
        return cls(pluggable_database_info_list)


