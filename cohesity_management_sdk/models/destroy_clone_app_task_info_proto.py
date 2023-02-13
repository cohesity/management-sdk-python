# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.error_proto
import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.credentials

class DestroyCloneAppTaskInfoProto(object):

    """Implementation of the 'DestroyCloneAppTaskInfoProto' model.

    Each available extension is listed below along with the location of the
    proto file (relative to magneto/connectors) where it is defined.
    DestroyCloneAppTaskInfoProto extension
    Location
    Extension
    ===========================================================================
    ==
    sql::DestroyCloneTaskInfo::sql_destroy_clone_app_task_info
    sql/sql.proto
    100
    oracle::DestroyCloneTaskInfo::oracle_destroy_clone_app_task_info
    oracle/oracle.proto
    101
    ad::DestroyTaskInfo::ad_destroy_app_task_info
    ad/ad.proto
    102
    exchange::DestroyTaskInfo::exchange_destroy_app_task_info
    exchange/exchange.proto
    103
    ===========================================================================
    ==

    Attributes:
        app_env (int): The application environment.
        error (ErrorProto): TODO: type description here.
        finished (bool): This will be set to true if the task is complete on
            the slave.
        target_entity (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        target_entity_credentials (Credentials): Specifies credentials to
            access a target source.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "app_env":'appEnv',
        "error":'error',
        "finished":'finished',
        "target_entity":'targetEntity',
        "target_entity_credentials":'targetEntityCredentials'
    }

    def __init__(self,
                 app_env=None,
                 error=None,
                 finished=None,
                 target_entity=None,
                 target_entity_credentials=None):
        """Constructor for the DestroyCloneAppTaskInfoProto class"""

        # Initialize members of the class
        self.app_env = app_env
        self.error = error
        self.finished = finished
        self.target_entity = target_entity
        self.target_entity_credentials = target_entity_credentials


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
        app_env = dictionary.get('appEnv')
        error = cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(dictionary.get('error')) if dictionary.get('error') else None
        finished = dictionary.get('finished')
        target_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('targetEntity')) if dictionary.get('targetEntity') else None
        target_entity_credentials = cohesity_management_sdk.models.credentials.Credentials.from_dictionary(dictionary.get('targetEntityCredentials')) if dictionary.get('targetEntityCredentials') else None

        # Return an object of this model
        return cls(app_env,
                   error,
                   finished,
                   target_entity,
                   target_entity_credentials)


