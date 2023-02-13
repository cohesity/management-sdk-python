# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class LastProtectionRunSummary(object):

    """Implementation of the 'LastProtectionRunSummary' model.

    LastProtectionRunsSummary is the summary of the last Protection Run for
    the
    Protection Jobs using the Specified Protection Policy.

    Attributes:
        number_of_cancelled_protection_runs (long|int): Specifies the number
            of cancelled Protection Runs the given Protection Policy has in
            the Last Run.
        number_of_failed_protection_runs (long|int): Specifies the number of
            failed Protection Runs the given Protection Policy has in the Last
            Run.
        number_of_protected_sources (long|int): Specifies the number of
            Protection Sources protected by the given Protection Policy.
        number_of_running_protection_runs (long|int): Specifies the number of
            running Protection Runs using the current Protection Policy.
        number_of_sla_violations (long|int): Specifies the number of SLA
            violations the given Protection Policy has in the Last Run..
        number_of_successful_protection_runs (long|int): Specifies the number
            of successful Protection Runs the given Protection Policy has in
            the Last Run.
        total_logical_backup_size_in_bytes (long|int): Specifies the
            aggregated total logical backup performed in all the Latest
            Protection Runs made for all the Protection Jobs which have the
            given Protection Policy Specified.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "number_of_cancelled_protection_runs":'numberOfCancelledProtectionRuns',
        "number_of_failed_protection_runs":'numberOfFailedProtectionRuns',
        "number_of_protected_sources":'numberOfProtectedSources',
        "number_of_running_protection_runs":'numberOfRunningProtectionRuns',
        "number_of_sla_violations":'numberOfSlaViolations',
        "number_of_successful_protection_runs":'numberOfSuccessfulProtectionRuns',
        "total_logical_backup_size_in_bytes":'totalLogicalBackupSizeInBytes'
    }

    def __init__(self,
                 number_of_cancelled_protection_runs=None,
                 number_of_failed_protection_runs=None,
                 number_of_protected_sources=None,
                 number_of_running_protection_runs=None,
                 number_of_sla_violations=None,
                 number_of_successful_protection_runs=None,
                 total_logical_backup_size_in_bytes=None):
        """Constructor for the LastProtectionRunSummary class"""

        # Initialize members of the class
        self.number_of_cancelled_protection_runs = number_of_cancelled_protection_runs
        self.number_of_failed_protection_runs = number_of_failed_protection_runs
        self.number_of_protected_sources = number_of_protected_sources
        self.number_of_running_protection_runs = number_of_running_protection_runs
        self.number_of_sla_violations = number_of_sla_violations
        self.number_of_successful_protection_runs = number_of_successful_protection_runs
        self.total_logical_backup_size_in_bytes = total_logical_backup_size_in_bytes


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
        number_of_cancelled_protection_runs = dictionary.get('numberOfCancelledProtectionRuns')
        number_of_failed_protection_runs = dictionary.get('numberOfFailedProtectionRuns')
        number_of_protected_sources = dictionary.get('numberOfProtectedSources')
        number_of_running_protection_runs = dictionary.get('numberOfRunningProtectionRuns')
        number_of_sla_violations = dictionary.get('numberOfSlaViolations')
        number_of_successful_protection_runs = dictionary.get('numberOfSuccessfulProtectionRuns')
        total_logical_backup_size_in_bytes = dictionary.get('totalLogicalBackupSizeInBytes')

        # Return an object of this model
        return cls(number_of_cancelled_protection_runs,
                   number_of_failed_protection_runs,
                   number_of_protected_sources,
                   number_of_running_protection_runs,
                   number_of_sla_violations,
                   number_of_successful_protection_runs,
                   total_logical_backup_size_in_bytes)


