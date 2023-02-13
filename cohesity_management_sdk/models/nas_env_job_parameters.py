# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.data_migration_job_parameters
import cohesity_management_sdk.models.data_uptier_job_parameters
import cohesity_management_sdk.models.file_path_filter
import cohesity_management_sdk.models.file_level_data_lock_config
import cohesity_management_sdk.models.filter_ip_config
import cohesity_management_sdk.models.snapshot_label
import cohesity_management_sdk.models.nas_source_throttling_params

class NasEnvJobParameters(object):

    """Implementation of the 'NasEnvJobParameters' model.

    Specifies job parameters applicable for all 'kGenericNas' Environment
    type
    Protection Sources in a Protection Job.

    Attributes:
        continue_on_error (bool): Specifies if the backup should continue on
            with other Protection Sources even if the backup operation of some
            Protection Source fails. If true, the Cohesity Cluster ignores the
            errors and continues with remaining Protection Sources in the job.
            If false, the backup operation stops when an error occurs. This
            does not apply to non-snapshot based generic NAS backup jobs. If
            not set, default value is true.
        data_migration_job_parameters (DataMigrationJobParameters): Specifies
            parameters applicable for data migration jobs in NAS environment.
        data_uptier_job_parameters (DataUptierJobParameters): Specifies
            additional parameters that are applicable only to the data uptier
            jobs in NAS environment.
        enable_faster_incremental_backups (bool): Specifies whether this job
            will enable faster incremental backups using change list or
            similar APIs
        encryption_enabled (bool): Specifies if the protection job should use
            encryption while backing up
        file_lock_config (FileLevelDataLockConfig): Optional config that
            enables file locking for this job. It cannot be disabled during
            the edit of a job, if it has been enabled during the creation of
            the job. Also, it cannot be enabled if it was disabled during the
            creation of the job.
        file_path_filters (FilePathFilter): Specifies filters to match files
            and directories on a Server. Two kinds of filters are supported.
            a) prefix which always starts with '/'. b) posix which always
            starts with '*' (cannot be "*" only). Regular expressions are not
            supported. If a directory is matched, the action is applicable to
            all of its descendants. File paths not matching any protectFilters
            are not backed up.  An example is: Protect Filters: "/" Exclude
            Filters: "/tmp", "*.mp4" Using such a policy will include
            everything under the root directory except the /tmp directory and
            all the mp4 files.
        filter_ip_config (FilterIpConfig): Specifies the list of IP addresses
            that are allowed or denied at the job level. Allowed IPs and
            Denied IPs cannot be used together.
        nas_protocol (NasProtocolNasEnvJobParametersEnum): Specifies the
            preferred protocol to use for backup. This does not apply to
            generic NAS and will be ignored. Specifies the protocol used by a
            NAS server. 'kNfs3' indicates NFS v3 protocol. 'kCifs1' indicates
            CIFS v1.0 protocol.
        nfs_version_preference (NfsVersionPreferenceEnum): Specifies the
            preferred NFS protocol to use for the backup when multiple NFS
            protocols are present on a single volume.
            Specifies the protocol used by a NAS server.
            'kNfs3' indicates NFS v3 protocol.
            'kCifs1' indicates CIFS v1.0 protocol.
        snapshot_label (SnapshotLabel): Specifies the incremental and full
            snapshot label for Data-Protect Netapp Volumes backup. If field is
            set , incremental and full snapshot label has to be provided. If
            field is not set, the snapshot label will be automatically set
            using timestamp.
        throttling_config (NasSourceThrottlingParams): Specifies the NAS
            specific source throttling parameters during full or incremental
            backup of the source.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "continue_on_error":'continueOnError',
        "data_migration_job_parameters":'dataMigrationJobParameters',
        "data_uptier_job_parameters":'dataUptierJobParameters',
        "enable_faster_incremental_backups":'enableFasterIncrementalBackups',
        "encryption_enabled":'encryptionEnabled',
        "file_lock_config":'fileLockConfig',
        "file_path_filters":'filePathFilters',
        "filter_ip_config":'filterIpConfig',
        "nas_protocol":'nasProtocol',
        "nfs_version_preference":'nfsVersionPreference',
        "snapshot_label":'snapshotLabel',
        "throttling_config":'throttlingConfig'
    }

    def __init__(self,
                 continue_on_error=None,
                 data_migration_job_parameters=None,
                 data_uptier_job_parameters=None,
                 enable_faster_incremental_backups=None,
                 encryption_enabled=None,
                 file_lock_config=None,
                 file_path_filters=None,
                 filter_ip_config=None,
                 nas_protocol=None,
                 nfs_version_preference=None,
                 snapshot_label=None,
                 throttling_config=None):
        """Constructor for the NasEnvJobParameters class"""

        # Initialize members of the class
        self.continue_on_error = continue_on_error
        self.data_migration_job_parameters = data_migration_job_parameters
        self.data_uptier_job_parameters = data_uptier_job_parameters
        self.enable_faster_incremental_backups = enable_faster_incremental_backups
        self.encryption_enabled = encryption_enabled
        self.file_lock_config = file_lock_config
        self.file_path_filters = file_path_filters
        self.filter_ip_config = filter_ip_config
        self.nas_protocol = nas_protocol
        self.nfs_version_preference = nfs_version_preference
        self.snapshot_label = snapshot_label
        self.throttling_config = throttling_config


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
        continue_on_error = dictionary.get('continueOnError')
        data_migration_job_parameters = cohesity_management_sdk.models.data_migration_job_parameters.DataMigrationJobParameters.from_dictionary(dictionary.get('dataMigrationJobParameters')) if dictionary.get('dataMigrationJobParameters') else None
        data_uptier_job_parameters = cohesity_management_sdk.models.data_uptier_job_parameters.DataUptierJobParameters.from_dictionary(dictionary.get('dataUptierJobParameters')) if dictionary.get('dataUptierJobParameters') else None
        enable_faster_incremental_backups = dictionary.get('enableFasterIncrementalBackups')
        encryption_enabled = dictionary.get('encryptionEnabled')
        file_lock_config = cohesity_management_sdk.models.file_level_data_lock_config.FileLevelDataLockConfig.from_dictionary(dictionary.get('fileLockConfig')) if dictionary.get('fileLockConfig') else None
        file_path_filters = cohesity_management_sdk.models.file_path_filter.FilePathFilter.from_dictionary(dictionary.get('filePathFilters')) if dictionary.get('filePathFilters') else None
        filter_ip_config = cohesity_management_sdk.models.filter_ip_config.FilterIpConfig.from_dictionary(dictionary.get('filterIpConfig')) if dictionary.get('filterIpConfig') else None
        nas_protocol = dictionary.get('nasProtocol')
        nfs_version_preference = dictionary.get('nfsVersionPreference')
        snapshot_label = cohesity_management_sdk.models.snapshot_label.SnapshotLabel.from_dictionary(dictionary.get('snapshotLabel')) if dictionary.get('snapshotLabel') else None
        throttling_config = cohesity_management_sdk.models.nas_source_throttling_params.NasSourceThrottlingParams.from_dictionary(dictionary.get('throttlingConfig')) if dictionary.get('throttlingConfig') else None

        # Return an object of this model
        return cls(continue_on_error,
                   data_migration_job_parameters,
                   data_uptier_job_parameters,
                   enable_faster_incremental_backups,
                   encryption_enabled,
                   file_lock_config,
                   file_path_filters,
                   filter_ip_config,
                   nas_protocol,
                   nfs_version_preference,
                   snapshot_label,
                   throttling_config)


