# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.protection_source_tree_info
import cohesity_management_sdk.models.protection_summary
import cohesity_management_sdk.models.protection_summary_by_env

class GetRegistrationInfoResponse(object):

    """Implementation of the 'GetRegistrationInfoResponse' model.

    Specifies the registration, protection and permission information of all
    or a
    subset of the registered Protection Source Trees or Views on the Cohesity
    Cluster.

    Attributes:
        root_nodes (list of ProtectionSourceTreeInfo): Specifies the
            registration, protection and permission information of either all
            or a subset of registered Protection Sources matching the filter
            parameters. overrideDescription: true
        stats (ProtectionSummary): Specifies the sum of all the stats of
            protection of Protection Sources and views selected by the query
            parameters.
        stats_by_env (list of ProtectionSummaryByEnv): Specifies the breakdown
            of the stats by environment overrideDescription: true

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "root_nodes":'rootNodes',
        "stats":'stats',
        "stats_by_env":'statsByEnv'
    }

    def __init__(self,
                 root_nodes=None,
                 stats=None,
                 stats_by_env=None):
        """Constructor for the GetRegistrationInfoResponse class"""

        # Initialize members of the class
        self.root_nodes = root_nodes
        self.stats = stats
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
        root_nodes = None
        if dictionary.get('rootNodes') != None:
            root_nodes = list()
            for structure in dictionary.get('rootNodes'):
                root_nodes.append(cohesity_management_sdk.models.protection_source_tree_info.ProtectionSourceTreeInfo.from_dictionary(structure))
        stats = cohesity_management_sdk.models.protection_summary.ProtectionSummary.from_dictionary(dictionary.get('stats')) if dictionary.get('stats') else None
        stats_by_env = None
        if dictionary.get('statsByEnv') != None:
            stats_by_env = list()
            for structure in dictionary.get('statsByEnv'):
                stats_by_env.append(cohesity_management_sdk.models.protection_summary_by_env.ProtectionSummaryByEnv.from_dictionary(structure))

        # Return an object of this model
        return cls(root_nodes,
                   stats,
                   stats_by_env)


