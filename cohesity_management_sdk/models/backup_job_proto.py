# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.alerting_policy_proto
import cohesity_management_sdk.models.backup_source_params
import cohesity_management_sdk.models.backup_job_proto_dr_to_cloud_params
import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.env_backup_params
import cohesity_management_sdk.models.backup_job_proto_exclude_source
import cohesity_management_sdk.models.backup_job_proto_exclusion_time_range
import cohesity_management_sdk.models.job_policy_proto
import cohesity_management_sdk.models.indexing_policy_proto
import cohesity_management_sdk.models.universal_id_proto
import cohesity_management_sdk.models.backup_job_pre_or_post_script
import cohesity_management_sdk.models.backup_job_proto_backup_source
import cohesity_management_sdk.models.time
import cohesity_management_sdk.models.stubbing_policy_proto
import cohesity_management_sdk.models.user_information
import cohesity_management_sdk.models.physical_file_backup_params_global_include_exclude

class BackupJobProto(object):

    """Implementation of the 'BackupJobProto' model.

    TODO: type model description here.

    Attributes:
        abort_in_exclusion_window (bool): This field determines whether a
            backup run should be aborted when it hits an exclusion window
            (assuming that it was started earlier when it was not in an
            exclusion window).
        alerting_policy (AlertingPolicyProto): TODO: type description here.
        backup_qos_principal (int): The backup QoS principal to use for the
            backup job.
        backup_source_params (list of BackupSourceParams): This contains
            additional backup params that are applicable to sources that are
            captured as part of the backup job. NOTE: The sources could point
            to higher level entities (such as a "Cluster" in VMware
            environment), but the source params captured here will not be for
            the matching higher level entity, but instead be for leaf-level
            entities (such as VMs).
        continue_on_quiesce_failure (bool): Whether to continue backing up on
            quiesce failure.
        create_remote_view (bool): If set to false, a remote view will not be
            created. If set to true and: 1) Remote view name is not provided
            by the user, a remote view is created with the same name as source
            view name. 2) Remote view name is provided by the user, a remote
            view is created with the given name.
        dedup_disabled_source_id_vec (list of long|int): List of source ids
            for which source side dedup is disabled from the backup job.
        deletion_status (int): Determines if the job (and associated backups)
            should be deleted. Once a job has been deleted, its status cannot
            be changed.
        description (string): Job description (as entered by the user).
        dr_to_cloud_params (BackupJobProtoDRToCloudParams): A Proto needed in
            case objects backed up by this job need to DR to cloud. "Fail
            over" signifies the mechanism to move the workload to cloud.
        eh_parent_source (EntityProto): Specifies the attributes and the
            latest statistics about an entity.
        end_time_usecs (long|int): The time (in usecs) after which no backup
            for the job should be scheduled.
        env_backup_params (EnvBackupParams): Message to capture any additional
            environment specific backup params at the job level.
        exclude_sources (list of BackupJobProtoExcludeSource): The list of
            sources to exclude from backups. These can have non-leaf-level
            entities, but it's up to the creator to ensure that a child of
            these sources hasn't been explicitly added to 'sources'.
        exclude_sources_deprecated (list of EntityProto): The list of sources
            to exclude from backups. These can have non-leaf-level entities,
            but it's up to the creator to ensure that a child of these sources
            hasn't been explicitly added to 'sources'.
        exclusion_ranges (list of BackupJobProtoExclusionTimeRange): Do not
            run backups in these time-ranges.
        full_backup_job_policy (JobPolicyProto): A message that specifies the
            policies to use for a job.
        full_backup_sla_time_mins (long|int): Same as 'sla_time_mins' above,
            but applies to full backups. NOTE: This value is considered only
            for full backups that are excepted i.e either scheduled or the
            first full backup and not for full backups that happen as a result
            of incremental backup failure.
        global_include_exclude (PhysicalFileBackupParams_GlobalIncludeExclude):
            Determines global include and exclude filters
            which are applied to all sources in a physical job.
        indexing_policy (IndexingPolicyProto): Proto to encapsulate file level
            indexing policy for VMs in a backup job.
        is_active (bool): Whether the backup job is active or not. Details
            about what an active job is can be found here:
            https://goo.gl/1mLvS3.
        is_continuous_snapshotting_enabled (bool): Indicates if Magneto should
            continue taking source snapshots even if there is a pending run.
        is_deleted (bool): Tracks whether the backup job has actually been
            deleted.
        is_direct_archive_enabled (bool): This field is set to true if this is
            a direct archive backup job.
        is_direct_archive_native_format_enabled (bool): This field is set to
            true if native format should be used for archiving. Applicable for
            only direct archive jobs.
        is_paused (bool): Whether the backup job is paused. New backup runs
            are not scheduled for the paused backup job. Active run of a
            backup job (if any) is not impacted.
        is_rpo_job (bool): Whether the backup job is an RPO policy job. These
            jobs are hidden from the user, and are created internally to have
            a backup schedule for the given source.
        job_creation_time_usecs (long|int): Time when this job was first
            created.
        job_id (long|int): A unique id for locally created jobs. This should
            only be used to identify jobs created on the local cluster. When
            Iris communicates with Magneto, Iris can continue to use this
            job_id field, which will always be assumed to refer to locally
            created jobs.  For remotely created jobs, the 'job_uid' field
            should be used. The only time Iris should ever need to refer to a
            remote job is when restoring an object from a remote snapshot. In
            all such cases, Iris should use the job_uid field.
        job_policy (JobPolicyProto): A message that specifies the policies to
            use for a job.
        job_uid (UniversalIdProto): TODO: type description here.
        last_modification_time_usecs (long|int): Time when this job
            description was last updated.
        last_pause_modification_time_usecs (long|int): Time when the job was
            last paused or unpaused.
        last_pause_reason (int): Last reason for pausing the backup job.
            Capturing the reason will help in resuming only the jobs that were
            paused because of a reason once the reason for pausing is not
            applicable.
        last_updated_username (string): The user who modified the job most
            recently.
        leverage_san_transport (bool): This is set to true by the user in
            order to backup the objects via a dedicated storage area network
            (SAN), as opposed to transport via LAN or management network.
            NOTE: Not all adapters support this method. Currently only VMware.
        leverage_storage_snapshots (bool): Whether to leverage the storage
            array based snapshots for this backup job. To leverage storage
            snapshots, the storage array has to be registered as a source. If
            storage based snapshots can not be taken, job will fallback to the
            default backup method. NOTE: This will be set for Pure snapshots.
        leverage_storage_snapshots_for_hyperflex (bool): This is set to true
            by the user if hyperflex snapshots are requested NOTE: If this is
            set to true, then leverage_storage_snapshots above should be
            false.
        log_backup_job_policy (JobPolicyProto): A message that specifies the
            policies to use for a job.
        max_allowed_source_snapshots (int): Determines the maximum number of
            source snapshots allowed for a given entity in the job. This is
            only applicable if 'is_continuous_snapshotting_enabled' is set to
            true.
        name (string): The name of this backup job. This must be unique across
            all jobs.
        num_snapshots_to_keep_on_primary (long|int): Specifies how many recent
            snapshots of each backed up entity to retain on the primary
            environment. If not specified, then snapshots will not be be
            deleted from the primary environment. NOTE: This is only
            applicable for certain environments like kPure.
        parent_source (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        perform_source_side_dedup (bool): Whether or not to perform source
            side dedup.
        policy_applied_time_msecs (long|int): Epoch time in milliseconds when
            the policy was last applied to this job. This field will be used
            to determine whether a policy has changed after it was applied to
            a particular job.
        policy_id (string): Id of the policy being applied to the backup job.
            It is expected to be of the form
            "cluster_id:cluster_instance_id:local_identifier".
        policy_name (string): The name of the policy referred to by
            policy_uid. This field can be stale and should not be relied upon
            for the latest name.
        post_backup_script (BackupJobPreOrPostScript): A message to
            encapsulate the pre and post scripts associated with a backup job.
            Pre script is executed before backup run of a job starts. Post
            script is executed after backup run of a job finishes. Currently,
            pre and post script is only supported for backup job of type
            'kPuppeteer' and agent-based backup jobs.
        pre_script (BackupJobPreOrPostScript): A message to encapsulate the
            pre and post scripts associated with a backup job. Pre script is
            executed before backup run of a job starts. Post script is
            executed after backup run of a job finishes. Currently, pre and
            post script is only supported for backup job of type 'kPuppeteer'
            and agent-based backup jobs.
        primary_job_uid (UniversalIdProto): TODO: type description here.
        priority (int): The priority for the job. This is used at admission
            time - all admitted jobs are treated equally. This is also used to
            determine the Madrox replication priority.
        quiesce (bool): Whether to take app-consistent snapshots by quiescing
            apps and the filesystem before taking a backup.
        remote_job_uids (list of UniversalIdProto): The globally unique ids of
            all remote jobs that are linked to this job (because of incoming
            replications). This field will only be populated for locally
            created jobs. This field is populated only for the local(stub) job
            during incoming replications. In the most common case of one
            cluster replicating to another, this field will only have one
            entry (which is the id of the job on Tx side) and matches the
            primary_job_uid. This will have multiple entries in the following
            situation: A->B, A->C replication. The backup is failed over to B,
            and B now starts replicating to C. In this case, the stub job at C
            will have two entries. One is the job id from cluster A, and
            another is the local(stub) job uid from B. Also note that since
            the job originated from A, primary_job_uid for all the replicated
            instances of this job across multiple clusters will remain the
            same (which is equal to the job id from the original cluster A).
        remote_view_name (string): A human readable name of the remote view. A
            remote view is created with name overwriting the latest snapshot.
        required_feature_vec (list of string): The features that are strictly
            required to be supported by the cluster of the backup job. This is
            currently used in the following cases: 1. Tx cluster looks at the
            Rx cluster's supported features and replicates the backup job only
            if all the features captured here are supported. 2. When
            performing remote restore of a backup job from an archival, this
            job will be retrieved only if the cluster supports all the
            features listed here.
        sla_time_mins (long|int): If specified, this variable determines the
            amount of time (after backup has started) in which backup is
            expected to finish for this job. An SLA violation is counted
            against this job if the amount of time taken exceeds this amount.
        source_filters (SourceFilters): Determines include and exclude filters
            which are applied to entities in a backup source. For SQL, this
            will be applicable only for auto protect sources.
        sources (list of BackupJobProtoBackupSource): The list of sources that
            should be backed up. A source in this list could be a descendant
            of another source in the list (this will be used when specifying
            override backup schedules).
        start_time (Time): A message to encapusulate time of a day. Users of
            this proto will have to store the timezone information separately.
            For example, when this proto is part of a backup job, timezone of
            the backup job is applied to get the absolute time.
        stubbing_policy (StubbingPolicyProto): Stubbing jobs do not use
            protection policies. Instead, schedule and retention policy will
            be embedded in the BackupJobProto.
        tag_vec (list of string): Tags associated with the job. User can
            specify tags/keywords that can indexed by Yoda and can be later
            searched in UI. For example, user can create a 'kPuppeteer' job to
            backup Oracle DB for 'payroll' department. User can specify
            following tags: 'payroll', 'Oracle_DB'.
        timezone (string): Timezone of the backup job. All time fields (i.e.,
            TimeOfDay) in this backup job are stored wrt to this timezone.
            The time zones have unique names of the form "Area/Location", e.g.
            "America/New_York". We are using "America/Los_Angeles" as a
            default value so as to be backward compatible with pre-2.7 code.
        truncate_logs (bool): Whether to truncate logs after a backup run.
            This is currently only relevant for full or incremental backups in
            a SQL environment.
        mtype (int): The type of environment this backup job corresponds to.
        user_info (UserInformation): A message to encapsulate information
            about the user who made the request. Request should be filtered by
            these fields if specified so that only the objects that the user
            is permissioned for are returned. If both sid_vec & tenant_id are
            specified then an intersection of respective results should be
            returned.
        view_box_id (long|int): The view box to which data will be written.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "abort_in_exclusion_window":'abortInExclusionWindow',
        "alerting_policy":'alertingPolicy',
        "backup_qos_principal":'backupQosPrincipal',
        "backup_source_params":'backupSourceParams',
        "continue_on_quiesce_failure":'continueOnQuiesceFailure',
        "create_remote_view":'createRemoteView',
        "dedup_disabled_source_id_vec":'dedupDisabledSourceIdVec',
        "deletion_status":'deletionStatus',
        "description":'description',
        "dr_to_cloud_params":'drToCloudParams',
        "eh_parent_source":'ehParentSource',
        "end_time_usecs":'endTimeUsecs',
        "env_backup_params":'envBackupParams',
        "exclude_sources":'excludeSources',
        "exclude_sources_deprecated":'excludeSources_DEPRECATED',
        "exclusion_ranges":'exclusionRanges',
        "full_backup_job_policy":'fullBackupJobPolicy',
        "full_backup_sla_time_mins":'fullBackupSlaTimeMins',
        "global_include_exclude":'globalIncludeExclude',
        "indexing_policy":'indexingPolicy',
        "is_active":'isActive',
        "is_continuous_snapshotting_enabled":'isContinuousSnapshottingEnabled',
        "is_deleted":'isDeleted',
        "is_direct_archive_enabled":'isDirectArchiveEnabled',
        "is_direct_archive_native_format_enabled":'isDirectArchiveNativeFormatEnabled',
        "is_paused":'isPaused',
        "is_rpo_job":'isRpoJob',
        "job_creation_time_usecs":'jobCreationTimeUsecs',
        "job_id":'jobId',
        "job_policy":'jobPolicy',
        "job_uid":'jobUid',
        "last_modification_time_usecs":'lastModificationTimeUsecs',
        "last_pause_modification_time_usecs":'lastPauseModificationTimeUsecs',
        "last_pause_reason":'lastPauseReason',
        "last_updated_username":'lastUpdatedUsername',
        "leverage_san_transport":'leverageSanTransport',
        "leverage_storage_snapshots":'leverageStorageSnapshots',
        "leverage_storage_snapshots_for_hyperflex":'leverageStorageSnapshotsForHyperflex',
        "log_backup_job_policy":'logBackupJobPolicy',
        "max_allowed_source_snapshots":'maxAllowedSourceSnapshots',
        "name":'name',
        "num_snapshots_to_keep_on_primary":'numSnapshotsToKeepOnPrimary',
        "parent_source":'parentSource',
        "perform_source_side_dedup":'performSourceSideDedup',
        "policy_applied_time_msecs":'policyAppliedTimeMsecs',
        "policy_id":'policyId',
        "policy_name":'policyName',
        "post_backup_script":'postBackupScript',
        "pre_script":'preScript',
        "primary_job_uid":'primaryJobUid',
        "priority":'priority',
        "quiesce":'quiesce',
        "remote_job_uids":'remoteJobUids',
        "remote_view_name":'remoteViewName',
        "required_feature_vec":'requiredFeatureVec',
        "sla_time_mins":'slaTimeMins',
        "source_filters":'sourceFilters',
        "sources":'sources',
        "start_time":'startTime',
        "stubbing_policy":'stubbingPolicy',
        "tag_vec":'tagVec',
        "timezone":'timezone',
        "truncate_logs":'truncateLogs',
        "mtype":'type',
        "user_info":'userInfo',
        "view_box_id":'viewBoxId'
    }

    def __init__(self,
                 abort_in_exclusion_window=None,
                 alerting_policy=None,
                 backup_qos_principal=None,
                 backup_source_params=None,
                 continue_on_quiesce_failure=None,
                 create_remote_view=None,
                 dedup_disabled_source_id_vec=None,
                 deletion_status=None,
                 description=None,
                 dr_to_cloud_params=None,
                 eh_parent_source=None,
                 end_time_usecs=None,
                 env_backup_params=None,
                 exclude_sources=None,
                 exclude_sources_deprecated=None,
                 exclusion_ranges=None,
                 full_backup_job_policy=None,
                 full_backup_sla_time_mins=None,
                 global_include_exclude=None,
                 indexing_policy=None,
                 is_active=None,
                 is_continuous_snapshotting_enabled=None,
                 is_deleted=None,
                 is_direct_archive_enabled=None,
                 is_direct_archive_native_format_enabled=None,
                 is_paused=None,
                 is_rpo_job=None,
                 job_creation_time_usecs=None,
                 job_id=None,
                 job_policy=None,
                 job_uid=None,
                 last_modification_time_usecs=None,
                 last_pause_modification_time_usecs=None,
                 last_pause_reason=None,
                 last_updated_username=None,
                 leverage_san_transport=None,
                 leverage_storage_snapshots=None,
                 leverage_storage_snapshots_for_hyperflex=None,
                 log_backup_job_policy=None,
                 max_allowed_source_snapshots=None,
                 name=None,
                 num_snapshots_to_keep_on_primary=None,
                 parent_source=None,
                 perform_source_side_dedup=None,
                 policy_applied_time_msecs=None,
                 policy_id=None,
                 policy_name=None,
                 post_backup_script=None,
                 pre_script=None,
                 primary_job_uid=None,
                 priority=None,
                 quiesce=None,
                 remote_job_uids=None,
                 remote_view_name=None,
                 required_feature_vec=None,
                 sla_time_mins=None,
                 source_filters=None,
                 sources=None,
                 start_time=None,
                 stubbing_policy=None,
                 tag_vec=None,
                 timezone=None,
                 truncate_logs=None,
                 mtype=None,
                 user_info=None,
                 view_box_id=None):
        """Constructor for the BackupJobProto class"""

        # Initialize members of the class
        self.abort_in_exclusion_window = abort_in_exclusion_window
        self.alerting_policy = alerting_policy
        self.backup_qos_principal = backup_qos_principal
        self.backup_source_params = backup_source_params
        self.continue_on_quiesce_failure = continue_on_quiesce_failure
        self.create_remote_view = create_remote_view
        self.dedup_disabled_source_id_vec = dedup_disabled_source_id_vec
        self.deletion_status = deletion_status
        self.description = description
        self.dr_to_cloud_params = dr_to_cloud_params
        self.eh_parent_source = eh_parent_source
        self.end_time_usecs = end_time_usecs
        self.env_backup_params = env_backup_params
        self.exclude_sources = exclude_sources
        self.exclude_sources_deprecated = exclude_sources_deprecated
        self.exclusion_ranges = exclusion_ranges
        self.full_backup_job_policy = full_backup_job_policy
        self.full_backup_sla_time_mins = full_backup_sla_time_mins
        self.global_include_exclude = global_include_exclude
        self.indexing_policy = indexing_policy
        self.is_active = is_active
        self.is_continuous_snapshotting_enabled = is_continuous_snapshotting_enabled
        self.is_deleted = is_deleted
        self.is_direct_archive_enabled = is_direct_archive_enabled
        self.is_direct_archive_native_format_enabled = is_direct_archive_native_format_enabled
        self.is_paused = is_paused
        self.is_rpo_job = is_rpo_job
        self.job_creation_time_usecs = job_creation_time_usecs
        self.job_id = job_id
        self.job_policy = job_policy
        self.job_uid = job_uid
        self.last_modification_time_usecs = last_modification_time_usecs
        self.last_pause_modification_time_usecs = last_pause_modification_time_usecs
        self.last_pause_reason = last_pause_reason
        self.last_updated_username = last_updated_username
        self.leverage_san_transport = leverage_san_transport
        self.leverage_storage_snapshots = leverage_storage_snapshots
        self.leverage_storage_snapshots_for_hyperflex = leverage_storage_snapshots_for_hyperflex
        self.log_backup_job_policy = log_backup_job_policy
        self.max_allowed_source_snapshots = max_allowed_source_snapshots
        self.name = name
        self.num_snapshots_to_keep_on_primary = num_snapshots_to_keep_on_primary
        self.parent_source = parent_source
        self.perform_source_side_dedup = perform_source_side_dedup
        self.policy_applied_time_msecs = policy_applied_time_msecs
        self.policy_id = policy_id
        self.policy_name = policy_name
        self.post_backup_script = post_backup_script
        self.pre_script = pre_script
        self.primary_job_uid = primary_job_uid
        self.priority = priority
        self.quiesce = quiesce
        self.remote_job_uids = remote_job_uids
        self.remote_view_name = remote_view_name
        self.required_feature_vec = required_feature_vec
        self.sla_time_mins = sla_time_mins
        self.source_filters = source_filters
        self.sources = sources
        self.start_time = start_time
        self.stubbing_policy = stubbing_policy
        self.tag_vec = tag_vec
        self.timezone = timezone
        self.truncate_logs = truncate_logs
        self.mtype = mtype
        self.user_info = user_info
        self.view_box_id = view_box_id


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
        abort_in_exclusion_window = dictionary.get('abortInExclusionWindow')
        alerting_policy = cohesity_management_sdk.models.alerting_policy_proto.AlertingPolicyProto.from_dictionary(dictionary.get('alertingPolicy')) if dictionary.get('alertingPolicy') else None
        backup_qos_principal = dictionary.get('backupQosPrincipal')
        backup_source_params = None
        if dictionary.get('backupSourceParams') != None:
            backup_source_params = list()
            for structure in dictionary.get('backupSourceParams'):
                backup_source_params.append(cohesity_management_sdk.models.backup_source_params.BackupSourceParams.from_dictionary(structure))
        continue_on_quiesce_failure = dictionary.get('continueOnQuiesceFailure')
        create_remote_view = dictionary.get('createRemoteView')
        dedup_disabled_source_id_vec = dictionary.get('dedupDisabledSourceIdVec')
        deletion_status = dictionary.get('deletionStatus')
        description = dictionary.get('description')
        dr_to_cloud_params = cohesity_management_sdk.models.backup_job_proto_dr_to_cloud_params.BackupJobProtoDRToCloudParams.from_dictionary(dictionary.get('drToCloudParams')) if dictionary.get('drToCloudParams') else None
        eh_parent_source = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('ehParentSource')) if dictionary.get('ehParentSource') else None
        end_time_usecs = dictionary.get('endTimeUsecs')
        env_backup_params = cohesity_management_sdk.models.env_backup_params.EnvBackupParams.from_dictionary(dictionary.get('envBackupParams')) if dictionary.get('envBackupParams') else None
        exclude_sources = None
        if dictionary.get('excludeSources') != None:
            exclude_sources = list()
            for structure in dictionary.get('excludeSources'):
                exclude_sources.append(cohesity_management_sdk.models.backup_job_proto_exclude_source.BackupJobProtoExcludeSource.from_dictionary(structure))
        exclude_sources_deprecated = None
        if dictionary.get('excludeSources_DEPRECATED') != None:
            exclude_sources_deprecated = list()
            for structure in dictionary.get('excludeSources_DEPRECATED'):
                exclude_sources_deprecated.append(cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(structure))
        exclusion_ranges = None
        if dictionary.get('exclusionRanges') != None:
            exclusion_ranges = list()
            for structure in dictionary.get('exclusionRanges'):
                exclusion_ranges.append(cohesity_management_sdk.models.backup_job_proto_exclusion_time_range.BackupJobProtoExclusionTimeRange.from_dictionary(structure))
        full_backup_job_policy = cohesity_management_sdk.models.job_policy_proto.JobPolicyProto.from_dictionary(dictionary.get('fullBackupJobPolicy')) if dictionary.get('fullBackupJobPolicy') else None
        full_backup_sla_time_mins = dictionary.get('fullBackupSlaTimeMins')
        global_include_exclude = cohesity_management_sdk.models.physical_file_backup_params_global_include_exclude.PhysicalFileBackupParams_GlobalIncludeExclude.from_dictionary(dictionary.get('globalIncludeExclude')) if dictionary.get('globalIncludeExclude') else None
        indexing_policy = cohesity_management_sdk.models.indexing_policy_proto.IndexingPolicyProto.from_dictionary(dictionary.get('indexingPolicy')) if dictionary.get('indexingPolicy') else None
        is_active = dictionary.get('isActive')
        is_continuous_snapshotting_enabled = dictionary.get('isContinuousSnapshottingEnabled')
        is_deleted = dictionary.get('isDeleted')
        is_direct_archive_enabled = dictionary.get('isDirectArchiveEnabled')
        is_direct_archive_native_format_enabled = dictionary.get('isDirectArchiveNativeFormatEnabled')
        is_paused = dictionary.get('isPaused')
        is_rpo_job = dictionary.get('isRpoJob')
        job_creation_time_usecs = dictionary.get('jobCreationTimeUsecs')
        job_id = dictionary.get('jobId')
        job_policy = cohesity_management_sdk.models.job_policy_proto.JobPolicyProto.from_dictionary(dictionary.get('jobPolicy')) if dictionary.get('jobPolicy') else None
        job_uid = cohesity_management_sdk.models.universal_id_proto.UniversalIdProto.from_dictionary(dictionary.get('jobUid')) if dictionary.get('jobUid') else None
        last_modification_time_usecs = dictionary.get('lastModificationTimeUsecs')
        last_pause_modification_time_usecs = dictionary.get('lastPauseModificationTimeUsecs')
        last_pause_reason = dictionary.get('lastPauseReason')
        last_updated_username = dictionary.get('lastUpdatedUsername')
        leverage_san_transport = dictionary.get('leverageSanTransport')
        leverage_storage_snapshots = dictionary.get('leverageStorageSnapshots')
        leverage_storage_snapshots_for_hyperflex = dictionary.get('leverageStorageSnapshotsForHyperflex')
        log_backup_job_policy = cohesity_management_sdk.models.job_policy_proto.JobPolicyProto.from_dictionary(dictionary.get('logBackupJobPolicy')) if dictionary.get('logBackupJobPolicy') else None
        max_allowed_source_snapshots = dictionary.get('maxAllowedSourceSnapshots')
        name = dictionary.get('name')
        num_snapshots_to_keep_on_primary = dictionary.get('numSnapshotsToKeepOnPrimary')
        parent_source = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('parentSource')) if dictionary.get('parentSource') else None
        perform_source_side_dedup = dictionary.get('performSourceSideDedup')
        policy_applied_time_msecs = dictionary.get('policyAppliedTimeMsecs')
        policy_id = dictionary.get('policyId')
        policy_name = dictionary.get('policyName')
        post_backup_script = cohesity_management_sdk.models.backup_job_pre_or_post_script.BackupJobPreOrPostScript.from_dictionary(dictionary.get('postBackupScript')) if dictionary.get('postBackupScript') else None
        pre_script = cohesity_management_sdk.models.backup_job_pre_or_post_script.BackupJobPreOrPostScript.from_dictionary(dictionary.get('preScript')) if dictionary.get('preScript') else None
        primary_job_uid = cohesity_management_sdk.models.universal_id_proto.UniversalIdProto.from_dictionary(dictionary.get('primaryJobUid')) if dictionary.get('primaryJobUid') else None
        priority = dictionary.get('priority')
        quiesce = dictionary.get('quiesce')
        remote_job_uids = None
        if dictionary.get('remoteJobUids') != None:
            remote_job_uids = list()
            for structure in dictionary.get('remoteJobUids'):
                remote_job_uids.append(cohesity_management_sdk.models.universal_id_proto.UniversalIdProto.from_dictionary(structure))
        remote_view_name = dictionary.get('remoteViewName')
        required_feature_vec = dictionary.get('requiredFeatureVec')
        sla_time_mins = dictionary.get('slaTimeMins')
        source_filters = cohesity_management_sdk.models.source_filters.SourceFilters.from_dictionary(dictionary.get('sourceFilters')) if dictionary.get('sourceFilters') else None
        sources = None
        if dictionary.get('sources') != None:
            sources = list()
            for structure in dictionary.get('sources'):
                sources.append(cohesity_management_sdk.models.backup_job_proto_backup_source.BackupJobProtoBackupSource.from_dictionary(structure))
        start_time = cohesity_management_sdk.models.time.Time.from_dictionary(dictionary.get('startTime')) if dictionary.get('startTime') else None
        stubbing_policy = cohesity_management_sdk.models.stubbing_policy_proto.StubbingPolicyProto.from_dictionary(dictionary.get('stubbingPolicy')) if dictionary.get('stubbingPolicy') else None
        tag_vec = dictionary.get('tagVec')
        timezone = dictionary.get('timezone')
        truncate_logs = dictionary.get('truncateLogs')
        mtype = dictionary.get('type')
        user_info = cohesity_management_sdk.models.user_information.UserInformation.from_dictionary(dictionary.get('userInfo')) if dictionary.get('userInfo') else None
        view_box_id = dictionary.get('viewBoxId')

        # Return an object of this model
        return cls(abort_in_exclusion_window,
                   alerting_policy,
                   backup_qos_principal,
                   backup_source_params,
                   continue_on_quiesce_failure,
                   create_remote_view,
                   dedup_disabled_source_id_vec,
                   deletion_status,
                   description,
                   dr_to_cloud_params,
                   eh_parent_source,
                   end_time_usecs,
                   env_backup_params,
                   exclude_sources,
                   exclude_sources_deprecated,
                   exclusion_ranges,
                   full_backup_job_policy,
                   full_backup_sla_time_mins,
                   global_include_exclude,
                   indexing_policy,
                   is_active,
                   is_continuous_snapshotting_enabled,
                   is_deleted,
                   is_direct_archive_enabled,
                   is_direct_archive_native_format_enabled,
                   is_paused,
                   is_rpo_job,
                   job_creation_time_usecs,
                   job_id,
                   job_policy,
                   job_uid,
                   last_modification_time_usecs,
                   last_pause_modification_time_usecs,
                   last_pause_reason,
                   last_updated_username,
                   leverage_san_transport,
                   leverage_storage_snapshots,
                   leverage_storage_snapshots_for_hyperflex,
                   log_backup_job_policy,
                   max_allowed_source_snapshots,
                   name,
                   num_snapshots_to_keep_on_primary,
                   parent_source,
                   perform_source_side_dedup,
                   policy_applied_time_msecs,
                   policy_id,
                   policy_name,
                   post_backup_script,
                   pre_script,
                   primary_job_uid,
                   priority,
                   quiesce,
                   remote_job_uids,
                   remote_view_name,
                   required_feature_vec,
                   sla_time_mins,
                   source_filters,
                   sources,
                   start_time,
                   stubbing_policy,
                   tag_vec,
                   timezone,
                   truncate_logs,
                   mtype,
                   user_info,
                   view_box_id)


