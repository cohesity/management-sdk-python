# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.last_protection_run_stats_by_env

class LastProtectionRunStats(object):

    """Implementation of the 'LastProtectionRunStats' model.

    Specifies the stats of last Protection Run.

    Attributes:
        num_objects_cancelled (long|int): Specifies the number of objects
            that were cancelled in the last Run across all Protection Jobs.
        num_objects_failed (long|int): Specifies the number of objects that
            were failed in the last Run across all Protection Jobs.
        num_objects_in_progress (long|int): Specifies the number of objects
            that are still in progress in the last Run across all Protection
            Jobs.
        num_objects_successful (long|int): Specifies the number of objects
            that were successful in the last Run across all Protection Jobs.
        num_runs_failed (long|int): Specifies the number of Protection Jobs
            for which specified Protection Run failed.
        num_runs_failed_sla (long|int): Specifies the number of Protection
            Jobs for which specified Protection Run failed SLA.
        num_runs_met_sla (long|int): Specifies the number of Protection Jobs
            for which specified Protection Run met SLA.
        stats_by_env (list of LastProtectionRunStatsByEnv): Specifies the last
            Protection Run stats by environment.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "num_objects_cancelled":'numObjectsCancelled',
        "num_objects_failed":'numObjectsFailed',
        "num_objects_in_progress":'numObjectsInProgress',
        "num_objects_successful":'numObjectsSuccessful',
        "num_runs_failed":'numRunsFailed',
        "num_runs_failed_sla":'numRunsFailedSla',
        "num_runs_met_sla":'numRunsMetSla',
        "stats_by_env":'statsByEnv'
    }

    def __init__(self,
                 num_objects_cancelled=None,
                 num_objects_failed=None,
                 num_objects_in_progress=None,
                 num_objects_successful=None,
                 num_runs_failed=None,
                 num_runs_failed_sla=None,
                 num_runs_met_sla=None,
                 stats_by_env=None):
        """Constructor for the LastProtectionRunStats class"""

        # Initialize members of the class
        self.num_objects_cancelled = num_objects_cancelled
        self.num_objects_failed = num_objects_failed
        self.num_objects_in_progress = num_objects_in_progress
        self.num_objects_successful = num_objects_successful
        self.num_runs_failed = num_runs_failed
        self.num_runs_failed_sla = num_runs_failed_sla
        self.num_runs_met_sla = num_runs_met_sla
        self.stats_by_env = stats_by_env


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
        num_objects_cancelled = dictionary.get('numObjectsCancelled')
        num_objects_failed = dictionary.get('numObjectsFailed')
        num_runs_failed = dictionary.get('numRunsFailed')
        num_objects_successful = dictionary.get('numObjectsSuccessful')
        num_objects_in_progress = dictionary.get('numObjectsInProgress')
        num_runs_failed_sla = dictionary.get('numRunsFailedSla')
        num_runs_met_sla = dictionary.get('numRunsMetSla')
        stats_by_env = None
        if dictionary.get('statsByEnv') != None:
            stats_by_env = list()
            for structure in dictionary.get('statsByEnv'):
                stats_by_env.append(cohesity_management_sdk.models.last_protection_run_stats_by_env.LastProtectionRunStatsByEnv.from_dictionary(structure))

        # Return an object of this model
        return cls(num_objects_cancelled,
                   num_objects_failed,
                   num_objects_in_progress,
                   num_objects_successful,
                   num_runs_failed,
                   num_runs_failed_sla,
                   num_runs_met_sla,
                   stats_by_env)


