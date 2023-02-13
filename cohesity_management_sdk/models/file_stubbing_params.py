# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.filtering_policy_proto
import cohesity_management_sdk.models.file_stubbing_params_target_view_map_entry

class FileStubbingParams(object):

    """Implementation of the 'FileStubbingParams' model.

    File Stubbing Parameters
    Message to capture the additional stubbing params for a file-based
    environment.

    Attributes:
        cold_file_window (long|int): Identifies the cold files in the NAS
            source. Files that haven't been accessed/modified in the last
            cold_file_window msecs or are older than cold_window_msecs are
            migrated.
        delete_orphan_data (bool): Delete migrated data if no symlink at
            source is pointing to it.
        enable_audit_logging (bool): Audit log the file tiering activity.
        file_select_policy (int): File migrate policy based on file
            access/modify time and age.
        file_size (long|int): Gives the size criteria to be used for selecting
            the files to be migrated. The cold files that are equal and
            greater than file_size or smaller than file_size are migrated.
        file_size_policy (int): File size policy for selecting files to
            migrate.
        filtering_policy (FilteringPolicyProto): Proto to encapsulate the
            filtering policy for backup objects like files or directories. If
            an object is not matched by any of the 'allow_filters', it will be
            excluded in the backup. If an object is matched by one of the
            'deny_filters', it will always be excluded in the backup.
            Basically 'deny_filters' overwrite 'allow_filters' if they both
            match the same object. Currently we only support two kinds of
            filter: prefix which always starts with '/', or postfix which
            always starts with '*' (cannot be "*" only). We don't support
            regular expression right now. A concrete example is: Allow
            filters: "/" Deny filters: "/tmp", "*.mp4" Using such a policy
            will include everything under the root directory except the /tmp
            directory and all the mp4 files.
        migrate_without_stub (bool): Migrate data without stub.
        nfs_mount_path (string): Mount path where the Cohesity target view
            must be mounted on all NFS clients for accessing the migrated
            data.
        nfs_mount_path_prefix (string): nfs_mount_path_prefix contains the
            parent directory path where respective view name will be suffixed
            to form a complete mount path where Cohesity target view will be
            mounted on NFS clients for accessing the migrated data.
        target_view_map (list of FileStubbingParams_TargetViewMapEntry): The
            object's entity id to TargetViewData map where the data will be
            migrated.
        target_view_name (string): The target view name to which the data will
            be migrated.
        target_view_prefix (string): target_view_prefix is used to support
            multiple objects in a single tiering job. It helps in generating
            view name which are reasonably close to the original share name.
        tiering_goal (long|int): Tiering Goal, i.e. the maximum amount of data
            that should be present on source after downtiering.



    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cold_file_window":'coldFileWindow',
        "delete_orphan_data":'deleteOrphanData',
        "enable_audit_logging":'enableAuditLogging',
        "file_select_policy":'fileSelectPolicy',
        "file_size":'fileSize',
        "file_size_policy":'fileSizePolicy',
        "filtering_policy":'filteringPolicy',
        "migrate_without_stub":'migrateWithoutStub',
        "nfs_mount_path":'nfsMountPath',
        "nfs_mount_path_prefix":'nfsMountPathPrefix',
        "target_view_map":'targetViewMap',
        "target_view_name":'targetViewName',
        "target_view_prefix":'targetViewPrefix',
        "tiering_goal":'tieringGoal'
    }

    def __init__(self,
                 cold_file_window=None,
                 delete_orphan_data=None,
                 enable_audit_logging=None,
                 file_select_policy=None,
                 file_size=None,
                 file_size_policy=None,
                 filtering_policy=None,
                 migrate_without_stub=None,
                 nfs_mount_path=None,
                 nfs_mount_path_prefix=None,
                 target_view_map=None,
                 target_view_name=None,
                 target_view_prefix=None,
                 tiering_goal=None):
        """Constructor for the FileStubbingParams class"""

        # Initialize members of the class
        self.cold_file_window = cold_file_window
        self.delete_orphan_data = delete_orphan_data
        self.enable_audit_logging = enable_audit_logging
        self.file_select_policy = file_select_policy
        self.file_size = file_size
        self.file_size_policy = file_size_policy
        self.filtering_policy = filtering_policy
        self.migrate_without_stub = migrate_without_stub
        self.nfs_mount_path = nfs_mount_path
        self.nfs_mount_path_prefix = nfs_mount_path_prefix
        self.target_view_map = target_view_map
        self.target_view_name = target_view_name
        self.target_view_prefix = target_view_prefix
        self.tiering_goal = tiering_goal


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
        cold_file_window = dictionary.get('coldFileWindow')
        delete_orphan_data = dictionary.get('deleteOrphanData')
        enable_audit_logging = dictionary.get('enableAuditLogging')
        file_select_policy = dictionary.get('fileSelectPolicy')
        file_size = dictionary.get('fileSize')
        file_size_policy = dictionary.get('fileSizePolicy')
        filtering_policy = cohesity_management_sdk.models.filtering_policy_proto.FilteringPolicyProto.from_dictionary(dictionary.get('filteringPolicy')) if dictionary.get('filteringPolicy') else None
        migrate_without_stub = dictionary.get('migrateWithoutStub', None)
        nfs_mount_path = dictionary.get('nfsMountPath')
        nfs_mount_path_prefix = dictionary.get('nfsMountPathPrefix')
        target_view_map = None
        if dictionary.get('targetViewMap') != None:
            target_view_map = list()
            for structure in dictionary.get('targetViewMap'):
                target_view_map.append(cohesity_management_sdk.models.file_stubbing_params_target_view_map_entry.FileStubbingParams_TargetViewMapEntry.from_dictionary(structure))
        target_view_name = dictionary.get('targetViewName')
        target_view_prefix = dictionary.get('targetViewPrefix')
        tiering_goal = dictionary.get('tieringGoal')

        # Return an object of this model
        return cls(cold_file_window,
                   delete_orphan_data,
                   enable_audit_logging,
                   file_select_policy,
                   file_size,
                   file_size_policy,
                   filtering_policy,
                   migrate_without_stub,
                   nfs_mount_path,
                   nfs_mount_path_prefix,
                   target_view_map,
                   target_view_name,
                   target_view_prefix,
                   tiering_goal)


