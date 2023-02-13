# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.last_protection_run_summary
import cohesity_management_sdk.models.protected_source_summary
import cohesity_management_sdk.models.protection_job_summary_for_policies
import cohesity_management_sdk.models.protection_policy
import cohesity_management_sdk.models.protection_runs_summary

class ProtectionPolicySummary(object):

    """Implementation of the 'ProtectionPolicySummary' model.

    ProtectionPolicySummary specifies protection summary of a given
    Protection Policy.

    Attributes:
        last_protection_run_summary (LastProtectionRunSummary):
            LastProtectionRunsSummary is the summary of the last Protection
            Run for the Protection Jobs using the Specified Protection
            Policy.
        pagination_cookie (string): If there are more results to display, use
            this value to get the next set of results, by using this value in
            paginationCookie param for the next request to
            GetProtectionPolicySummary.
        protected_sources_summary (list of ProtectedSourceSummary): Specifies
            the list of Protection Sources which are protected under the given
            policy. This is only populated if the policy is of type kRPO.
        protection_jobs_summary (list of ProtectionJobSummaryForPolicies):
            Specifies the list of Protection Jobs associated with the given
            Protection Policy. This is only populated if the type of the
            Protection Policy is kRegular.
        protection_policy (ProtectionPolicy): TODO: type description here.
        protection_runs_summary (ProtectionRunsSummary): ProtectionRunsSummary
            is the summary of the all the Protection Runs for the Protection
            Jobs using the Specified Protection Policy.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "last_protection_run_summary":'lastProtectionRunSummary',
        "pagination_cookie":'paginationCookie',
        "protected_sources_summary":'protectedSourcesSummary',
        "protection_jobs_summary":'protectionJobsSummary',
        "protection_policy":'protectionPolicy',
        "protection_runs_summary":'protectionRunsSummary'
    }

    def __init__(self,
                 last_protection_run_summary=None,
                 pagination_cookie=None,
                 protected_sources_summary=None,
                 protection_jobs_summary=None,
                 protection_policy=None,
                 protection_runs_summary=None):
        """Constructor for the ProtectionPolicySummary class"""

        # Initialize members of the class
        self.last_protection_run_summary = last_protection_run_summary
        self.pagination_cookie = pagination_cookie
        self.protected_sources_summary = protected_sources_summary
        self.protection_jobs_summary = protection_jobs_summary
        self.protection_policy = protection_policy
        self.protection_runs_summary = protection_runs_summary


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
        last_protection_run_summary = cohesity_management_sdk.models.last_protection_run_summary.LastProtectionRunSummary.from_dictionary(dictionary.get('lastProtectionRunSummary')) if dictionary.get('lastProtectionRunSummary') else None
        pagination_cookie = dictionary.get('paginationCookie')
        protected_sources_summary = None
        if dictionary.get('protectedSourcesSummary') != None:
            protected_sources_summary = list()
            for structure in dictionary.get('protectedSourcesSummary'):
                protected_sources_summary.append(cohesity_management_sdk.models.protected_source_summary.ProtectedSourceSummary.from_dictionary(structure))
        protection_jobs_summary = None
        if dictionary.get('protectionJobsSummary') != None:
            protection_jobs_summary = list()
            for structure in dictionary.get('protectionJobsSummary'):
                protection_jobs_summary.append(cohesity_management_sdk.models.protection_job_summary_for_policies.ProtectionJobSummaryForPolicies.from_dictionary(structure))
        protection_policy = cohesity_management_sdk.models.protection_policy.ProtectionPolicy.from_dictionary(dictionary.get('protectionPolicy')) if dictionary.get('protectionPolicy') else None
        protection_runs_summary = cohesity_management_sdk.models.protection_runs_summary.ProtectionRunsSummary.from_dictionary(dictionary.get('protectionRunsSummary')) if dictionary.get('protectionRunsSummary') else None

        # Return an object of this model
        return cls(last_protection_run_summary,
                   pagination_cookie,
                   protected_sources_summary,
                   protection_jobs_summary,
                   protection_policy,
                   protection_runs_summary)


