# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.error_proto

class CloudDeployInfoProtoCloudDeployEntity(object):

    """Implementation of the 'CloudDeployInfoProto_CloudDeployEntity' model.

    TODO: type model description here.

    Attributes:
        deployed_vm_name (string): Optional name that should be used for
            deployed VM.
        entity (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        error (ErrorProto): TODO: type description here.
        previous_relative_clone_dir_path (string): Directory where files of
            the entity's previous snapshot were cloned to. Path is relative to
            the destination view.
        previous_relative_clone_paths (list of string): All the paths that the
            entity's previous snapshot files were cloned to. Each path is
            relative to the destination view.
        progress_monitor_task_path (string): Progress monitor task path for
            this entity which is relative to the root path of the cloud deploy
            task progress monitor.
        public_status (int): Iris-facing task state. This field is stamped
            during the export.
        relative_clone_paths (list of string): All the paths that the entity's
            files were cloned to. Each path is relative to the destination
            view.
        status (int): The status of the entity.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "deployed_vm_name":'deployedVmName',
        "entity":'entity',
        "error":'error',
        "previous_relative_clone_dir_path":'previousRelativeCloneDirPath',
        "previous_relative_clone_paths":'previousRelativeClonePaths',
        "progress_monitor_task_path":'progressMonitorTaskPath',
        "public_status":'publicStatus',
        "relative_clone_paths":'relativeClonePaths',
        "status":'status'
    }

    def __init__(self,
                 deployed_vm_name=None,
                 entity=None,
                 error=None,
                 previous_relative_clone_dir_path=None,
                 previous_relative_clone_paths=None,
                 progress_monitor_task_path=None,
                 public_status=None,
                 relative_clone_paths=None,
                 status=None):
        """Constructor for the CloudDeployInfoProtoCloudDeployEntity class"""

        # Initialize members of the class
        self.deployed_vm_name = deployed_vm_name
        self.entity = entity
        self.error = error
        self.previous_relative_clone_dir_path = previous_relative_clone_dir_path
        self.previous_relative_clone_paths = previous_relative_clone_paths
        self.progress_monitor_task_path = progress_monitor_task_path
        self.public_status = public_status
        self.relative_clone_paths = relative_clone_paths
        self.status = status


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
        deployed_vm_name = dictionary.get('deployedVmName')
        entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('entity')) if dictionary.get('entity') else None
        error = cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(dictionary.get('error')) if dictionary.get('error') else None
        previous_relative_clone_dir_path = dictionary.get('previousRelativeCloneDirPath')
        previous_relative_clone_paths = dictionary.get('previousRelativeClonePaths')
        progress_monitor_task_path = dictionary.get('progressMonitorTaskPath')
        public_status = dictionary.get('publicStatus')
        relative_clone_paths = dictionary.get('relativeClonePaths')
        status = dictionary.get('status')

        # Return an object of this model
        return cls(deployed_vm_name,
                   entity,
                   error,
                   previous_relative_clone_dir_path,
                   previous_relative_clone_paths,
                   progress_monitor_task_path,
                   public_status,
                   relative_clone_paths,
                   status)


