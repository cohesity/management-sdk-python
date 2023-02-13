# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.oracle_db_config

class RestoreOracleAppObjectParamsAlternateLocationParams(object):

    """Implementation of the 'RestoreOracleAppObjectParams_AlternateLocationParams' model.

    For restoring to alternate location this message can not be empty and all
    the fields inside the message also can not be empty.

    Attributes:
        base_dir (string): Base directory of Oracle at destination. Example :
            /u01/app/oracle
        database_file_destination (string): Location to put the database
            files(datafiles, logfiles etc.).
        home_dir (string): Home directory of Oracle at destination. Example :
            /u01/app/oracle/product/11.2.0.3/db_1
        new_database_name (string): The name of the Oracle database that we
            restore to.
        new_sid_deprecated (string): Deprecated field SID of new Oracle
            database.
        oracle_db_config (OracleDBConfig): This proto captures the oracle
            database configuration for alternate DB restore.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "base_dir":'baseDir',
        "database_file_destination":'databaseFileDestination',
        "home_dir":'homeDir',
        "new_database_name":'newDatabaseName',
        "new_sid_deprecated":'newSidDeprecated',
        "oracle_db_config":'oracleDbConfig'
    }

    def __init__(self,
                 base_dir=None,
                 database_file_destination=None,
                 home_dir=None,
                 new_database_name=None,
                 new_sid_deprecated=None,
                 oracle_db_config=None):
        """Constructor for the RestoreOracleAppObjectParamsAlternateLocationParams class"""

        # Initialize members of the class
        self.base_dir = base_dir
        self.database_file_destination = database_file_destination
        self.home_dir = home_dir
        self.new_database_name = new_database_name
        self.new_sid_deprecated = new_sid_deprecated
        self.oracle_db_config = oracle_db_config


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
        base_dir = dictionary.get('baseDir')
        database_file_destination = dictionary.get('databaseFileDestination')
        home_dir = dictionary.get('homeDir')
        new_database_name = dictionary.get('newDatabaseName')
        new_sid_deprecated = dictionary.get('newSidDeprecated')
        oracle_db_config = cohesity_management_sdk.models.oracle_db_config.OracleDBConfig.from_dictionary(dictionary.get('oracleDbConfig')) if dictionary.get('oracleDbConfig') else None

        # Return an object of this model
        return cls(base_dir,
                   database_file_destination,
                   home_dir,
                   new_database_name,
                   new_sid_deprecated,
                   oracle_db_config)


