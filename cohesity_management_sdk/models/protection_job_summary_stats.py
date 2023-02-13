# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ProtectionJobSummaryStats(object):

    """Implementation of the 'ProtectionJobSummaryStats' model.

    Specifies statistics about a Protection Job.

    Attributes:
        average_run_time_usecs (long|int): Specifies the average run time of
            all successful Protection Runs. It is specified as a Unix epoch
            Timestamp (in microseconds).
        fastest_run_time_usecs (long|int): Specifies the time taken for a
            fastest successful Protection Run so far. It is specified as a
            Unix epoch Timestamp (in microseconds).
        num_canceled_runs (long|int): Specifies the number of runs that were
            cancelled.
        num_failed_runs (long|int): Specifies the number of runs that failed
            to finish.
        num_sla_violations (long|int): Specifies the number of runs having SLA
            violations.
        num_successful_runs (long|int): Specifies the number of runs that
            finished successfully.
        slowest_run_time_usecs (long|int): Specifies the time taken for a
            slowest successful Protection Run so far. It is specified as a
            Unix epoch Timestamp (in microseconds).
        total_bytes_read_from_source (long|int): Specifies the total amount of
            data read from the source (so far).
        total_logical_backup_size_bytes (long|int): Specifies the size of the
            source object (such as a VM) protected by this task on the primary
            storage after the snapshot is taken. The logical size of the data
            on the source if the data is fully hydrated or expanded and not
            reduced by change-block tracking, compression and deduplication.
        total_physical_backup_size_bytes (long|int): Specifies the total
            amount of physical space used on the Cohesity Cluster to store the
            protected object after being reduced by change-block tracking,
            compression and deduplication. For example, if the logical backup
            size is 1GB, but only 1MB was used on the Cohesity Cluster to
            store it, this field be equal to 1MB.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "average_run_time_usecs":'averageRunTimeUsecs',
        "fastest_run_time_usecs":'fastestRunTimeUsecs',
        "num_canceled_runs":'numCanceledRuns',
        "num_failed_runs":'numFailedRuns',
        "num_sla_violations":'numSlaViolations',
        "num_successful_runs":'numSuccessfulRuns',
        "slowest_run_time_usecs":'slowestRunTimeUsecs',
        "total_bytes_read_from_source":'totalBytesReadFromSource',
        "total_logical_backup_size_bytes":'totalLogicalBackupSizeBytes',
        "total_physical_backup_size_bytes":'totalPhysicalBackupSizeBytes'
    }

    def __init__(self,
                 average_run_time_usecs=None,
                 fastest_run_time_usecs=None,
                 num_canceled_runs=None,
                 num_failed_runs=None,
                 num_sla_violations=None,
                 num_successful_runs=None,
                 slowest_run_time_usecs=None,
                 total_bytes_read_from_source=None,
                 total_logical_backup_size_bytes=None,
                 total_physical_backup_size_bytes=None):
        """Constructor for the ProtectionJobSummaryStats class"""

        # Initialize members of the class
        self.average_run_time_usecs = average_run_time_usecs
        self.fastest_run_time_usecs = fastest_run_time_usecs
        self.num_canceled_runs = num_canceled_runs
        self.num_failed_runs = num_failed_runs
        self.num_sla_violations = num_sla_violations
        self.num_successful_runs = num_successful_runs
        self.slowest_run_time_usecs = slowest_run_time_usecs
        self.total_bytes_read_from_source = total_bytes_read_from_source
        self.total_logical_backup_size_bytes = total_logical_backup_size_bytes
        self.total_physical_backup_size_bytes = total_physical_backup_size_bytes


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
        average_run_time_usecs = dictionary.get('averageRunTimeUsecs')
        fastest_run_time_usecs = dictionary.get('fastestRunTimeUsecs')
        num_canceled_runs = dictionary.get('numCanceledRuns')
        num_failed_runs = dictionary.get('numFailedRuns')
        num_sla_violations = dictionary.get('numSlaViolations')
        num_successful_runs = dictionary.get('numSuccessfulRuns')
        slowest_run_time_usecs = dictionary.get('slowestRunTimeUsecs')
        total_bytes_read_from_source = dictionary.get('totalBytesReadFromSource')
        total_logical_backup_size_bytes = dictionary.get('totalLogicalBackupSizeBytes')
        total_physical_backup_size_bytes = dictionary.get('totalPhysicalBackupSizeBytes')

        # Return an object of this model
        return cls(average_run_time_usecs,
                   fastest_run_time_usecs,
                   num_canceled_runs,
                   num_failed_runs,
                   num_sla_violations,
                   num_successful_runs,
                   slowest_run_time_usecs,
                   total_bytes_read_from_source,
                   total_logical_backup_size_bytes,
                   total_physical_backup_size_bytes)


