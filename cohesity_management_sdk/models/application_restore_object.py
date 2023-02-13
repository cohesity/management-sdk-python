# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.ad_restore_parameters
import cohesity_management_sdk.models.exchange_restore_parameters
import cohesity_management_sdk.models.sql_restore_parameters

class ApplicationRestoreObject(object):

    """Implementation of the 'ApplicationRestoreObject' model.

    Specifies the Application Server to restore and parameters specific to
    that application.

    Attributes:
        ad_restore_parameters (AdRestoreParameters): Specifies the parameters
            specific to Application domain controller.
        application_server_id (long|int): Specifies the Application Server to
            restore (for example, kSQL).
        exchange_restore_parameters (ExchangeRestoreParameters): Specifies
             parameters speicific to Exchange Application Server.
        sql_restore_parameters (SqlRestoreParameters): Specifies the
            parameters specific the Application Server instance.
        target_host_id (long|int): Specifies the target host if the
            application is to be restored to a different host. If this is
            empty, then the application is restored to the original host,
            which is the hosting Protection Source.
        target_root_node_id (long|int): Specifies the registered root node,
            like vCenter, of targetHost. If this is empty, then it is assumed
            the root node of the target host is the same as the host
            Protection Source of the application.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ad_restore_parameters":'adRestoreParameters',
        "application_server_id":'applicationServerId',
        "exchange_restore_parameters":'exchangeRestoreParameters',
        "sql_restore_parameters":'sqlRestoreParameters',
        "target_host_id":'targetHostId',
        "target_root_node_id":'targetRootNodeId'
    }

    def __init__(self,
                 ad_restore_parameters=None,
                 application_server_id=None,
                 exchange_restore_parameters=None,
                 sql_restore_parameters=None,
                 target_host_id=None,
                 target_root_node_id=None):
        """Constructor for the ApplicationRestoreObject class"""

        # Initialize members of the class
        self.ad_restore_parameters = ad_restore_parameters
        self.application_server_id = application_server_id
        self.exchange_restore_parameters = exchange_restore_parameters
        self.sql_restore_parameters = sql_restore_parameters
        self.target_host_id = target_host_id
        self.target_root_node_id = target_root_node_id


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
        ad_restore_parameters = cohesity_management_sdk.models.ad_restore_parameters.AdRestoreParameters.from_dictionary(dictionary.get('adRestoreParameters')) if dictionary.get('adRestoreParameters') else None
        application_server_id = dictionary.get('applicationServerId')
        sql_restore_parameters = cohesity_management_sdk.models.sql_restore_parameters.SqlRestoreParameters.from_dictionary(dictionary.get('sqlRestoreParameters')) if dictionary.get('sqlRestoreParameters') else None
        target_host_id = dictionary.get('targetHostId')
        target_root_node_id = dictionary.get('targetRootNodeId')
        exchange_restore_parameters = cohesity_management_sdk.models.exchange_restore_parameters.ExchangeRestoreParameters.from_dictionary(dictionary.get('exchangeRestoreParameters')) if dictionary.get('exchangeRestoreParameters') else None
        # Return an object of this model
        return cls(ad_restore_parameters,
                   application_server_id,
                   exchange_restore_parameters,
                   sql_restore_parameters,
                   target_host_id,
                   target_root_node_id)


