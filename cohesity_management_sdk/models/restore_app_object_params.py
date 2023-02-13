# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.restore_ad_app_object_params
import cohesity_management_sdk.models.restore_oracle_app_object_params
import cohesity_management_sdk.models.restore_sql_app_object_params
import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.restore_exchange_params

class RestoreAppObjectParams(object):

    """Implementation of the 'RestoreAppObjectParams' model.

    TODO: type model description here.

    Attributes:
        ad_restore_params (RestoreADAppObjectParams): TODO: type description
            here.
        clone_task_id (long|int): Id of finished clone task which has to be
            refreshed with different data.
        exchange_restore_params(RestoreExchangeParams): The Exchange specific
            application object restore params. Only applicable if the
            RestoreAppObject.app_entity is of type kExchange.
        oracle_restore_params (RestoreOracleAppObjectParams): TODO: type
            description here.
        sql_restore_params (RestoreSqlAppObjectParams): TODO: type description
            here.
        target_host (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        target_host_parent_source (EntityProto): Specifies the attributes and
            the latest statistics about an entity.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ad_restore_params":'adRestoreParams',
        "clone_task_id":'cloneTaskId',
        "exchange_restore_params":'exchangeRestoreParams',
        "oracle_restore_params":'oracleRestoreParams',
        "sql_restore_params":'sqlRestoreParams',
        "target_host":'targetHost',
        "target_host_parent_source":'targetHostParentSource'
    }

    def __init__(self,
                 ad_restore_params=None,
                 clone_task_id=None,
                 exchange_restore_params=None,
                 oracle_restore_params=None,
                 sql_restore_params=None,
                 target_host=None,
                 target_host_parent_source=None):
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
        return cls(ad_restore_params,
                   clone_task_id,
                   exchange_restore_params,
                   oracle_restore_params,
                   sql_restore_params,
                   target_host,
                   target_host_parent_source)


