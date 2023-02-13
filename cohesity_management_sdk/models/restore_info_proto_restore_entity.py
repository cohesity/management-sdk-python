# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.error_proto

class RestoreInfoProtoRestoreEntity(object):

    """Implementation of the 'RestoreInfoProto_RestoreEntity' model.

    TODO: type model description here.

    Attributes:
        entity (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        error (ErrorProto): TODO: type description here.
        progress_monitor_task_path (string): The path relative to the root
            path of the restore task progress monitor of the progress monitor
            for this entity.
        public_status (int): Iris-facing task state. This field is stamped
            during the export.
        relative_restore_paths (list of string): All the paths that the
            entity's files were restored to. Each path is relative to the
            destination view.
        resource_pool_entity (EntityProto): Specifies the attributes and the
            latest statistics about an entity.
        restored_entity (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        status (int): The restore status of the entity.
        warnings (list of ErrorProto): Optional warnings if any.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "entity":'entity',
        "error":'error',
        "progress_monitor_task_path":'progressMonitorTaskPath',
        "public_status":'publicStatus',
        "relative_restore_paths":'relativeRestorePaths',
        "resource_pool_entity":'resourcePoolEntity',
        "restored_entity":'restoredEntity',
        "status":'status',
        "warnings":'warnings'
    }

    def __init__(self,
                 entity=None,
                 error=None,
                 progress_monitor_task_path=None,
                 public_status=None,
                 relative_restore_paths=None,
                 resource_pool_entity=None,
                 restored_entity=None,
                 status=None,
                 warnings=None):
        """Constructor for the RestoreInfoProtoRestoreEntity class"""

        # Initialize members of the class
        self.entity = entity
        self.error = error
        self.progress_monitor_task_path = progress_monitor_task_path
        self.public_status = public_status
        self.relative_restore_paths = relative_restore_paths
        self.resource_pool_entity = resource_pool_entity
        self.restored_entity = restored_entity
        self.status = status
        self.warnings = warnings


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
        entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('entity')) if dictionary.get('entity') else None
        error = cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(dictionary.get('error')) if dictionary.get('error') else None
        progress_monitor_task_path = dictionary.get('progressMonitorTaskPath')
        public_status = dictionary.get('publicStatus')
        relative_restore_paths = dictionary.get('relativeRestorePaths')
        resource_pool_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('resourcePoolEntity')) if dictionary.get('resourcePoolEntity') else None
        restored_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('restoredEntity')) if dictionary.get('restoredEntity') else None
        status = dictionary.get('status')
        warnings = None
        if dictionary.get('warnings') != None:
            warnings = list()
            for structure in dictionary.get('warnings'):
                warnings.append(cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(structure))

        # Return an object of this model
        return cls(entity,
                   error,
                   progress_monitor_task_path,
                   public_status,
                   relative_restore_paths,
                   resource_pool_entity,
                   restored_entity,
                   status,
                   warnings)


