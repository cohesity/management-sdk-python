# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.cluster_audit_log
import cohesity_management_sdk.models.gdpr_copy_task
import cohesity_management_sdk.models.protection_info

class ObjectInformation(object):

    """Implementation of the 'ObjectInformation' model.

    Attributes:
        accessible_users (list of string): Species the list of user who have
            access to this object.
        audit_logs (list of ClusterAuditLog): Specifies the audit log
            information.
        copy_task_info (list of GdprCopyTask): Specifies the copy task
            information.
        is_protected (bool): Specifies the protection status of the object.
        location (string): Specifies the location of the parent source.
        protection_info (list of ProtectionInfo): Specifies the data locations
            for the protected objects.
        root_node_id (int|long): Specifies the id of the root node.
        source_id (long|int): Specifies the id of the Protection Source.
        source_name (string): Specifies the name of the object.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "accessible_users":'accessibleUsers',
        "audit_logs":'auditLogs',
        "copy_task_info":'copyTaskInfo',
        "is_protected":'isProtected',
        "location":'location',
        "protection_info":'protectionInfo',
        "root_node_id":'rootNodeId',
        "source_id":'sourceId',
        "source_name":'sourceName'
    }

    def __init__(self,
                 accessible_users=None,
                 audit_logs=None,
                 copy_task_info=None,
                 is_protected=None,
                 location=None,
                 protection_info=None,
                 root_node_id=None,
                 source_id=None,
                 source_name=None):
        """Constructor for the ObjectInformation class"""

        # Initialize members of the class
        self.accessible_users = accessible_users
        self.audit_logs = audit_logs
        self.copy_task_info = copy_task_info
        self.is_protected = is_protected
        self.location = location
        self.protection_info = protection_info
        self.root_node_id = root_node_id
        self.source_id = source_id
        self.source_name = source_name


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
        accessible_users = dictionary.get('accessibleUsers')
        audit_logs = None
        if dictionary.get('auditLogs') != None:
            audit_logs = list()
            for structure in dictionary.get('auditLogs'):
                audit_logs.append(cohesity_management_sdk.models.cluster_audit_log.ClusterAuditLog.from_dictionary(structure))
        copy_task_info = None
        if dictionary.get('copyTaskInfo') != None:
            copy_task_info = list()
            for structure in dictionary.get('copyTaskInfo'):
                copy_task_info.append(cohesity_management_sdk.models.gdpr_copy_task.GdprCopyTask.from_dictionary(structure))
        is_protected = dictionary.get('isProtected')
        location = dictionary.get('location')
        protection_info = None
        if dictionary.get('protectionInfo') != None:
            protection_info = list()
            for structure in dictionary.get('protectionInfo'):
                protection_info.append(cohesity_management_sdk.models.protection_info.ProtectionInfo.from_dictionary(structure))
        root_node_id = dictionary.get('rootNodeId')
        source_id = dictionary.get('sourceId')
        source_name = dictionary.get('sourceName')

        # Return an object of this model
        return cls(accessible_users,
                   audit_logs,
                   copy_task_info,
                   is_protected,
                   location,
                   protection_info,
                   root_node_id,
                   source_id,
                   source_name)


