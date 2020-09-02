# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.alerting_config
import cohesity_management_sdk.models.cloud_parameters
import cohesity_management_sdk.models.data_migration_policy
import cohesity_management_sdk.models.environment_type_job_parameters
import cohesity_management_sdk.models.time_of_day
import cohesity_management_sdk.models.indexing_policy
import cohesity_management_sdk.models.backup_script
import cohesity_management_sdk.models.remote_job_script
import cohesity_management_sdk.models.source_special_parameter

class ProtectionJobRequestBody(object):

    """Implementation of the 'ProtectionJobRequestBody' model.

    Specifies information about a Protection Job.

    Attributes:
        leverage_san_transport (bool): If this field is set to true, then the
            backup for the objects will be performed using dedicated storage
            area network (SAN) instead of LAN or managment network.
        abort_in_blackout_period (bool): If true, the Cohesity Cluster aborts
            any currently executing Job Runs of this Protection Job when a
            blackout period specified for this Job starts, even if the Job Run
            started before the blackout period began. If false, a Job Run
            continues to execute, if the Job Run started before the blackout
            period starts.
        alerting_config (AlertingConfig): Specifies optional settings for
            alerting.
        alerting_policy (list of AlertingPolicyEnum): Array of Job Events.
            During Job Runs, the following Job Events are generated: 1) Job
            succeeds 2) Job fails 3) Job violates the SLA These Job Events can
            cause Alerts to be generated. 'kSuccess' means the Protection Job
            succeeded. 'kFailure' means the Protection Job failed.
            'kSlaViolation' means the Protection Job took longer than the time
            period specified in the SLA.
        cloud_parameters (CloudParameters): Specifies Cloud parameters that
            are applicable to all Protection Sources in a Protection Job in
            certain scenarios.
        continue_on_quiesce_failure (bool): Whether to continue backing up on
            quiesce failure.
        create_remote_view (bool): Specifies whether to create a remote view
            name to use for view overwrite.
        data_migration_policy (DataMigrationPolicy): Specifies settings for
            data migration in NAS environment. This also specifies the
            retention policy that should be applied to files after they have
            been moved to cohesity cluster.
        dedup_disabled_source_ids (list of long|int): List of source ids for
            which source side dedup is disabled from the backup job.
        description (string): Specifies a text description about the
            Protection Job.
        end_time_usecs (long|int): Specifies the epoch time (in microseconds)
            after which the Protection Job becomes dormant.
        environment (EnvironmentProtectionJobRequestBodyEnum): Specifies the
            environment type (such as kVMware or kSQL) of the Protection
            Source this Job is protecting. Supported environment types such as
            'kView', 'kSQL', 'kVMware', etc. NOTE: 'kPuppeteer' refers to
            Cohesity's Remote Adapter. 'kVMware' indicates the VMware
            Protection Source environment. 'kHyperV' indicates the HyperV
            Protection Source environment. 'kSQL' indicates the SQL Protection
            Source environment. 'kView' indicates the View Protection Source
            environment. 'kPuppeteer' indicates the Cohesity's Remote Adapter.
            'kPhysical' indicates the physical Protection Source environment.
            'kPure' indicates the Pure Storage Protection Source environment.
            'Nimble' indicates the Nimble Storage Protection Source
            environment. 'kAzure' indicates the Microsoft's Azure Protection
            Source environment. 'kNetapp' indicates the Netapp Protection
            Source environment. 'kAgent' indicates the Agent Protection Source
            environment. 'kGenericNas' indicates the Generic Network Attached
            Storage Protection Source environment. 'kAcropolis' indicates the
            Acropolis Protection Source environment. 'kPhsicalFiles' indicates
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
            environment. 'kO365Outlook' indicates Office 365 outlook
            Source environment. 'kHyperFlex' indicates the Hyper Flex
            Protection Source environment. 'kGCPNative' indicates the GCP
            Native Protection Source environment. 'kAzureNative' indicates the
            Azure Native Protection Source environment. 'kKubernetes'
            indicates a Kubernetes Protection Source environment.
            'kElastifile' indicates Elastifile Protection Source environment.
            'kAD' indicates Active Directory Protection Source environment.
            'kRDSSnapshotManager' indicates AWS RDS Protection Source
            environment. 'kCassandra' indicates Cassandra Protection Source
            environment. 'kMongoDB' indicates MongoDB Protection Source
            environment. 'kCouchbase' indicates Couchbase Protection Source
            environment. 'kHdfs' indicates Hdfs Protection Source environment.
            'kHive' indicates Hive Protection Source environment. 'kHBase'
            indicates HBase Protection Source environment.
        environment_parameters (EnvironmentTypeJobParameters): Specifies
            additional parameters that are common to all Protection Sources in
            a Protection Job created for a particular environment type.
        exclude_source_ids (list of long|int): Array of Excluded Source
            Objects.  List of Object ids from a Protection Source that should
            not be protected and are excluded from being backed up by the
            Protection Job. Leaf and non-leaf Objects may be in this list and
            an Object in this list must have an ancestor in the sourceId
            list.
        exclude_vm_tag_ids (list of long|int): Array of Arrays of VM Tag Ids
            that Specify VMs to Exclude.  Optionally specify a list of VMs to
            exclude from protecting by listing Protection Source ids of VM
            Tags in this two dimensional array. Using this two dimensional
            array of Tag ids, the Cluster generates a list of VMs to exclude
            from protecting, which are derived from intersections of the inner
            arrays and union of the outer array, as shown by the following
            example. For example a Datacenter is selected to be protected but
            you want to exclude all the 'Former Employees' VMs in the East and
            West but keep all the VMs for 'Former Employees' in the South
            which are also stored in this Datacenter, by specifying the
            following tag id array: [ [1000, 2221], [1000, 3031] ], where 1000
            is the 'Former Employee' VM Tag id, 2221 is the 'East' VM Tag id
            and 3031 is the 'West' VM Tag id. The first inner array [1000,
            2221] produces a list of VMs that are both tagged with 'Former
            Employees' and 'East' (an intersection). The second inner array
            [1000, 3031] produces a list of VMs that are both tagged with
            'Former Employees' and 'West' (an intersection). The outer array
            combines the list of VMs from the two inner arrays. The list of
            resulting VMs are excluded from being protected this Job.
        full_protection_sla_time_mins (long|int): If specified, this setting
            is number of minutes that a Job Run of a Full (no CBT) backup
            schedule is expected to complete, which is known as a
            Service-Level Agreement (SLA). A SLA violation is reported when
            the run time of a Job Run exceeds the SLA time period specified
            for this backup schedule.
        full_protection_start_time (TimeOfDay): Specifies the time of day to
            start the Full Protection Schedule. This is optional and only
            applicable if the Protection Policy defines a monthly or a daily
            Full (no CBT) Protection Schedule. Default value is 02:00 AM.
            deprecated: true
        incremental_protection_sla_time_mins (long|int): If specified, this
            setting is number of minutes that a Job Run of a CBT-based backup
            schedule is expected to complete, which is known as a
            Service-Level Agreement (SLA). A SLA violation is reported when
            the run time of a Job Run exceeds the SLA time period specified
            for this backup schedule.
        incremental_protection_start_time (TimeOfDay): Specifies the time of
            day to start the CBT-based Protection Schedule. This is optional
            and only applicable if the Protection Policy defines a monthly or
            a daily CBT-based Protection Schedule. Default value is 02:00 AM.
            deprecated: true
        indexing_policy (IndexingPolicy): Specifies settings for indexing
            files found in an Object (such as a VM) so these files can be
            searched and recovered. This also specifies inclusion and
            exclusion rules that determine the directories to index.
        is_direct_archive_enabled (bool): Specifies if this is a direct
            archive backup job.
        is_native_format (bool): Specifies if native format should be used for
            archiving, applicable for only direct archive jobs.
        leverage_storage_snapshots (bool): Specifies whether to leverage the
            storage array based snapshots for this backup job. To leverage
            storage snapshots, the storage array has to be registered as a
            source. If storage based snapshots can not be taken, job will
            fallback to the default backup method.
        leverage_storage_snapshots_for_hyperflex (bool): Specifies whether to
            leverage Hyperflex as the storage snapshot array
        name (string): Specifies the name of the Protection Job.
        parent_source_id (long|int): Specifies the id of the registered
            Protection Source that is the parent of the Objects that may be
            protected by this Job. For example when a vCenter Server is
            registered on a Cohesity Cluster, the Cohesity Cluster assigns a
            unique id to this field that represents the vCenter Server.
        perform_source_side_dedup (bool): Specifies whether source side dedupe
            should be performed or not.
        policy_id (string): Specifies the unique id of the Protection Policy
            associated with the Protection Job. The Policy provides retry
            settings, Protection Schedules, Priority, SLA, etc. The Job
            defines the Storage Domain (View Box), the Objects to Protect (if
            applicable), Start Time, Indexing settings, etc.
        post_backup_script (BackupScript): Specifies the script associated
            with the backup job. This field must be specified for 'kPhysical'
            jobs. This script will be executed post backup run.
        pre_backup_script (BackupScript): Specifies the script associated with
            the backup job. This field must be specified for 'kPhysical' jobs.
            This script will be executed pre backup run. The 'remoteScript'
            field will be used for remote adapter jobs and 'preBackupScript'
            field will be used for 'kPhysical' jobs.
        priority (PriorityEnum): Specifies the priority of execution for a
            Protection Job. Cohesity supports concurrent backups but if the
            number of Jobs exceeds the ability to process Jobs, the specified
            priority determines the execution Job priority. This field also
            specifies the replication priority. 'kLow' indicates lowest
            execution priority for a Protection job. 'kMedium' indicates
            medium execution priority for a Protection job. 'kHigh' indicates
            highest execution priority for a Protection job.
        qos_type (QosTypeEnum): Specifies the QoS policy type to use for this
            Protection Job. 'kBackupHDD' indicates the Cohesity Cluster writes
            data directly to the HDD tier for this Protection Job. This is the
            recommended setting. 'kBackupSSD' indicates the Cohesity Cluster
            writes data directly to the SSD tier for this Protection Job. Only
            specify this policy if you need fast ingest speed for a small
            number of Protection Jobs.
        quiesce (bool): Indicates if the App-Consistent option is enabled for
            this Job. If the option is enabled, the Cohesity Cluster quiesces
            the file system and applications before taking
            Application-Consistent Snapshots. VMware Tools must be installed
            on the guest Operating System.
        remote_script (RemoteJobScript): For a Remote Adapter 'kPuppeteer'
            Job, this field specifies the settings about the remote script
            that will be executed by this Job. Only specify this field for
            Remote Adapter 'kPuppeteer' Jobs.
        remote_view_name (string): Specifies the remote view name to use for
            view overwrite.
        source_ids (list of long|int): Array of Protected Source Objects.
            Specifies the list of Object ids from the Protection Source to
            protect (or back up) by the Protection Job. An Object in this list
            may be descendant of another Object in this list. For example a
            Datacenter could be selected but its child Host excluded. However,
            a child VM under the Host could be explicitly selected to be
            protected. Both the Datacenter and the VM are listed.
        source_special_parameters (list of SourceSpecialParameter): Array of
            Special Source Parameters.  Specifies additional settings that can
            apply to a subset of the Sources listed in the Protection Job. For
            example, you can specify a list of files and folders to protect
            instead of protecting the entire Physical Server. If this field's
            setting conflicts with environmentParameters, then this setting
            will be used. Specific volume selections must be passed in here to
            take effect.
        start_time (TimeOfDay): Specifies the time of day to start the
            Protection Schedule. This is optional and only applicable if the
            Protection Policy defines a monthly or a daily Protection
            Schedule. Default value is 02:00 AM.
        timezone (string): Specifies the timezone to use when calculating time
            for this Protection Job such as the Job start time. Specify the
            timezone in the following format: "Area/Location", for example:
            "America/New_York".
        user_specified_tags (list of string): Tags associated with the job.
            User can specify tags/keywords that can indexed by Yoda and can be
            later searched in UI. For example, user can create a 'kPuppeteer'
            job to backup Oracle DB for 'payroll' department. User can specify
            following tags: 'payroll', 'Oracle_DB'.
        view_box_id (long|int): Specifies the Storage Domain (View Box) id
            where this Job writes data.
        view_name (string): For a Remote Adapter 'kPuppeteer' Job or a 'kView'
            Job, this field specifies a View name that should be protected.
            Specify this field when creating a Protection Job for the first
            time for a View. If this field is specified, ParentSourceId,
            SourceIds, and ExcludeSourceIds should not be specified.
        vm_tag_ids (list of long|int): Array of Arrays of VMs Tags Ids that
            Specify VMs to Protect.  Optionally specify a list of VMs to
            protect by listing Protection Source ids of VM Tags in this two
            dimensional array. Using this two dimensional array of Tag ids,
            the Cluster generates a list of VMs to protect which are derived
            from intersections of the inner arrays and union of the outer
            array, as shown by the following example. To protect only 'Eng'
            VMs in the East and all the VMs in the West, specify the following
            tag id array: [ [1101, 2221], [3031] ], where 1101 is the 'Eng' VM
            Tag id, 2221 is the 'East' VM Tag id and 3031 is the 'West' VM Tag
            id. The inner array [1101, 2221] produces a list of VMs that are
            both tagged with 'Eng' and 'East' (an intersection). The outer
            array combines the list from the inner array with list of VMs
            tagged with 'West' (a union). The list of resulting VMs are
            protected by this Job.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "policy_id":'policyId',
        "view_box_id":'viewBoxId',
        "leverage_san_transport":'LeverageSanTransport',
        "abort_in_blackout_period":'abortInBlackoutPeriod',
        "alerting_config":'alertingConfig',
        "alerting_policy":'alertingPolicy',
        "cloud_parameters":'cloudParameters',
        "continue_on_quiesce_failure":'continueOnQuiesceFailure',
        "create_remote_view":'createRemoteView',
        "data_migration_policy":'dataMigrationPolicy',
        "dedup_disabled_source_ids":'dedupDisabledSourceIds',
        "description":'description',
        "end_time_usecs":'endTimeUsecs',
        "environment":'environment',
        "environment_parameters":'environmentParameters',
        "exclude_source_ids":'excludeSourceIds',
        "exclude_vm_tag_ids":'excludeVmTagIds',
        "full_protection_sla_time_mins":'fullProtectionSlaTimeMins',
        "full_protection_start_time":'fullProtectionStartTime',
        "incremental_protection_sla_time_mins":'incrementalProtectionSlaTimeMins',
        "incremental_protection_start_time":'incrementalProtectionStartTime',
        "indexing_policy":'indexingPolicy',
        "is_direct_archive_enabled":'isDirectArchiveEnabled',
        "is_native_format":'isNativeFormat',
        "leverage_storage_snapshots":'leverageStorageSnapshots',
        "leverage_storage_snapshots_for_hyperflex":'leverageStorageSnapshotsForHyperflex',
        "parent_source_id":'parentSourceId',
        "perform_source_side_dedup":'performSourceSideDedup',
        "post_backup_script":'postBackupScript',
        "pre_backup_script":'preBackupScript',
        "priority":'priority',
        "qos_type":'qosType',
        "quiesce":'quiesce',
        "remote_script":'remoteScript',
        "remote_view_name":'remoteViewName',
        "source_ids":'sourceIds',
        "source_special_parameters":'sourceSpecialParameters',
        "start_time":'startTime',
        "timezone":'timezone',
        "user_specified_tags":'userSpecifiedTags',
        "view_name":'viewName',
        "vm_tag_ids":'vmTagIds'
    }

    def __init__(self,
                 name=None,
                 policy_id=None,
                 view_box_id=None,
                 leverage_san_transport=None,
                 abort_in_blackout_period=None,
                 alerting_config=None,
                 alerting_policy=None,
                 cloud_parameters=None,
                 continue_on_quiesce_failure=None,
                 create_remote_view=None,
                 data_migration_policy=None,
                 dedup_disabled_source_ids=None,
                 description=None,
                 end_time_usecs=None,
                 environment=None,
                 environment_parameters=None,
                 exclude_source_ids=None,
                 exclude_vm_tag_ids=None,
                 full_protection_sla_time_mins=None,
                 full_protection_start_time=None,
                 incremental_protection_sla_time_mins=None,
                 incremental_protection_start_time=None,
                 indexing_policy=None,
                 is_direct_archive_enabled=None,
                 is_native_format=None,
                 leverage_storage_snapshots=None,
                 leverage_storage_snapshots_for_hyperflex=None,
                 parent_source_id=None,
                 perform_source_side_dedup=None,
                 post_backup_script=None,
                 pre_backup_script=None,
                 priority=None,
                 qos_type=None,
                 quiesce=None,
                 remote_script=None,
                 remote_view_name=None,
                 source_ids=None,
                 source_special_parameters=None,
                 start_time=None,
                 timezone=None,
                 user_specified_tags=None,
                 view_name=None,
                 vm_tag_ids=None):
        """Constructor for the ProtectionJobRequestBody class"""

        # Initialize members of the class
        self.leverage_san_transport = leverage_san_transport
        self.abort_in_blackout_period = abort_in_blackout_period
        self.alerting_config = alerting_config
        self.alerting_policy = alerting_policy
        self.cloud_parameters = cloud_parameters
        self.continue_on_quiesce_failure = continue_on_quiesce_failure
        self.create_remote_view = create_remote_view
        self.data_migration_policy = data_migration_policy
        self.dedup_disabled_source_ids = dedup_disabled_source_ids
        self.description = description
        self.end_time_usecs = end_time_usecs
        self.environment = environment
        self.environment_parameters = environment_parameters
        self.exclude_source_ids = exclude_source_ids
        self.exclude_vm_tag_ids = exclude_vm_tag_ids
        self.full_protection_sla_time_mins = full_protection_sla_time_mins
        self.full_protection_start_time = full_protection_start_time
        self.incremental_protection_sla_time_mins = incremental_protection_sla_time_mins
        self.incremental_protection_start_time = incremental_protection_start_time
        self.indexing_policy = indexing_policy
        self.is_direct_archive_enabled = is_direct_archive_enabled
        self.is_native_format = is_native_format
        self.leverage_storage_snapshots = leverage_storage_snapshots
        self.leverage_storage_snapshots_for_hyperflex = leverage_storage_snapshots_for_hyperflex
        self.name = name
        self.parent_source_id = parent_source_id
        self.perform_source_side_dedup = perform_source_side_dedup
        self.policy_id = policy_id
        self.post_backup_script = post_backup_script
        self.pre_backup_script = pre_backup_script
        self.priority = priority
        self.qos_type = qos_type
        self.quiesce = quiesce
        self.remote_script = remote_script
        self.remote_view_name = remote_view_name
        self.source_ids = source_ids
        self.source_special_parameters = source_special_parameters
        self.start_time = start_time
        self.timezone = timezone
        self.user_specified_tags = user_specified_tags
        self.view_box_id = view_box_id
        self.view_name = view_name
        self.vm_tag_ids = vm_tag_ids


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
        name = dictionary.get('name')
        policy_id = dictionary.get('policyId')
        view_box_id = dictionary.get('viewBoxId')
        leverage_san_transport = dictionary.get('LeverageSanTransport')
        abort_in_blackout_period = dictionary.get('abortInBlackoutPeriod')
        alerting_config = cohesity_management_sdk.models.alerting_config.AlertingConfig.from_dictionary(dictionary.get('alertingConfig')) if dictionary.get('alertingConfig') else None
        alerting_policy = dictionary.get('alertingPolicy')
        cloud_parameters = cohesity_management_sdk.models.cloud_parameters.CloudParameters.from_dictionary(dictionary.get('cloudParameters')) if dictionary.get('cloudParameters') else None
        continue_on_quiesce_failure = dictionary.get('continueOnQuiesceFailure')
        create_remote_view = dictionary.get('createRemoteView')
        data_migration_policy = cohesity_management_sdk.models.data_migration_policy.DataMigrationPolicy.from_dictionary(dictionary.get('dataMigrationPolicy')) if dictionary.get('dataMigrationPolicy') else None
        dedup_disabled_source_ids = dictionary.get('dedupDisabledSourceIds')
        description = dictionary.get('description')
        end_time_usecs = dictionary.get('endTimeUsecs')
        environment = dictionary.get('environment')
        environment_parameters = cohesity_management_sdk.models.environment_type_job_parameters.EnvironmentTypeJobParameters.from_dictionary(dictionary.get('environmentParameters')) if dictionary.get('environmentParameters') else None
        exclude_source_ids = dictionary.get('excludeSourceIds')
        exclude_vm_tag_ids = dictionary.get('excludeVmTagIds')
        full_protection_sla_time_mins = dictionary.get('fullProtectionSlaTimeMins')
        full_protection_start_time = cohesity_management_sdk.models.time_of_day.TimeOfDay.from_dictionary(dictionary.get('fullProtectionStartTime')) if dictionary.get('fullProtectionStartTime') else None
        incremental_protection_sla_time_mins = dictionary.get('incrementalProtectionSlaTimeMins')
        incremental_protection_start_time = cohesity_management_sdk.models.time_of_day.TimeOfDay.from_dictionary(dictionary.get('incrementalProtectionStartTime')) if dictionary.get('incrementalProtectionStartTime') else None
        indexing_policy = cohesity_management_sdk.models.indexing_policy.IndexingPolicy.from_dictionary(dictionary.get('indexingPolicy')) if dictionary.get('indexingPolicy') else None
        is_direct_archive_enabled = dictionary.get('isDirectArchiveEnabled')
        is_native_format = dictionary.get('isNativeFormat')
        leverage_storage_snapshots = dictionary.get('leverageStorageSnapshots')
        leverage_storage_snapshots_for_hyperflex = dictionary.get('leverageStorageSnapshotsForHyperflex')
        parent_source_id = dictionary.get('parentSourceId')
        perform_source_side_dedup = dictionary.get('performSourceSideDedup')
        post_backup_script = cohesity_management_sdk.models.backup_script.BackupScript.from_dictionary(dictionary.get('postBackupScript')) if dictionary.get('postBackupScript') else None
        pre_backup_script = cohesity_management_sdk.models.backup_script.BackupScript.from_dictionary(dictionary.get('preBackupScript')) if dictionary.get('preBackupScript') else None
        priority = dictionary.get('priority')
        qos_type = dictionary.get('qosType')
        quiesce = dictionary.get('quiesce')
        remote_script = cohesity_management_sdk.models.remote_job_script.RemoteJobScript.from_dictionary(dictionary.get('remoteScript')) if dictionary.get('remoteScript') else None
        remote_view_name = dictionary.get('remoteViewName')
        source_ids = dictionary.get('sourceIds')
        source_special_parameters = None
        if dictionary.get('sourceSpecialParameters') != None:
            source_special_parameters = list()
            for structure in dictionary.get('sourceSpecialParameters'):
                source_special_parameters.append(cohesity_management_sdk.models.source_special_parameter.SourceSpecialParameter.from_dictionary(structure))
        start_time = cohesity_management_sdk.models.time_of_day.TimeOfDay.from_dictionary(dictionary.get('startTime')) if dictionary.get('startTime') else None
        timezone = dictionary.get('timezone')
        user_specified_tags = dictionary.get('userSpecifiedTags')
        view_name = dictionary.get('viewName')
        vm_tag_ids = dictionary.get('vmTagIds')

        # Return an object of this model
        return cls(name,
                   policy_id,
                   view_box_id,
                   leverage_san_transport,
                   abort_in_blackout_period,
                   alerting_config,
                   alerting_policy,
                   cloud_parameters,
                   continue_on_quiesce_failure,
                   create_remote_view,
                   data_migration_policy,
                   dedup_disabled_source_ids,
                   description,
                   end_time_usecs,
                   environment,
                   environment_parameters,
                   exclude_source_ids,
                   exclude_vm_tag_ids,
                   full_protection_sla_time_mins,
                   full_protection_start_time,
                   incremental_protection_sla_time_mins,
                   incremental_protection_start_time,
                   indexing_policy,
                   is_direct_archive_enabled,
                   is_native_format,
                   leverage_storage_snapshots,
                   leverage_storage_snapshots_for_hyperflex,
                   parent_source_id,
                   perform_source_side_dedup,
                   post_backup_script,
                   pre_backup_script,
                   priority,
                   qos_type,
                   quiesce,
                   remote_script,
                   remote_view_name,
                   source_ids,
                   source_special_parameters,
                   start_time,
                   timezone,
                   user_specified_tags,
                   view_name,
                   vm_tag_ids)


