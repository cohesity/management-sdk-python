# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.dag_application_server_info
import cohesity_management_sdk.models.exchange_dag_protection_preference

class DagInfo(object):

    """Implementation of the 'DagInfo' model.

    Specifies the information about the DAG(Database availability group).

    Attributes:
        dag_application_server_info_list (list of DagApplicationServerInfo):
            Specifies the status of all the Exchange Application Servers that
            are part of this DAG.
        exchange_dag_protection_preference (ExchangeDAGProtectionPreference):
            Specifies information about the preference order while choosing
            between which database copy of the database which is part of DAG
            should be protected.
        guid (string): Specifies Unique GUID for the DAG.
        name (string): Specifies display name of the DAG.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dag_application_server_info_list":'dagApplicationServerInfoList',
        "exchange_dag_protection_preference":'exchangeDagProtectionPreference',
        "guid":'guid',
        "name":'name'
    }

    def __init__(self,
                 dag_application_server_info_list=None,
                 exchange_dag_protection_preference=None,
                 guid=None,
                 name=None):
        """Constructor for the DagInfo class"""

        # Initialize members of the class
        self.dag_application_server_info_list = dag_application_server_info_list
        self.exchange_dag_protection_preference = exchange_dag_protection_preference
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
        dag_application_server_info_list = None
        if dictionary.get('dagApplicationServerInfoList') != None:
            dag_application_server_info_list = list()
            for structure in dictionary.get('dagApplicationServerInfoList'):
                dag_application_server_info_list.append(cohesity_management_sdk.models.dag_application_server_info.DagApplicationServerInfo.from_dictionary(structure))
        exchange_dag_protection_preference = cohesity_management_sdk.models.exchange_dag_protection_preference.ExchangeDAGProtectionPreference.from_dictionary(dictionary.get('exchangeDagProtectionPreference')) if dictionary.get('exchangeDagProtectionPreference') else None
        guid = dictionary.get('guid', None)
        name = dictionary.get('name', None)

        # Return an object of this model
        return cls(dag_application_server_info_list,
                   exchange_dag_protection_preference,
                   guid,
                   name)


