# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.protection_sources_summary_stats

class ProtectionSourcesJobsSummaryReportResponseWrapper(object):

    """Implementation of the 'ProtectionSourcesJobsSummaryReportResponseWrapper' model.


    Attributes:
        protection_sources_jobs_summary (list of
            ProtectionSourcesSummaryStats): Specifies the list of Snapshot
            summary statistics that match the filter criteria.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "protection_sources_jobs_summary":'protectionSourcesJobsSummary'
    }

    def __init__(self,
                 protection_sources_jobs_summary=None):
        """Constructor for the ProtectionSourcesJobsSummaryReportResponseWrapper class"""

        # Initialize members of the class
        self.protection_sources_jobs_summary = protection_sources_jobs_summary


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
        protection_sources_jobs_summary = None
        if dictionary.get('protectionSourcesJobsSummary') != None:
            protection_sources_jobs_summary = list()
            for structure in dictionary.get('protectionSourcesJobsSummary'):
                protection_sources_jobs_summary.append(cohesity_management_sdk.models.protection_sources_summary_stats.ProtectionSourcesSummaryStats.from_dictionary(structure))

        # Return an object of this model
        return cls(protection_sources_jobs_summary)


