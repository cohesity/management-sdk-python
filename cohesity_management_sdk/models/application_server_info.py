# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.exchange_database_copy_info
import cohesity_management_sdk.models.exchange_database_info

class ApplicationServerInfo(object):

    """Implementation of the 'ApplicationServerInfo' model.

    Specifies the Information about the Exchange Server Node.

    Attributes:
        database_copy_info_list (list of ExchangeDatabaseCopyInfo): Specifies
            the list of all the copies of the Exchange databases(that are part
            of DAG) that are present on this Exchange Node.
        database_info_list (list of ExchangeDatabaseInfo): Specifies the list
            of all the databases available on the standalone Exchange server
            node. This is populated for the Standlone Exchange Servers.
        fqdn (string): Specifies the fully qualified domain name of the
            Exchange Server.
        guid (string): Specifies the Guid of the Exchange Application Server.
        name (string): Specifies the display name of the Exchange
            Application Server.
        total_size_bytes (int):  Specifies the total size of all Exchange
            database copies in all the Exchange Application Servers that are
            part of the DAG.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "database_copy_info_list": 'databaseCopyInfoList',
        "database_info_list":'databaseInfoList',
        "fqdn": 'fqdn',
        "guid": 'guid',
        "name": 'name',
        "total_size_bytes":'totalSizeBytes'
    }

    def __init__(self,
                 database_copy_info_list=None,
                 database_info_list=None,
                 fqdn=None,
                 guid=None,
                 name=None,
                 total_size_bytes=None):
        """Constructor for the ApplicationServerInfo class"""

        # Initialize members of the class
        self.database_copy_info_list = database_copy_info_list
        self.database_info_list = database_info_list
        self.fqdn = fqdn
        self.guid = guid
        self.name = name
        self.total_size_bytes = total_size_bytes

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
        database_copy_info_list = None
        if dictionary.get('databaseCopyInfoList') != None:
            database_copy_info_list = list()
            for structure in dictionary.get('databaseCopyInfoList'):
                database_copy_info_list.append(cohesity_management_sdk.models.exchange_database_copy_info.ExchangeDatabaseCopyInfo.from_dictionary(structure))
        database_info_list = None
        if dictionary.get('databaseInfoList') != None:
            database_info_list = list()
            for structure in dictionary.get('databaseInfoList'):
                database_info_list.append(cohesity_management_sdk.models.exchange_database_info.ExchangeDatabaseInfo.from_dictionary(structure))
        fqdn = dictionary.get('fqdn')
        guid = dictionary.get('guid')
        name = dictionary.get('name')
        total_size_bytes = dictionary.get('totalSizeBytes')

        # Return an object of this model
        return cls(database_copy_info_list,
                   database_info_list,
                   fqdn,
                   guid,
                   name,
                   total_size_bytes)


