# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto

class SetupRestoreDiskTaskInfoProto(object):

    """Implementation of the 'SetupRestoreDiskTaskInfoProto' model.

    Each available extension is listed below along with the location of the
    proto file (relative to magneto/connectors) where it is defined.
    SetupRestoreDiskTaskInfoProto
    extension, extension_number
    Location
    ===========================================================================
    ==
    vmware::SetupRestoreDiskTaskInfo
    vmware_setup_restore_disk_task_info, 100
    connectors/vmware/vmware_setup_restore_disks.proto.proto
    AgentSetupRestoreDiskTaskInfo
    agent_setup_restore_disk_task_info, 101
    base/agent.proto
    app_file::SetupRestoreTaskInfo
    app_file_setup_restore_task_info, 102
    connectors/app_file/app_file_setup_restore.proto
    hyperv::SetupRestoreDiskTaskInfo
    hyperv_setup_restore_disk_task_info, 103
    connectors/hyperv/hyperv_setup_restore_disks.proto
    ===========================================================================
    ==

    Attributes:
        entity (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        progress_monitor_root_task_path (string): The path to the progress
            monitor root task if any.
        root_entity (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        source_view_name (string): The source view which contains the backups
            for the 'entity'.
        task_id (long|int): The id of the associated task.
        view_box_id (long|int): The view box id containing the backups for the
            'entity'.
        view_name (string): Destination view into which the files will be
            cloned.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "entity":'entity',
        "progress_monitor_root_task_path":'progressMonitorRootTaskPath',
        "root_entity":'rootEntity',
        "source_view_name":'sourceViewName',
        "task_id":'taskId',
        "view_box_id":'viewBoxId',
        "view_name":'viewName'
    }

    def __init__(self,
                 entity=None,
                 progress_monitor_root_task_path=None,
                 root_entity=None,
                 source_view_name=None,
                 task_id=None,
                 view_box_id=None,
                 view_name=None):
        """Constructor for the SetupRestoreDiskTaskInfoProto class"""

        # Initialize members of the class
        self.entity = entity
        self.progress_monitor_root_task_path = progress_monitor_root_task_path
        self.root_entity = root_entity
        self.source_view_name = source_view_name
        self.task_id = task_id
        self.view_box_id = view_box_id
        self.view_name = view_name


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
        progress_monitor_root_task_path = dictionary.get('progressMonitorRootTaskPath')
        root_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('rootEntity')) if dictionary.get('rootEntity') else None
        source_view_name = dictionary.get('sourceViewName')
        task_id = dictionary.get('taskId')
        view_box_id = dictionary.get('viewBoxId')
        view_name = dictionary.get('viewName')

        # Return an object of this model
        return cls(entity,
                   progress_monitor_root_task_path,
                   root_entity,
                   source_view_name,
                   task_id,
                   view_box_id,
                   view_name)


