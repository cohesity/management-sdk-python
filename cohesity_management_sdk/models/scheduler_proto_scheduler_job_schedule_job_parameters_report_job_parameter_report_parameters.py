# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class SchedulerProto_SchedulerJob_ScheduleJobParameters_ReportJobParameter_Report_Parameters(object):

    """Implementation of the 'SchedulerProto_SchedulerJob_ScheduleJobParameters_ReportJobParameter_Report_Parameters' model.

    TODO: type description here.


    Attributes:

        all_under_hierarchy (bool): Specifies if subtenants of the given
            tenants should be considered for report generation.
        compact_version (string): Specifies the Cohesity Agent software
            version.
        consecutive_failures (int): Specifies the number of consecutive
            failures.
        environment (string): Specifies the Environment for the entity being
            protected.
        exclude_users_within_alert_threshold (bool): User Quotas: Only the list
            of users who has exceeded the alert threshold will be returned.
        group_by (int): Specifies if the report should be grouped by any field.
        health_status (list of string): Specifies the Cohesity Agent health
            status.
        host_os_type (list of string): Specifies the OS type on which Cohesity
            Agent is installed.
        job_id (long|int): Specifies the id of the job for which to get the
            report data.
        job_name (string): Specifies the name of the job for which to get the
            report data.
        last_n_days (int): Specifies the number of days from current date for
            which the report data is to be fetched.
        object_ids (list of long|int): Specifies the object ids for which to
            get the report data.
        object_type (string): Specifies the object type for which to get the
            report data.
        registered_source_id (long|int): Specifies the registered source for
            which to get the report data.
        registered_source_ids (list of long|int): Specifies the registered
            sources for which to get the report data.
        rollup (string): Specifies the rollup(day/week/month) for protected
            object trends report.
        run_status (list of string): Specifies the run status for which to get
            the report data.
        sid (string): Specifies the sid of the user.
        tenant_id_vec (list of string): Specifies tenant ids for which report
            needs to be generated.
        timezone (string): Specifies the timezone.
        unix_uid (int): Specifies the unix uid of the user.
        vault_ids (list of long|int): Specifies the vault ids for which to get
            the report data.
        view_box_id (long|int): Specifies the view box for which to get the
            report data.
        view_name (string): Specifies the view name for which the report is
            required.
        viewbox_ids (list of long|int): Specifies the viewbox ids to filter by.
        vm_name (string): Specifies the VM name for which to get the report
            data.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "all_under_hierarchy":'allUnderHierarchy',
        "compact_version":'compactVersion',
        "consecutive_failures":'consecutiveFailures',
        "environment":'environment',
        "exclude_users_within_alert_threshold":'excludeUsersWithinAlertThreshold',
        "group_by":'groupBy',
        "health_status":'healthStatus',
        "host_os_type":'hostOsType',
        "job_id":'jobId',
        "job_name":'jobName',
        "last_n_days":'lastNDays',
        "object_ids":'objectIds',
        "object_type":'objectType',
        "registered_source_id":'registeredSourceId',
        "registered_source_ids":'registeredSourceIds',
        "rollup":'rollup',
        "run_status":'runStatus',
        "sid":'sid',
        "tenant_id_vec":'tenantIdVec',
        "timezone":'timezone',
        "unix_uid":'unixUid',
        "vault_ids":'vaultIds',
        "view_box_id":'viewBoxId',
        "view_name":'viewName',
        "viewbox_ids":'viewboxIds',
        "vm_name":'vmName',
    }
    def __init__(self,
                 all_under_hierarchy=None,
                 compact_version=None,
                 consecutive_failures=None,
                 environment=None,
                 exclude_users_within_alert_threshold=None,
                 group_by=None,
                 health_status=None,
                 host_os_type=None,
                 job_id=None,
                 job_name=None,
                 last_n_days=None,
                 object_ids=None,
                 object_type=None,
                 registered_source_id=None,
                 registered_source_ids=None,
                 rollup=None,
                 run_status=None,
                 sid=None,
                 tenant_id_vec=None,
                 timezone=None,
                 unix_uid=None,
                 vault_ids=None,
                 view_box_id=None,
                 view_name=None,
                 viewbox_ids=None,
                 vm_name=None,
            ):

        """Constructor for the SchedulerProto_SchedulerJob_ScheduleJobParameters_ReportJobParameter_Report_Parameters class"""

        # Initialize members of the class
        self.all_under_hierarchy = all_under_hierarchy
        self.compact_version = compact_version
        self.consecutive_failures = consecutive_failures
        self.environment = environment
        self.exclude_users_within_alert_threshold = exclude_users_within_alert_threshold
        self.group_by = group_by
        self.health_status = health_status
        self.host_os_type = host_os_type
        self.job_id = job_id
        self.job_name = job_name
        self.last_n_days = last_n_days
        self.object_ids = object_ids
        self.object_type = object_type
        self.registered_source_id = registered_source_id
        self.registered_source_ids = registered_source_ids
        self.rollup = rollup
        self.run_status = run_status
        self.sid = sid
        self.tenant_id_vec = tenant_id_vec
        self.timezone = timezone
        self.unix_uid = unix_uid
        self.vault_ids = vault_ids
        self.view_box_id = view_box_id
        self.view_name = view_name
        self.viewbox_ids = viewbox_ids
        self.vm_name = vm_name

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
        all_under_hierarchy = dictionary.get('allUnderHierarchy')
        compact_version = dictionary.get('compactVersion')
        consecutive_failures = dictionary.get('consecutiveFailures')
        environment = dictionary.get('environment')
        exclude_users_within_alert_threshold = dictionary.get('excludeUsersWithinAlertThreshold')
        group_by = dictionary.get('groupBy')
        health_status = dictionary.get("healthStatus")
        host_os_type = dictionary.get("hostOsType")
        job_id = dictionary.get('jobId')
        job_name = dictionary.get('jobName')
        last_n_days = dictionary.get('lastNDays')
        object_ids = dictionary.get("objectIds")
        object_type = dictionary.get('objectType')
        registered_source_id = dictionary.get('registeredSourceId')
        registered_source_ids = dictionary.get("registeredSourceIds")
        rollup = dictionary.get('rollup')
        run_status = dictionary.get("runStatus")
        sid = dictionary.get('sid')
        tenant_id_vec = dictionary.get("tenantIdVec")
        timezone = dictionary.get('timezone')
        unix_uid = dictionary.get('unixUid')
        vault_ids = dictionary.get("vaultIds")
        view_box_id = dictionary.get('viewBoxId')
        view_name = dictionary.get('viewName')
        viewbox_ids = dictionary.get("viewboxIds")
        vm_name = dictionary.get('vmName')

        # Return an object of this model
        return cls(
            all_under_hierarchy,
            compact_version,
            consecutive_failures,
            environment,
            exclude_users_within_alert_threshold,
            group_by,
            health_status,
            host_os_type,
            job_id,
            job_name,
            last_n_days,
            object_ids,
            object_type,
            registered_source_id,
            registered_source_ids,
            rollup,
            run_status,
            sid,
            tenant_id_vec,
            timezone,
            unix_uid,
            vault_ids,
            view_box_id,
            view_name,
            viewbox_ids,
            vm_name
)