# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.protection_job_run_stats
import cohesity_management_sdk.models.source_backup_status


class BackupRun(object):

    """Implementation of the 'BackupRun' model.

    Specifies details about the Backup task for a Job Run. A Backup task
    captures the original backup snapshots for each Protection Source in the
    Job.


    Attributes:

        environment (EnvironmentBackupRunEnum): Specifies the environment type
            that the task is protecting. Supported environment types such as
            'kView', 'kSQL', 'kVMware', etc. NOTE: 'kPuppeteer' refers to
            Cohesity's Remote Adapter. 'kVMware' indicates the VMware
            Protection Source environment. 'kHyperV' indicates the HyperV
            Protection Source environment. 'kSQL' indicates the SQL Protection
            Source environment. 'kView' indicates the View Protection Source
            environment. 'kPuppeteer' indicates the Cohesity's Remote Adapter.
            'kPhysical' indicates the physical Protection Source environment.
            'kPure' indicates the Pure Storage Protection Source environment.
            'kNimble' indicates the Nimble Storage Protection Source
            environment. 'kAzure' indicates the Microsoft's Azure Protection
            Source environment. 'kNetapp' indicates the Netapp Protection
            Source environment. 'kAgent' indicates the Agent Protection Source
            environment. 'kGenericNas' indicates the Generic Network Attached
            Storage Protection Source environment. 'kAcropolis' indicates the
            Acropolis Protection Source environment. 'kPhysicalFiles' indicates
            the Physical Files Protection Source environment. 'kIsilon'
            indicates the Dell EMC's Isilon Protection Source environment.
            'kGPFS' indicates IBM's GPFS Protection Source environment. 'kKVM'
            indicates the KVM Protection Source environment. 'kAWS' indicates
            the AWS Protection Source environment. 'kExchange' indicates the
            Exchange Protection Source environment. 'kHyperVVSS' indicates the
            HyperV VSS Protection Source environment. 'kOracle' indicates the
            Oracle Protection Source environment. 'kGCP' indicates the Google
            Cloud Platform Protection Source environment. 'kFlashBlade'
            indicates the Flash Blade Protection Source environment.
            'kAWSNative' indicates the AWS Native Protection Source
            environment. 'kO365' indicates the Office 365 Protection Source
            environment. 'kO365Outlook' indicates Office 365 outlook Protection
            Source environment. 'kHyperFlex' indicates the Hyper Flex
            Protection Source environment. 'kGCPNative' indicates the GCP
            Native Protection Source environment. 'kAzureNative' indicates the
            Azure Native Protection Source environment. 'kKubernetes' indicates
            a Kubernetes Protection Source environment. 'kElastifile' indicates
            Elastifile Protection Source environment. 'kAD' indicates Active
            Directory Protection Source environment. 'kRDSSnapshotManager'
            indicates AWS RDS Protection Source environment. 'kCassandra'
            indicates Cassandra Protection Source environment. 'kMongoDB'
            indicates MongoDB Protection Source environment. 'kCouchbase'
            indicates Couchbase Protection Source environment. 'kHdfs'
            indicates Hdfs Protection Source environment. 'kHive' indicates
            Hive Protection Source environment. 'kHBase' indicates HBase
            Protection Source environment. 'kUDA' indicates Universal Data
            Adapter Protection Source environment. 'kO365Teams' indicates the
            Office365 Teams Protection Source environment. 'kO365Group'
            indicates the Office365 Groups Protection Source environment.
            'kO365Exchange' indicates the Office365 Mailbox Protection Source
            environment. 'kO365OneDrive' indicates the Office365 OneDrive
            Protection Source environment. 'kO365Sharepoint' indicates the
            Office365 SharePoint Protection Source environment.
            'kO365PublicFolders' indicates the Office365 PublicFolders
            Protection Source environment.
        error (string): Specifies if an error occurred (if any) while running
            this task. This field is populated when the status is equal to
            'kFailure'.
        job_run_id (long|int): Specifies the id of the Job Run that ran the
            backup task and the copy tasks.
        message (string): Specifies a message after finishing the task
            successfully. This field is optionally populated when the status is
            equal to 'kSuccess'.
        metadata_deleted (bool): Specifies if the metadata and snapshots
            associated with this Job Run have been deleted. This field is set
            to true when the snapshots, which are marked for deletion, are
            removed by garbage collection. The associated metadata is also
            deleted.
        quiesced (bool): Specifies if app-consistent snapshot was captured.
            This field is set to true, if an app-consistent snapshot was taken
            by quiescing applications and the file system before taking a
            backup.
        run_type (RunTypeEnum): Specifies the type of backup such as
            'kRegular', 'kFull', 'kLog' or 'kSystem'. 'kRegular' indicates a
            incremental (CBT) backup. Incremental backups utilizing CBT (if
            supported) are captured of the target protection objects. The first
            run of a kRegular schedule captures all the blocks. 'kFull'
            indicates a full (no CBT) backup. A complete backup (all blocks) of
            the target protection objects are always captured and Change Block
            Tracking (CBT) is not utilized. 'kLog' indicates a Database Log
            backup. Capture the database transaction logs to allow rolling back
            to a specific point in time. 'kSystem' indicates a system backup.
            System backups are used to do bare metal recovery of the system to
            a specific point in time.
        sla_violated (bool): Specifies if the SLA was violated for the Job Run.
            This field is set to true, if time to complete the Job Run is
            longer than the SLA specified. This field is populated when the
            status is set to 'kSuccess' or 'kFailure'.
        snapshots_deleted (bool): Specifies if backup snapshots associated with
            this Job Run have been marked for deletion because of the retention
            settings in the Policy or if they were manually deleted from the
            Cohesity Dashboard.
        snapshots_deleted_time_usecs (long|int): Specifies if backup snapshots
            associated with this Job Run have been marked for deletion because
            of the retention settings in the Policy or if they were manually
            deleted from the Cohesity Dashboard.
        source_backup_status (list of SourceBackupStatus): Array of Source
            Object Backup Status.  Specifies the status of backing up each
            source objects (such as VMs) associated with the job.
        stats (ProtectionJobRunStats): Specifies the aggregated stats of all
            Backup Run tasks in a Protection Run.
        status (StatusBackupRunEnum): Specifies the status of Backup task such
            as 'kRunning', 'kSuccess', 'kFailure' etc. kWarning, kOnHold,
            kMissed, kFinalizing, kWaitingToRetry.
        warnings (list of string): Array of Warnings.  Specifies the warnings
            that occurred (if any) while running this task.
        worm_retention_type (WormRetentionTypeEnum): Specifies WORM retention
            type for the snapshot as given by the policy. When a WORM retention
            type is specified, the snapshot will be kept until the maximum of
            the snapshot retention time. During that time, the snapshot cannot
            be deleted. 'kNone' implies there is no WORM retention set.
            'kCompliance' implies WORM retention is set for compliance reason.
            'kAdministrative' implies WORM retention is set for administrative
            purposes.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "environment":'environment',
        "error":'error',
        "job_run_id":'jobRunId',
        "message":'message',
        "metadata_deleted":'metadataDeleted',
        "quiesced":'quiesced',
        "run_type":'runType',
        "sla_violated":'slaViolated',
        "snapshots_deleted":'snapshotsDeleted',
        "snapshots_deleted_time_usecs":'snapshotsDeletedTimeUsecs',
        "source_backup_status":'sourceBackupStatus',
        "stats":'stats',
        "status":'status',
        "warnings":'warnings',
        "worm_retention_type":'wormRetentionType',
    }
    def __init__(self,
                 environment=None,
                 error=None,
                 job_run_id=None,
                 message=None,
                 metadata_deleted=None,
                 quiesced=None,
                 run_type=None,
                 sla_violated=None,
                 snapshots_deleted=None,
                 snapshots_deleted_time_usecs=None,
                 source_backup_status=None,
                 stats=None,
                 status=None,
                 warnings=None,
                 worm_retention_type=None,
            ):

        """Constructor for the BackupRun class"""

        # Initialize members of the class
        self.environment = environment
        self.error = error
        self.job_run_id = job_run_id
        self.message = message
        self.metadata_deleted = metadata_deleted
        self.quiesced = quiesced
        self.run_type = run_type
        self.sla_violated = sla_violated
        self.snapshots_deleted = snapshots_deleted
        self.snapshots_deleted_time_usecs = snapshots_deleted_time_usecs
        self.source_backup_status = source_backup_status
        self.stats = stats
        self.status = status
        self.warnings = warnings
        self.worm_retention_type = worm_retention_type

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
        environment = dictionary.get('environment')
        error = dictionary.get('error')
        job_run_id = dictionary.get('jobRunId')
        message = dictionary.get('message')
        metadata_deleted = dictionary.get('metadataDeleted')
        quiesced = dictionary.get('quiesced')
        run_type = dictionary.get('runType')
        sla_violated = dictionary.get('slaViolated')
        snapshots_deleted = dictionary.get('snapshotsDeleted')
        snapshots_deleted_time_usecs = dictionary.get('snapshotsDeletedTimeUsecs')
        source_backup_status = None
        if dictionary.get('sourceBackupStatus') != None:
            source_backup_status = list()
            for structure in dictionary.get('sourceBackupStatus'):
                source_backup_status.append(cohesity_management_sdk.models.source_backup_status.SourceBackupStatus.from_dictionary(structure))
        stats = cohesity_management_sdk.models.protection_job_run_stats.ProtectionJobRunStats.from_dictionary(dictionary.get('stats')) if dictionary.get('stats') else None
        status = dictionary.get('status')
        warnings = dictionary.get("warnings")
        worm_retention_type = dictionary.get('wormRetentionType')

        # Return an object of this model
        return cls(
            environment,
            error,
            job_run_id,
            message,
            metadata_deleted,
            quiesced,
            run_type,
            sla_violated,
            snapshots_deleted,
            snapshots_deleted_time_usecs,
            source_backup_status,
            stats,
            status,
            warnings,
            worm_retention_type
)