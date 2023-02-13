# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.protection_job
import cohesity_management_sdk.models.protection_policy
import cohesity_management_sdk.models.protection_source
import cohesity_management_sdk.models.protection_summary

class ProtectedVmInfo(object):

    """Implementation of the 'ProtectedVmInfo' model.

    Specifies the Protection Jobs information of a VM.

    Attributes:
        protection_jobs (list of ProtectionJob): Specifies the list of
            Protection Jobs that protect the VM.
        protection_policies (list of ProtectionPolicy): Specifies the list of
            Policies that are used by the Protection Jobs.
        protection_source (ProtectionSource): Specifies a generic structure
            that represents a node in the Protection Source tree. Node details
            will depend on the environment of the Protection Source.
        stats (ProtectionSummary): Specifies the protection stats of VM.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "protection_jobs":'protectionJobs',
        "protection_policies":'protectionPolicies',
        "protection_source":'protectionSource',
        "stats":'stats'
    }

    def __init__(self,
                 protection_jobs=None,
                 protection_policies=None,
                 protection_source=None,
                 stats=None):
        """Constructor for the ProtectedVmInfo class"""

        # Initialize members of the class
        self.protection_jobs = protection_jobs
        self.protection_policies = protection_policies
        self.protection_source = protection_source
        self.stats = stats


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
        protection_jobs = None
        if dictionary.get('protectionJobs') != None:
            protection_jobs = list()
            for structure in dictionary.get('protectionJobs'):
                protection_jobs.append(cohesity_management_sdk.models.protection_job.ProtectionJob.from_dictionary(structure))
        protection_policies = None
        if dictionary.get('protectionPolicies') != None:
            protection_policies = list()
            for structure in dictionary.get('protectionPolicies'):
                protection_policies.append(cohesity_management_sdk.models.protection_policy.ProtectionPolicy.from_dictionary(structure))
        protection_source = cohesity_management_sdk.models.protection_source.ProtectionSource.from_dictionary(dictionary.get('protectionSource')) if dictionary.get('protectionSource') else None
        stats = cohesity_management_sdk.models.protection_summary.ProtectionSummary.from_dictionary(dictionary.get('stats')) if dictionary.get('stats') else None

        # Return an object of this model
        return cls(protection_jobs,
                   protection_policies,
                   protection_source,
                   stats)


