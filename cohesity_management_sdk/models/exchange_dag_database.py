# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.exchange_database_copy_info

class ExchangeDAGDatabase(object):

    """Implementation of the 'ExchangeDAGDatabase' model.

    Specifies the information about all the copies of the database that is
    part of DAG.

    Attributes:
        database_copy_info_list (list of ExchangeDatabaseCopyInfo): Specifies
            about all the copies of this DAG database. This include active and
            passive copy of the database.
        guid (string): Specifies the guid of the database.
        name (string): Specifes the name of the database.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "database_copy_info_list":'databaseCopyInfoList',
        "guid":'guid',
        "name":'name'
    }

    def __init__(self,
                 database_copy_info_list=None,
                 guid=None,
                 name=None):
        """Constructor for the ExchangeDAGDatabase class"""

        # Initialize members of the class
        self.database_copy_info_list = database_copy_info_list
        self.guid = guid
        self.name = name


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
        guid = dictionary.get('guid')
        name = dictionary.get('name')

        # Return an object of this model
        return cls(database_copy_info_list,
                   guid,
                   name)


