# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.exchange_dag_protection_preference
import cohesity_management_sdk.models.exchange_host_info

class ExchangeDagHostsResponse(object):

    """Implementation of the 'ExchangeDagHostsResponse' model.

    Specifies if the endpoint provided in the request is standalone exchange
    server or not. If the endpoint is not a standalone exchange server, the
    list of hosts which belong to the Exchange DAG are returned.

    Attributes:
        exchange_dag_protection_preference (ExchangeDAGProtectionPreference):
            Specifies information about the preference order while choosing
            between which database copy of the exchange database, which is
            part of DAG, should be protected.Specifies the CA certificate in
            PEM format.
        exchange_host_info_list (list of ExchangeHostInfo): Specifies the list
            of exchange hosts that belong to Exchange DAG.
        guid (string): Specifies the Unique GUID for the DAG.
        is_standalone_host (bool): Specifies if the endpoint provided in the
            request is a standlone exchange server or not.
            exchangeHostInfoList is not populated if it is a standalone
            exchange server.
        name (string): Specifies the display name of the DAG.
        protection_source_id (int): Specifies the Protection Source Id of the
            Exchange DAG if it is already created.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "exchange_dag_protection_preference": 'exchangeDagProtectionPreference',
        "exchange_host_info_list": 'exchangeHostInfoList',
        "guid": 'guid',
        "is_standalone_host": 'isStandaloneHost',
        "name":'name',
        "protection_source_id":'protectionSourceId'
    }

    def __init__(self,
                 exchange_dag_protection_preference=None,
                 exchange_host_info_list=None,
                 guid=None,
                 is_standalone_host=None,
                 name=None,
                 protection_source_id=None):
        """Constructor for the ExchangeDagHostsResponse class"""

        # Initialize members of the class
        self.exchange_dag_protection_preference = exchange_dag_protection_preference
        self.exchange_host_info_list = exchange_host_info_list
        self.guid = guid
        self.is_standalone_host = is_standalone_host
        self.name = name
        self.protection_source_id = protection_source_id

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
        exchange_dag_protection_preference = cohesity_management_sdk.models.exchange_dag_protection_preference.ExchangeDAGProtectionPreference.from_dictionary(dictionary.get('exchangeDagProtectionPreference')) if dictionary.get('exchangeDagProtectionPreference') else None
        exchange_host_info_list = None
        if dictionary.get('exchangeHostInfoList') != None:
            exchange_host_info_list = list()
            for structure in dictionary.get('exchangeHostInfoList'):
                exchange_host_info_list.append(cohesity_management_sdk.models.exchange_host_info.ExchangeHostInfo.from_dictionary(structure))
        guid = dictionary.get('guid')
        is_standalone_host = dictionary.get('isStandaloneHost')
        name = dictionary.get('name')
        protection_source_id = dictionary.get('protectionSourceId')

        # Return an object of this model
        return cls(exchange_dag_protection_preference,
                   exchange_host_info_list,
                   guid,
                   is_standalone_host,
                   name,
                   protection_source_id)


