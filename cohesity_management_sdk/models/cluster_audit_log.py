# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.tenant

class ClusterAuditLog(object):

    """Implementation of the 'ClusterAuditLog' model.

    Specifies information about a single Cluster audit log.
    When an action (such as pausing a Protection Job) occurs, an audit log is
    generated that provides details about the action.

    Attributes:
        action (string): Specifies the action that caused the log to be
            generated.
        cluster_info (string): Specifies the information of the cluster.
        details (string): Specifies more information about the action.
        domain (string): Specifies the domain of the user who caused the
            action that generated the log.
        entity_id (string): Specifies the id of the entity (object) that the
            action is invoked on.
        entity_name (string): Specifies the entity (object) name that the
            action is invoked on. For example, if a Job called BackupEng is
            paused, this field returns BackupEng.
        entity_type (string): Specifies the type of the entity (object) that
            the action is invoked on. For example, if a Job called BackupEng
            is paused, this field returns 'Protection Job'.
        human_timestamp (string): Specifies the time when the log was
            generated. The time is specified using a human readable
            timestamp.
        impersonation (bool): Specifies if the log was generated during
            impersonation.
        ip (string): Specifies the IP address of the user making this action.
        new_record (string): Specifies the record after the action is
            invoked.
        original_tenant (Tenant): Specifies details about a tenant.
        previous_record (string): Specifies the record before the action is
            invoked.
        tenant (Tenant): Specifies details about a tenant.
        timestamp_usecs (long|int): Specifies the time when the log was
            generated. The time is specified using a Unix epoch Timestamp (in
            microseconds).
        user_name (string): Specifies the user who caused the action that
            generated the log.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "action":'action',
        "cluster_info":'clusterInfo',
        "details":'details',
        "domain":'domain',
        "entity_id":'entityId',
        "entity_name":'entityName',
        "entity_type":'entityType',
        "human_timestamp":'humanTimestamp',
        "impersonation":'impersonation',
        "ip":'ip',
        "new_record":'newRecord',
        "original_tenant":'originalTenant',
        "previous_record":'previousRecord',
        "tenant":'tenant',
        "timestamp_usecs":'timestampUsecs',
        "user_name":'userName'
    }

    def __init__(self,
                 action=None,
                 cluster_info=None,
                 details=None,
                 domain=None,
                 entity_id=None,
                 entity_name=None,
                 entity_type=None,
                 human_timestamp=None,
                 impersonation=None,
                 ip=None,
                 new_record=None,
                 original_tenant=None,
                 previous_record=None,
                 tenant=None,
                 timestamp_usecs=None,
                 user_name=None):
        """Constructor for the ClusterAuditLog class"""

        # Initialize members of the class
        self.action = action
        self.cluster_info = cluster_info
        self.details = details
        self.domain = domain
        self.entity_id = entity_id
        self.entity_name = entity_name
        self.entity_type = entity_type
        self.human_timestamp = human_timestamp
        self.impersonation = impersonation
        self.ip = ip
        self.new_record = new_record
        self.original_tenant = original_tenant
        self.previous_record = previous_record
        self.tenant = tenant
        self.timestamp_usecs = timestamp_usecs
        self.user_name = user_name


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
        action = dictionary.get('action')
        cluster_info = dictionary.get('clusterInfo')
        details = dictionary.get('details')
        domain = dictionary.get('domain')
        entity_id = dictionary.get('entityId')
        entity_name = dictionary.get('entityName')
        entity_type = dictionary.get('entityType')
        human_timestamp = dictionary.get('humanTimestamp')
        impersonation = dictionary.get('impersonation')
        ip = dictionary.get('ip')
        new_record = dictionary.get('newRecord')
        original_tenant = cohesity_management_sdk.models.tenant.Tenant.from_dictionary(dictionary.get('originalTenant')) if dictionary.get('originalTenant') else None
        previous_record = dictionary.get('previousRecord')
        tenant = cohesity_management_sdk.models.tenant.Tenant.from_dictionary(dictionary.get('tenant')) if dictionary.get('tenant') else None
        timestamp_usecs = dictionary.get('timestampUsecs')
        user_name = dictionary.get('userName')

        # Return an object of this model
        return cls(action,
                   cluster_info,
                   details,
                   domain,
                   entity_id,
                   entity_name,
                   entity_type,
                   human_timestamp,
                   impersonation,
                   ip,
                   new_record,
                   original_tenant,
                   previous_record,
                   tenant,
                   timestamp_usecs,
                   user_name)


