# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.error_proto


class RestoreInfoProto_RestoreEntity(object):

    """Implementation of the 'RestoreInfoProto_RestoreEntity' model.

    TODO: type description here.


    Attributes:

        entity (EntityProto): The entity that was restored.
        error (ErrorProto): If the restore of the 'entity' failed, this field
            may contain the cause of the failure.
        progress_monitor_task_path (string): The path relative to the root path
            of the restore task progress monitor of the progress monitor for
            this entity.
        public_status (int): Iris-facing task state. This field is stamped
            during the export.
        relative_restore_paths (list of string): All the paths that the
            entity's files were restored to. Each path is relative to the
            destination view.
        resource_pool_entity (EntityProto): Even though, this field is
            redundant for kCloneVMs task, we will set this field for sake of
            consistency.  Please note that this field may not be set if the
            restore of this entity fails.
        restored_entity (EntityProto): Note: For a recovery task in the VMware
            environment, once the VM is created, it is storage vMotioned to its
            primary datastore. If storage vMotion fails, Magneto marks the
            recovery task as failed. However, this field will still be set for
            the recovered VM. It can be used later to clean up the VM from
            primary environment (i.e, vCenter)
        restored_view_name (string): Cloned or converted view name which is
            used to restore the entity. In case of on-prem deploy task this
            view name will be used in next run.
        status (int): The restore status of the entity.
        total_bytes_restored (long|int): Contains the information regarding
            total bytes restored for this entity. Currently updated only in
            case of outlook restore.
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
        "restored_view_name":'restoredViewName',
        "status":'status',
        "total_bytes_restored":'totalBytesRestored',
        "warnings":'warnings',
    }
    def __init__(self,
                 entity=None,
                 error=None,
                 progress_monitor_task_path=None,
                 public_status=None,
                 relative_restore_paths=None,
                 resource_pool_entity=None,
                 restored_entity=None,
                 restored_view_name=None,
                 status=None,
                 total_bytes_restored=None,
                 warnings=None,
            ):

        """Constructor for the RestoreInfoProto_RestoreEntity class"""

        # Initialize members of the class
        self.entity = entity
        self.error = error
        self.progress_monitor_task_path = progress_monitor_task_path
        self.public_status = public_status
        self.relative_restore_paths = relative_restore_paths
        self.resource_pool_entity = resource_pool_entity
        self.restored_entity = restored_entity
        self.restored_view_name = restored_view_name
        self.status = status
        self.total_bytes_restored = total_bytes_restored
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
        relative_restore_paths = dictionary.get("relativeRestorePaths")
        resource_pool_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('resourcePoolEntity')) if dictionary.get('resourcePoolEntity') else None
        restored_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('restoredEntity')) if dictionary.get('restoredEntity') else None
        restored_view_name = dictionary.get('restoredViewName')
        status = dictionary.get('status')
        total_bytes_restored = dictionary.get('totalBytesRestored')
        warnings = None
        if dictionary.get('warnings') != None:
            warnings = list()
            for structure in dictionary.get('warnings'):
                warnings.append(cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(structure))

        # Return an object of this model
        return cls(
            entity,
            error,
            progress_monitor_task_path,
            public_status,
            relative_restore_paths,
            resource_pool_entity,
            restored_entity,
            restored_view_name,
            status,
            total_bytes_restored,
            warnings
)