# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.vault_run_info

class VaultRunStatsSummary(object):

    """Implementation of the 'VaultRunStatsSummary' model.

    Specifies the stats by run type for each vault run.

    Attributes:
        failure_time_series (list of VaultRunInfo): Specifies the time series
            for the failed runs that ended in the given time frame.
        num_failed_runs (long|int): Specifies the number of runs that ended in
            failure during the given time frame.
        num_in_progress_runs (long|int): Specifies the number of runs that
            were currently in progress at the time that the API call was
            made.
        num_queued_runs (long|int): Specifies the number of runs that were
            currently queued at the time that the API call was made.
        num_successful_runs (long|int): Specifies the number of runs that
            ended in success during the given time frame.
        success_time_series (list of VaultRunInfo): Specifies the time series
            for the successful runs that ended in the given time frame.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "failure_time_series":'failureTimeSeries',
        "num_failed_runs":'numFailedRuns',
        "num_in_progress_runs":'numInProgressRuns',
        "num_queued_runs":'numQueuedRuns',
        "num_successful_runs":'numSuccessfulRuns',
        "success_time_series":'successTimeSeries'
    }

    def __init__(self,
                 failure_time_series=None,
                 num_failed_runs=None,
                 num_in_progress_runs=None,
                 num_queued_runs=None,
                 num_successful_runs=None,
                 success_time_series=None):
        """Constructor for the VaultRunStatsSummary class"""

        # Initialize members of the class
        self.failure_time_series = failure_time_series
        self.num_failed_runs = num_failed_runs
        self.num_in_progress_runs = num_in_progress_runs
        self.num_queued_runs = num_queued_runs
        self.num_successful_runs = num_successful_runs
        self.success_time_series = success_time_series


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
        failure_time_series = None
        if dictionary.get('failureTimeSeries') != None:
            failure_time_series = list()
            for structure in dictionary.get('failureTimeSeries'):
                failure_time_series.append(cohesity_management_sdk.models.vault_run_info.VaultRunInfo.from_dictionary(structure))
        num_failed_runs = dictionary.get('numFailedRuns')
        num_in_progress_runs = dictionary.get('numInProgressRuns')
        num_queued_runs = dictionary.get('numQueuedRuns')
        num_successful_runs = dictionary.get('numSuccessfulRuns')
        success_time_series = None
        if dictionary.get('successTimeSeries') != None:
            success_time_series = list()
            for structure in dictionary.get('successTimeSeries'):
                success_time_series.append(cohesity_management_sdk.models.vault_run_info.VaultRunInfo.from_dictionary(structure))

        # Return an object of this model
        return cls(failure_time_series,
                   num_failed_runs,
                   num_in_progress_runs,
                   num_queued_runs,
                   num_successful_runs,
                   success_time_series)


