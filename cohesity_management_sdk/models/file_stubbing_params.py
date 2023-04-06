# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.file_stubbing_params_target_view_map_entry
import cohesity_management_sdk.models.filtering_policy_proto
import cohesity_management_sdk.models.nas_analysis_job_params_access_time_bucket
import cohesity_management_sdk.models.nas_analysis_job_params_file_size_bucket
import cohesity_management_sdk.models.nas_analysis_job_params_file_type_bucket
import cohesity_management_sdk.models.nas_analysis_job_params_mod_time_bucket


class FileStubbingParams(object):

    """Implementation of the 'FileStubbingParams' model.

    File Stubbing Parameters Message to capture the additional stubbing params
    for a file-based environment.


    Attributes:

        access_time_buckets (list of NasAnalysisJobParams_AccessTimeBucket):
            File access time buckets.
        cold_file_window (long|int): Identifies the cold files in the NAS
            source. Files that haven't been accessed/modified in the last
            cold_file_window msecs or are older than cold_window_msecs are
            migrated.
        delete_orphan_data (bool): Delete migrated data if no symlink at source
            is pointing to it.
        denied_file_type_buckets (list of NasAnalysisJobParams_FileTypeBucket):
            Denied file type buckets. This is list is mutually exclusive of
            allowed buckets. This is used only when allowed buckets contain
            'Other-*' bucket in which case we will have to deny all the
            extensions which are not present allowed buckets. This field is
            only used for communication between master and slave. Iris only
            uses the 'file_type_buckets' field.
        enable_audit_logging (bool): Audit log the file tiering activity.
        enable_checksum_verification (bool): Enable checksum verification for
            downtier job.
        file_select_policy (int): File migrate policy based on file
            access/modify time and age. Depcrecated.
        file_size (long|int): Gives the size criteria to be used for selecting
            the files to be migrated. The cold files that are equal and greater
            than file_size or smaller than file_size are migrated.
        file_size_buckets (list of NasAnalysisJobParams_FileSizeBucket): File
            size buckets.
        file_size_policy (int): File size policy for selecting files to
            migrate. Depcrecated.
        file_type_buckets (list of NasAnalysisJobParams_FileTypeBucket):
            Allowed file type buckets.
        filtering_policy (FilteringPolicyProto): The filtering policy to decide
            which objects within a source should be stubbed. If this is not
            specified, then all the objects within the source will be migrated
            based on the migration policy. We use the filtering_policy in
            NasBackupParams. So this field is deprecated.
        migrate_without_stub (bool): Migrate data without stub.
        mod_time_buckets (list of NasAnalysisJobParams_ModTimeBucket): File
            modification time buckets.
        nfs_mount_path (string): Mount path where the Cohesity target view must
            be mounted on all NFS clients for accessing the migrated data.
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
        "access_time_buckets":'accessTimeBuckets',
        "cold_file_window":'coldFileWindow',
        "delete_orphan_data":'deleteOrphanData',
        "denied_file_type_buckets":'deniedFileTypeBuckets',
        "enable_audit_logging":'enableAuditLogging',
        "enable_checksum_verification":'enableChecksumVerification',
        "file_select_policy":'fileSelectPolicy',
        "file_size":'fileSize',
        "file_size_buckets":'fileSizeBuckets',
        "file_size_policy":'fileSizePolicy',
        "file_type_buckets":'fileTypeBuckets',
        "filtering_policy":'filteringPolicy',
        "migrate_without_stub":'migrateWithoutStub',
        "mod_time_buckets":'modTimeBuckets',
        "nfs_mount_path":'nfsMountPath',
        "nfs_mount_path_prefix":'nfsMountPathPrefix',
        "target_view_map":'targetViewMap',
        "target_view_name":'targetViewName',
        "target_view_prefix":'targetViewPrefix',
        "tiering_goal":'tieringGoal',
    }
    def __init__(self,
                 access_time_buckets=None,
                 cold_file_window=None,
                 delete_orphan_data=None,
                 denied_file_type_buckets=None,
                 enable_audit_logging=None,
                 enable_checksum_verification=None,
                 file_select_policy=None,
                 file_size=None,
                 file_size_buckets=None,
                 file_size_policy=None,
                 file_type_buckets=None,
                 filtering_policy=None,
                 migrate_without_stub=None,
                 mod_time_buckets=None,
                 nfs_mount_path=None,
                 nfs_mount_path_prefix=None,
                 target_view_map=None,
                 target_view_name=None,
                 target_view_prefix=None,
                 tiering_goal=None,
            ):

        """Constructor for the FileStubbingParams class"""

        # Initialize members of the class
        self.access_time_buckets = access_time_buckets
        self.cold_file_window = cold_file_window
        self.delete_orphan_data = delete_orphan_data
        self.denied_file_type_buckets = denied_file_type_buckets
        self.enable_audit_logging = enable_audit_logging
        self.enable_checksum_verification = enable_checksum_verification
        self.file_select_policy = file_select_policy
        self.file_size = file_size
        self.file_size_buckets = file_size_buckets
        self.file_size_policy = file_size_policy
        self.file_type_buckets = file_type_buckets
        self.filtering_policy = filtering_policy
        self.migrate_without_stub = migrate_without_stub
        self.mod_time_buckets = mod_time_buckets
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
        access_time_buckets = None
        if dictionary.get('accessTimeBuckets') != None:
            access_time_buckets = list()
            for structure in dictionary.get('accessTimeBuckets'):
                access_time_buckets.append(cohesity_management_sdk.models.nas_analysis_job_params_access_time_bucket.NasAnalysisJobParams_AccessTimeBucket.from_dictionary(structure))
        cold_file_window = dictionary.get('coldFileWindow')
        delete_orphan_data = dictionary.get('deleteOrphanData')
        denied_file_type_buckets = None
        if dictionary.get('deniedFileTypeBuckets') != None:
            denied_file_type_buckets = list()
            for structure in dictionary.get('deniedFileTypeBuckets'):
                denied_file_type_buckets.append(cohesity_management_sdk.models.nas_analysis_job_params_file_type_bucket.NasAnalysisJobParams_FileTypeBucket.from_dictionary(structure))
        enable_audit_logging = dictionary.get('enableAuditLogging')
        enable_checksum_verification = dictionary.get('enableChecksumVerification')
        file_select_policy = dictionary.get('fileSelectPolicy')
        file_size = dictionary.get('fileSize')
        file_size_buckets = None
        if dictionary.get('fileSizeBuckets') != None:
            file_size_buckets = list()
            for structure in dictionary.get('fileSizeBuckets'):
                file_size_buckets.append(cohesity_management_sdk.models.nas_analysis_job_params_file_size_bucket.NasAnalysisJobParams_FileSizeBucket.from_dictionary(structure))
        file_size_policy = dictionary.get('fileSizePolicy')
        file_type_buckets = None
        if dictionary.get('fileTypeBuckets') != None:
            file_type_buckets = list()
            for structure in dictionary.get('fileTypeBuckets'):
                file_type_buckets.append(cohesity_management_sdk.models.nas_analysis_job_params_file_type_bucket.NasAnalysisJobParams_FileTypeBucket.from_dictionary(structure))
        filtering_policy = cohesity_management_sdk.models.filtering_policy_proto.FilteringPolicyProto.from_dictionary(dictionary.get('filteringPolicy')) if dictionary.get('filteringPolicy') else None
        migrate_without_stub = dictionary.get('migrateWithoutStub')
        mod_time_buckets = None
        if dictionary.get('modTimeBuckets') != None:
            mod_time_buckets = list()
            for structure in dictionary.get('modTimeBuckets'):
                mod_time_buckets.append(cohesity_management_sdk.models.nas_analysis_job_params_mod_time_bucket.NasAnalysisJobParams_ModTimeBucket.from_dictionary(structure))
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
        return cls(
            access_time_buckets,
            cold_file_window,
            delete_orphan_data,
            denied_file_type_buckets,
            enable_audit_logging,
            enable_checksum_verification,
            file_select_policy,
            file_size,
            file_size_buckets,
            file_size_policy,
            file_type_buckets,
            filtering_policy,
            migrate_without_stub,
            mod_time_buckets,
            nfs_mount_path,
            nfs_mount_path_prefix,
            target_view_map,
            target_view_name,
            target_view_prefix,
            tiering_goal
)