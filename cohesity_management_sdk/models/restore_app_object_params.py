# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.restore_ad_app_object_params
import cohesity_management_sdk.models.restore_exchange_params
import cohesity_management_sdk.models.restore_oracle_app_object_params
import cohesity_management_sdk.models.restore_sql_app_object_params


class RestoreAppObjectParams(object):

    """Implementation of the 'RestoreAppObjectParams' model.

    TODO: type description here.


    Attributes:

        ad_restore_params (RestoreADAppObjectParams): The AD specific
            application object restore params. Only applicable if the
            RestoreAppObject.app_entity is of type kAD.
        clone_task_id (long|int): Id of finished clone task which has to be
            refreshed with different data.
        exchange_restore_params (RestoreExchangeParams): The Exchange specific
            application object restore params. Only applicable if the
            RestoreAppObject.app_entity is of type kExchange.
        oracle_restore_params (RestoreOracleAppObjectParams): Note: Only one of
            sql_restore_params and oracle_restore_params can be set.
        sql_restore_params (RestoreSqlAppObjectParams): The SQL specific
            application object restore params. Only applicable if the
            RestoreAppObject.app_entity is of type kSQL.
        target_host (EntityProto): The target host if the application is to be
            restored to a different host. If this is empty, then we are
            restoring to the original host, which is the owner entity.
        target_host_parent_source (EntityProto): The registered source managing
            the target host. If this is empty, then the target host has the
            same parent source as the owner entity.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "ad_restore_params":'adRestoreParams',
        "clone_task_id":'cloneTaskId',
        "exchange_restore_params":'exchangeRestoreParams',
        "oracle_restore_params":'oracleRestoreParams',
        "sql_restore_params":'sqlRestoreParams',
        "target_host":'targetHost',
        "target_host_parent_source":'targetHostParentSource',
    }
    def __init__(self,
                 ad_restore_params=None,
                 clone_task_id=None,
                 exchange_restore_params=None,
                 oracle_restore_params=None,
                 sql_restore_params=None,
                 target_host=None,
                 target_host_parent_source=None,
            ):

        """Constructor for the RestoreAppObjectParams class"""

        # Initialize members of the class
        self.ad_restore_params = ad_restore_params
        self.clone_task_id = clone_task_id
        self.exchange_restore_params = exchange_restore_params
        self.oracle_restore_params = oracle_restore_params
        self.sql_restore_params = sql_restore_params
        self.target_host = target_host
        self.target_host_parent_source = target_host_parent_source

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
        ad_restore_params = cohesity_management_sdk.models.restore_ad_app_object_params.RestoreADAppObjectParams.from_dictionary(dictionary.get('adRestoreParams')) if dictionary.get('adRestoreParams') else None
        clone_task_id = dictionary.get('cloneTaskId')
        exchange_restore_params = cohesity_management_sdk.models.restore_exchange_params.RestoreExchangeParams.from_dictionary(dictionary.get('exchangeRestoreParams')) if dictionary.get('exchangeRestoreParams') else None
        oracle_restore_params = cohesity_management_sdk.models.restore_oracle_app_object_params.RestoreOracleAppObjectParams.from_dictionary(dictionary.get('oracleRestoreParams')) if dictionary.get('oracleRestoreParams') else None
        sql_restore_params = cohesity_management_sdk.models.restore_sql_app_object_params.RestoreSqlAppObjectParams.from_dictionary(dictionary.get('sqlRestoreParams')) if dictionary.get('sqlRestoreParams') else None
        target_host = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('targetHost')) if dictionary.get('targetHost') else None
        target_host_parent_source = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('targetHostParentSource')) if dictionary.get('targetHostParentSource') else None

        # Return an object of this model
        return cls(
            ad_restore_params,
            clone_task_id,
            exchange_restore_params,
            oracle_restore_params,
            sql_restore_params,
            target_host,
            target_host_parent_source
)