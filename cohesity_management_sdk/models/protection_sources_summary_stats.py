# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.protection_source
import cohesity_management_sdk.models.tenant_info

class ProtectionSourcesSummaryStats(object):

    """Implementation of the 'ProtectionSourcesSummaryStats' model.

    Specifies Job Run (Snapshot) summary statistics about the specified
    leaf Protection Source Object (such as a VM).

    Attributes:
        first_failed_run_time_usecs (int|long): Specifies the start time of
            the first failed Job Run protecting this Protection Source Object.
            The time is specified as a Unix epoch Timestamp (in microseconds).
        first_successful_run_time_usecs (long|int): Specifies the start time
            of the first successful Job Run protecting this Protection Source
            Object.
            The time is specified as a Unix epoch Timestamp (in microseconds).
        job_name (string): Specifies the job name.
        last_failed_run_time_usecs (int|long): Specifies the start time of the
            last failed Job Run protecting this Protection Source Object.
            The time is specified as a Unix epoch Timestamp (in microseconds).
        last_run_end_time_usecs (long|int): Specifies the end time of the last
            Job Run protecting this Protection Source Object.
            The time is specified as a Unix epoch Timestamp (in microseconds).
        last_run_error_msg (string): Specifies the error message associated
            with last run, if the last run has failed.
        last_run_start_time_usecs (long|int): Specifies the start time of the
            last Run of this object's snapshot.
            The time is specified in Unix epoch Timestamp (in microseconds).
        last_run_status (RunStatusEnum): Specifies the Job Run status of the
            last Job Run protecting this Protection Source Object.
            'kSuccess' indicates that the Job Run was successful.
            'kRunning' indicates that the Job Run is currently running.
            'kWarning' indicates that the Job Run was successful but warnings
            were issued.
            'kCancelled' indicates that the Job Run was canceled.
            'kError' indicates the Job Run encountered an error and did not
            run to completion.
        last_run_type (RunTypeEnum): Specifies the status of the Job Run.
            'kRegular' indicates an incremental (CBT) backup. Incremental
            backups utilizing CBT (if supported) are captured of the target
            protection objects.
            The first run of a kRegular schedule captures all the blocks.
            'kFull' indicates a full (no CBT) backup. A complete backup
            (all blocks) of the target protection objects are always captured
            and Change Block Tracking (CBT) is not utilized.
            'kLog' indicates a Database Log backup. Capture the database
            transaction logs to allow rolling back to a specific point in
            time.
            'kSystem' indicates system volume backup. It produces an image
            for bare metal recovery.
        last_successful_run_time_usecs (int|long): Specifies the start time of
            the last successful Job Run protecting this Protection Source
            Object.
            The time is specified as a Unix epoch Timestamp (in microseconds).
        num_data_read_bytes (long|int): Specifies the total number of bytes
            read while protecting this Protection Source Object.
        num_errors (int): Specifies the total number of errors reported during
            Job Runs of this Protection Source Object.
        num_logical_bytes_protected (int|long): Specifies the total logical
            bytes protected for this Protection Source Object.
            The logical size is when the data is fully hydrated or expanded.
        num_snapshots (int): Specifies the total number of Snapshots that are
            backing up this Protection Source Object.
        num_success_runs (int): Specifies the total number of successful Job
            Runs protecting this Protection Source Object.
        num_warnings (int): Specifies the total number of warnings reported
            during Job Runs of this Protection Source Object.
        protection_source (ProtectionSource): Specifies the leaf Protection
            Source Object (such as VM). Snapshot summary statistics are
            reported for this Protection Source Object
        registered_source (string): Specifies the name of the Registered
            Source that is the top level parent of the specified Protection
            Source Object.
        tenants (list of TenantInfo): Specifies basic information about
            tenants having access to the protection job.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "first_failed_run_time_usecs":'firstFailedRunTimeUsecs',
        "first_successful_run_time_usecs":'firstSuccessfulRunTimeUsecs',
        "job_name":'jobName',
        "last_failed_run_time_usecs":'lastFailedRunTimeUsecs',
        "last_run_end_time_usecs":'lastRunEndTimeUsecs',
        "last_run_error_msg":'lastRunErrorMsg',
        "last_run_start_time_usecs":'lastRunStartTimeUsecs',
        "last_run_status":'lastRunStatus',
        "last_run_type":'lastRunType',
        "last_successful_run_time_usecs":'lastSuccessfulRunTimeUsecs',
        "num_data_read_bytes":'numDataReadBytes',
        "num_errors":'numErrors',
        "num_logical_bytes_protected":'numLogicalBytesProtected',
        "num_snapshots":'numSnapshots',
        "num_success_runs":'numSuccessRuns',
        "num_warnings":'numWarnings',
        "protection_source":'protectionSource',
        "registered_source":'registeredSource',
        "tenants":'tenants'
    }

    def __init__(self,
                 first_failed_run_time_usecs=None,
                 first_successful_run_time_usecs=None,
                 job_name=None,
                 last_failed_run_time_usecs=None,
                 last_run_end_time_usecs=None,
                 last_run_error_msg=None,
                 last_run_start_time_usecs=None,
                 last_run_status=None,
                 last_run_type=None,
                 last_successful_run_time_usecs=None,
                 num_data_read_bytes=None,
                 num_errors=None,
                 num_logical_bytes_protected=None,
                 num_snapshots=None,
                 num_success_runs=None,
                 num_warnings=None,
                 protection_source=None,
                 registered_source=None,
                 tenants=None):
        """Constructor for the ProtectionSourcesSummaryStats class"""

        # Initialize members of the class
        self.first_failed_run_time_usecs = first_failed_run_time_usecs
        self.first_successful_run_time_usecs = first_successful_run_time_usecs
        self.job_name = job_name
        self.last_failed_run_time_usecs = last_failed_run_time_usecs
        self.last_run_end_time_usecs = last_run_end_time_usecs
        self.last_run_error_msg = last_run_error_msg
        self.last_run_start_time_usecs = last_run_start_time_usecs
        self.last_run_status = last_run_status
        self.last_run_type = last_run_type
        self.last_successful_run_time_usecs = last_successful_run_time_usecs
        self.num_data_read_bytes = num_data_read_bytes
        self.num_errors = num_errors
        self.num_logical_bytes_protected = num_logical_bytes_protected
        self.num_snapshots = num_snapshots
        self.num_success_runs = num_success_runs
        self.num_warnings = num_warnings
        self.protection_source = protection_source
        self.registered_source = registered_source
        self.tenants = tenants


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
        first_failed_run_time_usecs = dictionary.get('firstFailedRunTimeUsecs')
        first_successful_run_time_usecs = dictionary.get('firstSuccessfulRunTimeUsecs')
        job_name = dictionary.get('jobName')
        last_failed_run_time_usecs = dictionary.get('lastFailedRunTimeUsecs')
        last_run_end_time_usecs = dictionary.get('lastRunEndTimeUsecs')
        last_run_error_msg = dictionary.get('lastRunErrorMsg')
        last_run_start_time_usecs = dictionary.get('lastRunStartTimeUsecs')
        last_run_status = dictionary.get('lastRunStatus')
        last_run_type = dictionary.get('lastRunType')
        last_successful_run_time_usecs = dictionary.get('lastSuccessfulRunTimeUsecs')
        num_data_read_bytes = dictionary.get('numDataReadBytes')
        num_errors = dictionary.get('numErrors')
        num_logical_bytes_protected = dictionary.get('numLogicalBytesProtected')
        num_snapshots = dictionary.get('numSnapshots')
        num_success_runs = dictionary.get('numSuccessRuns')
        num_warnings = dictionary.get('numWarnings')
        protection_source = cohesity_management_sdk.models.protection_source.ProtectionSource.from_dictionary(dictionary.get('protectionSource')) if dictionary.get('protectionSource') else None
        registered_source = dictionary.get('registeredSource')
        tenants = None
        if dictionary.get('tenants') != None:
            tenants = list()
            for structure in dictionary.get('tenants'):
                tenants.append(cohesity_management_sdk.models.tenant_info.TenantInfo.from_dictionary(structure))

        # Return an object of this model
        return cls(first_failed_run_time_usecs,
                   first_successful_run_time_usecs,
                   job_name,
                   last_failed_run_time_usecs,
                   last_run_end_time_usecs,
                   last_run_error_msg,
                   last_run_start_time_usecs,
                   last_run_status,
                   last_run_type,
                   last_successful_run_time_usecs,
                   num_data_read_bytes,
                   num_errors,
                   num_logical_bytes_protected,
                   num_snapshots,
                   num_success_runs,
                   num_warnings,
                   protection_source,
                   registered_source,
                   tenants)



