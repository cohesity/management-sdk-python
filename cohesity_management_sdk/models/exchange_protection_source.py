# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.dag_info
import cohesity_management_sdk.models.application_server_info
import cohesity_management_sdk.models.exchange_database_copy_info
import cohesity_management_sdk.models.exchange_dag_database
import cohesity_management_sdk.models.exchange_database_info

class ExchangeProtectionSource(object):

    """Implementation of the 'ExchangeProtectionSource' model.

    Specifies an object representing an Exchange entity.
    DAG - Database availability group

    Attributes:
        dag_info (DagInfo): Specifies the Exchange DAG information if
            ExchangeProtectionSourceType is 'kExchangeDAG'.
        application_server_info (ApplicationServerInfo): Specifies the
            Exchange Application server information if
            ExchangeProtectionSourceType is 'kExhangeNode'
        dag_database_copy_info (ExchangeDatabaseCopyInfo): Specifies the
            Exchange DAG Database copy information if
            ExchangeProtectionSourceType is 'kExchangeDAGDatabaseCopy'.
        dag_database_info (ExchangeDAGDatabase): Specifies the Exchange DAG
            Database information if ExchangeProtectionSourceType is
            'kExchangeDAGDatabase'
        name (string): TODO: add description here.
        owner_id (int): Specifies the entity id of the owner of the Exchange
            Protection Source.
        standalone_database_copy_info (ExchangeDatabaseInfo): Specifies the
            Exchange Standalone Database information if
            ExchangeProtectionSourceType is 'kExchangeStandaloneDatabase'.
        mtype (int): Specifies the type of the Exchange Protection Source.
        uuid (string): Specifies the UUID for the Exchange entity.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dag_info": 'DagInfo',
        "application_server_info": 'applicationServerInfo',
        "dag_database_copy_info":'dagDatabaseCopyInfo',
        "dag_database_info":'dagDatabaseInfo',
        "name": 'name',
        "owner_id":'ownerId',
        "standalone_database_copy_info":'standaloneDatabaseCopyInfo',
        "mtype": 'type',
        "uuid":'uuid'
    }

    def __init__(self,
                 dag_info=None,
                 application_server_info=None,
                 dag_database_copy_info=None,
                 dag_database_info=None,
                 name=None,
                 owner_id=None,
                 standalone_database_copy_info=None,
                 mtype=None,
                 uuid=None):
        """Constructor for the ExchangeProtectionSource class"""

        # Initialize members of the class
        self.dag_info = dag_info
        self.application_server_info = application_server_info
        self.dag_database_copy_info = dag_database_copy_info
        self.dag_database_info = dag_database_info
        self.name = name
        self.owner_id = owner_id
        self.standalone_database_copy_info = standalone_database_copy_info
        self.mtype = mtype
        self.uuid = uuid

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
        dag_info = cohesity_management_sdk.models.dag_info.DagInfo.from_dictionary(dictionary.get('DagInfo')) if dictionary.get('DagInfo') else None
        application_server_info = cohesity_management_sdk.models.application_server_info.ApplicationServerInfo.from_dictionary(dictionary.get('applicationServerInfo')) if dictionary.get('applicationServerInfo') else None
        dag_database_copy_info = cohesity_management_sdk.models.exchange_database_copy_info.ExchangeDatabaseCopyInfo.from_dictionary(dictionary.get('dagDatabaseCopyInfo')) if dictionary.get('dagDatabaseCopyInfo') else None
        dag_database_info = cohesity_management_sdk.models.exchange_dag_database.ExchangeDAGDatabase.from_dictionary(dictionary.get('dagDatabaseInfo')) if dictionary.get('dagDatabaseInfo') else None
        name = dictionary.get('name')
        owner_id = dictionary.get('ownerId')
        standalone_database_copy_info = cohesity_management_sdk.models.exchange_database_info.ExchangeDatabaseInfo.from_dictionary(dictionary.get('standaloneDatabaseCopyInfo')) if dictionary.get('standaloneDatabaseCopyInfo') else None
        mtype = dictionary.get('type')
        uuid = dictionary.get('uuid')

        # Return an object of this model
        return cls(dag_info,
                   application_server_info,
                   dag_database_copy_info,
                   dag_database_info,
                   name,
                   owner_id,
                   standalone_database_copy_info,
                   mtype,
                   uuid)


