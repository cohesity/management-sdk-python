# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.filtering_policy_proto
import cohesity_management_sdk.models.nas_throttling_params
import cohesity_management_sdk.models.s3_view_backup_properties
import cohesity_management_sdk.models.view_id_mapping_proto_file_level_data_lock_config


class NasBackupParams(object):

    """Implementation of the 'NasBackupParams' model.

    Message to capture any additional backup params for a NAS environment.


    Attributes:

        backup_all_existing_snapshot (bool): This bool parameter will be set
            only for DP volumes when customer doesn't select the
            full_backup_snapshot_label and incremental_backup_snapshot_label.
            When set to true, backend will be using existing oldest snapshot
            for the first backup. Each incremental will be selected in
            ascending of snapshot create time on the source.
        blacklisted_ip_addrs (list of string): Job level list of IP addresses
            that should not be used.
        continue_on_error (bool): Whether the backup job should continue on
            errors for snapshot based backups. For non-snapshot-based generic
            NAS backup jobs, Magneto always continues on errors.
        encryption_enabled (bool): Whether this backup job should use
            encryption.
        filtering_policy (FilteringPolicyProto): The filtering policy to decide
            which objects within a source should be backed up. If this is not
            specified, then all of the objects within the source will be backed
            up.
        fld_config (ViewIdMappingProto_FileLevelDataLockConfig): File level
            data lock configuration. To support File DataLock functionality
            similar to Netapp SnapLock, the following fields will be required
            from the user. This is same as what Cohesity as a filer offers for
            File DataLock.
        full_backup_snapshot_label (string): Only used when we backup using
            discovered snapshots. This prefix is to figure out which discovered
            snapshot we need to use for full backup.
        incremental_backup_snapshot_label (string): Only used when we backup
            using discovered snapshots. This prefix is to figure out which
            discovered snapshot we need to use for incremental backup.
        is_source_initiated_backup (bool): Source initiated backup when the
            source sends pushes the data like for example snapmirror based
            backup for netapp.
        mixed_mode_preference (int): If the target entity is a mixed mode
            volume, which NAS protocol type the user prefer to backup. This
            does not apply to generic NAS and will be ignored.
        modify_source_permissions (bool): Specifies if the source permissions
            can be modified to allow the backup.
        nfs_version_preference (int): If the target entity supports both NFSv3
            and NFSv4.1, which NAS protocol type the user prefers to backup.
            This does not apply to generic NAS and will be ignored.
        s3_viewbackupproperties (S3ViewBackupProperties): This message captures
            all the details of S3 view.
        shared_view_name (string): Specifies the view name if the view is to be
            shared across multiple backup jobs. Required for backing up
            multiple directories of the same share through different protection
            jobs(for faster backup).
        snapshot_change_enabled (bool): Whether this backup job should utilize
            changelist like API when available for faster incremental backups.
        throttling_params (NasThrottlingParams): NAS throttling params for full
            and incremental backups. This overrides corresponding source level
            parameters.
        whitelisted_ip_addrs (list of string): Job level list of IP addresses
            that should be used exclusively.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "backup_all_existing_snapshot":'backupAllExistingSnapshot',
        "blacklisted_ip_addrs":'blacklistedIpAddrs',
        "continue_on_error":'continueOnError',
        "encryption_enabled":'encryptionEnabled',
        "filtering_policy":'filteringPolicy',
        "fld_config":'fldConfig',
        "full_backup_snapshot_label":'fullBackupSnapshotLabel',
        "incremental_backup_snapshot_label":'incrementalBackupSnapshotLabel',
        "is_source_initiated_backup":'isSourceInitiatedBackup',
        "mixed_mode_preference":'mixedModePreference',
        "modify_source_permissions":'modifySourcePermissions',
        "nfs_version_preference":'nfsVersionPreference',
        "s3_viewbackupproperties":'s3Viewbackupproperties',
        "shared_view_name":'sharedViewName',
        "snapshot_change_enabled":'snapshotChangeEnabled',
        "throttling_params":'throttlingParams',
        "whitelisted_ip_addrs":'whitelistedIpAddrs',
    }
    def __init__(self,
                 backup_all_existing_snapshot=None,
                 blacklisted_ip_addrs=None,
                 continue_on_error=None,
                 encryption_enabled=None,
                 filtering_policy=None,
                 fld_config=None,
                 full_backup_snapshot_label=None,
                 incremental_backup_snapshot_label=None,
                 is_source_initiated_backup=None,
                 mixed_mode_preference=None,
                 modify_source_permissions=None,
                 nfs_version_preference=None,
                 s3_viewbackupproperties=None,
                 shared_view_name=None,
                 snapshot_change_enabled=None,
                 throttling_params=None,
                 whitelisted_ip_addrs=None,
            ):

        """Constructor for the NasBackupParams class"""

        # Initialize members of the class
        self.backup_all_existing_snapshot = backup_all_existing_snapshot
        self.blacklisted_ip_addrs = blacklisted_ip_addrs
        self.continue_on_error = continue_on_error
        self.encryption_enabled = encryption_enabled
        self.filtering_policy = filtering_policy
        self.fld_config = fld_config
        self.full_backup_snapshot_label = full_backup_snapshot_label
        self.incremental_backup_snapshot_label = incremental_backup_snapshot_label
        self.is_source_initiated_backup = is_source_initiated_backup
        self.mixed_mode_preference = mixed_mode_preference
        self.modify_source_permissions = modify_source_permissions
        self.nfs_version_preference = nfs_version_preference
        self.s3_viewbackupproperties = s3_viewbackupproperties
        self.shared_view_name = shared_view_name
        self.snapshot_change_enabled = snapshot_change_enabled
        self.throttling_params = throttling_params
        self.whitelisted_ip_addrs = whitelisted_ip_addrs

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
        backup_all_existing_snapshot = dictionary.get('backupAllExistingSnapshot')
        blacklisted_ip_addrs = dictionary.get("blacklistedIpAddrs")
        continue_on_error = dictionary.get('continueOnError')
        encryption_enabled = dictionary.get('encryptionEnabled')
        filtering_policy = cohesity_management_sdk.models.filtering_policy_proto.FilteringPolicyProto.from_dictionary(dictionary.get('filteringPolicy')) if dictionary.get('filteringPolicy') else None
        fld_config = cohesity_management_sdk.models.view_id_mapping_proto_file_level_data_lock_config.ViewIdMappingProto_FileLevelDataLockConfig.from_dictionary(dictionary.get('fldConfig')) if dictionary.get('fldConfig') else None
        full_backup_snapshot_label = dictionary.get('fullBackupSnapshotLabel')
        incremental_backup_snapshot_label = dictionary.get('incrementalBackupSnapshotLabel')
        is_source_initiated_backup = dictionary.get('isSourceInitiatedBackup')
        mixed_mode_preference = dictionary.get('mixedModePreference')
        modify_source_permissions = dictionary.get('modifySourcePermissions')
        nfs_version_preference = dictionary.get('nfsVersionPreference')
        s3_viewbackupproperties = cohesity_management_sdk.models.s3_view_backup_properties.S3ViewBackupProperties.from_dictionary(dictionary.get('s3Viewbackupproperties')) if dictionary.get('s3Viewbackupproperties') else None
        shared_view_name = dictionary.get('sharedViewName')
        snapshot_change_enabled = dictionary.get('snapshotChangeEnabled')
        throttling_params = cohesity_management_sdk.models.nas_throttling_params.NasThrottlingParams.from_dictionary(dictionary.get('throttlingParams')) if dictionary.get('throttlingParams') else None
        whitelisted_ip_addrs = dictionary.get("whitelistedIpAddrs")

        # Return an object of this model
        return cls(
            backup_all_existing_snapshot,
            blacklisted_ip_addrs,
            continue_on_error,
            encryption_enabled,
            filtering_policy,
            fld_config,
            full_backup_snapshot_label,
            incremental_backup_snapshot_label,
            is_source_initiated_backup,
            mixed_mode_preference,
            modify_source_permissions,
            nfs_version_preference,
            s3_viewbackupproperties,
            shared_view_name,
            snapshot_change_enabled,
            throttling_params,
            whitelisted_ip_addrs
)