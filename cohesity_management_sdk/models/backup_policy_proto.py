# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.backup_policy_proto_continuous_schedule
import cohesity_management_sdk.models.backup_policy_proto_daily_schedule
import cohesity_management_sdk.models.backup_policy_proto_monthly_schedule
import cohesity_management_sdk.models.backup_policy_proto_one_off_schedule
import cohesity_management_sdk.models.backup_policy_proto_schedule_end

class BackupPolicyProto(object):

    """Implementation of the 'BackupPolicyProto' model.

    If a backup does not get a chance to when it's due (either due to the
    system
    being busy or a conflict with another instance of the same job), the
    backup
    will still be run when the conflicts go away. But, if there are multiple
    instances of the same job that are due to be run, only the latest
    instance
    would be run.

    Attributes:
        continuous_schedule (BackupPolicyProtoContinuousSchedule): TODO: type
            description here.
        daily_schedule (BackupPolicyProtoDailySchedule): The daily schedule
            encompasses weekly schedules as well. This has been done so there
            is only one way of specifying a schedule (backing up daily is the
            same as backing up weekly, but on all days of the week).
        monthly_schedule (BackupPolicyProtoMonthlySchedule): TODO: type
            description here.
        name (string): A backup schedule can have an optional name.
        num_days_to_keep (long|int): Specifies how to determine the expiration
            time for snapshots created by a backup run. The snapshots will be
            marked as expiring (i.e., eligible to be garbage collected) in
            'num_days_to_keep' days from when the snapshots were created.
        num_retries (int): The number of retries to perform (for retryable
            errors) before giving up.
        one_off_schedule (BackupPolicyProtoOneOffSchedule): TODO: type
            description here.
        periodicity (int): Determines how often the job should be run.
        retry_delay_mins (int): The number of minutes to wait before retrying
            a failed job.
        schedule_end (BackupPolicyProtoScheduleEnd): TODO: type description
            here.
        start_window_interval_mins (int): This field determines the amount of
            time (in minutes) after which a scheduled job will not be started.
            For example, if a job is scheduled to be run every Sunday at 5am,
            and this field is set to 30 minutes, but the job was unable to
            start by 5:30am on a Sunday due to other conflicts (say too many
            other jobs were already running), Magneto will not attempt to
            start the job until the next scheduled time (on the following
            Sunday). If this field is not set, the interval will be determined
            by the Magneto flag
            --magneto_master_default_start_window_interval_mins.
        truncate_logs (bool): Whether to truncate logs after a backup run.
            This is currently only relevant for full or incremental backups in
            a SQL environment.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "continuous_schedule":'continuousSchedule',
        "daily_schedule":'dailySchedule',
        "monthly_schedule":'monthlySchedule',
        "name":'name',
        "num_days_to_keep":'numDaysToKeep',
        "num_retries":'numRetries',
        "one_off_schedule":'oneOffSchedule',
        "periodicity":'periodicity',
        "retry_delay_mins":'retryDelayMins',
        "schedule_end":'scheduleEnd',
        "start_window_interval_mins":'startWindowIntervalMins',
        "truncate_logs":'truncateLogs'
    }

    def __init__(self,
                 continuous_schedule=None,
                 daily_schedule=None,
                 monthly_schedule=None,
                 name=None,
                 num_days_to_keep=None,
                 num_retries=None,
                 one_off_schedule=None,
                 periodicity=None,
                 retry_delay_mins=None,
                 schedule_end=None,
                 start_window_interval_mins=None,
                 truncate_logs=None):
        """Constructor for the BackupPolicyProto class"""

        # Initialize members of the class
        self.continuous_schedule = continuous_schedule
        self.daily_schedule = daily_schedule
        self.monthly_schedule = monthly_schedule
        self.name = name
        self.num_days_to_keep = num_days_to_keep
        self.num_retries = num_retries
        self.one_off_schedule = one_off_schedule
        self.periodicity = periodicity
        self.retry_delay_mins = retry_delay_mins
        self.schedule_end = schedule_end
        self.start_window_interval_mins = start_window_interval_mins
        self.truncate_logs = truncate_logs


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
        continuous_schedule = cohesity_management_sdk.models.backup_policy_proto_continuous_schedule.BackupPolicyProtoContinuousSchedule.from_dictionary(dictionary.get('continuousSchedule')) if dictionary.get('continuousSchedule') else None
        daily_schedule = cohesity_management_sdk.models.backup_policy_proto_daily_schedule.BackupPolicyProtoDailySchedule.from_dictionary(dictionary.get('dailySchedule')) if dictionary.get('dailySchedule') else None
        monthly_schedule = cohesity_management_sdk.models.backup_policy_proto_monthly_schedule.BackupPolicyProtoMonthlySchedule.from_dictionary(dictionary.get('monthlySchedule')) if dictionary.get('monthlySchedule') else None
        name = dictionary.get('name')
        num_days_to_keep = dictionary.get('numDaysToKeep')
        num_retries = dictionary.get('numRetries')
        one_off_schedule = cohesity_management_sdk.models.backup_policy_proto_one_off_schedule.BackupPolicyProtoOneOffSchedule.from_dictionary(dictionary.get('oneOffSchedule')) if dictionary.get('oneOffSchedule') else None
        periodicity = dictionary.get('periodicity')
        retry_delay_mins = dictionary.get('retryDelayMins')
        schedule_end = cohesity_management_sdk.models.backup_policy_proto_schedule_end.BackupPolicyProtoScheduleEnd.from_dictionary(dictionary.get('scheduleEnd')) if dictionary.get('scheduleEnd') else None
        start_window_interval_mins = dictionary.get('startWindowIntervalMins')
        truncate_logs = dictionary.get('truncateLogs')

        # Return an object of this model
        return cls(continuous_schedule,
                   daily_schedule,
                   monthly_schedule,
                   name,
                   num_days_to_keep,
                   num_retries,
                   one_off_schedule,
                   periodicity,
                   retry_delay_mins,
                   schedule_end,
                   start_window_interval_mins,
                   truncate_logs)


