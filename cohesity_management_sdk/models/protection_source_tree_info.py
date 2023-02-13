# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.application_info
import cohesity_management_sdk.models.entity_permission_information
import cohesity_management_sdk.models.registered_source_info
import cohesity_management_sdk.models.protection_source
import cohesity_management_sdk.models.protection_summary
import cohesity_management_sdk.models.protection_summary_by_env

class ProtectionSourceTreeInfo(object):

    """Implementation of the 'ProtectionSourceTreeInfo' model.

    Specifies the registration and protection information of a registered
    Protection Source Tree on the Cohesity Cluster.
    Many different Protection Source trees are supported such as
    'kVMware', 'kAcropolis', 'kPhysical' etc.,

    Attributes:
        applications (list of ApplicationInfo): Array of applications
            hierarchy registered on this node.  Specifies the application type
            and the list of instances of the application objects. For example
            for SQL Server, this list provides the SQL Server instances
            running on a VM or a Physical Server.
        entity_permission_info (EntityPermissionInformation): Specifies the
            permission information of entities.
        logical_size_bytes (long|int): Specifies the logical size of the
            Protection Source in bytes.
        registration_info (RegisteredSourceInfo): Specifies registration
            information for a root node in a Protection Sources tree. A root
            node represents a registered Source on the Cohesity Cluster, such
            as a vCenter Server.
        root_node (ProtectionSource): Specifies the Protection Source for the
            root node of the Protection Source tree.
        stats (ProtectionSummary): Specifies the stats of protection for a
            Protection Source Tree.
        stats_by_env (list of ProtectionSummaryByEnv): Specifies the breakdown
            of the stats of protection by environment. overrideDescription:
            true
        total_downtiered_size_in_bytes (long|int): Specifies the total bytes
            downtiered from the source so far.
        total_uptiered_size_in_bytes (long|int): Specifies the total bytes
            uptiered to the source so far.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "applications":'applications',
        "entity_permission_info":'entityPermissionInfo',
        "logical_size_bytes":'logicalSizeBytes',
        "registration_info":'registrationInfo',
        "root_node":'rootNode',
        "stats":'stats',
        "stats_by_env":'statsByEnv',
        "total_downtiered_size_in_bytes":'totalDowntieredSizeInBytes',
        "total_uptiered_size_in_bytes":'totalUptieredSizeInBytes'
    }

    def __init__(self,
                 applications=None,
                 entity_permission_info=None,
                 logical_size_bytes=None,
                 registration_info=None,
                 root_node=None,
                 stats=None,
                 stats_by_env=None,
                 total_downtiered_size_in_bytes=None,
                 total_uptiered_size_in_bytes=None):
        """Constructor for the ProtectionSourceTreeInfo class"""

        # Initialize members of the class
        self.applications = applications
        self.entity_permission_info = entity_permission_info
        self.logical_size_bytes = logical_size_bytes
        self.registration_info = registration_info
        self.root_node = root_node
        self.stats = stats
        self.stats_by_env = stats_by_env
        self.total_downtiered_size_in_bytes = total_downtiered_size_in_bytes
        self.total_uptiered_size_in_bytes = total_uptiered_size_in_bytes


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
        applications = None
        if dictionary.get('applications') != None:
            applications = list()
            for structure in dictionary.get('applications'):
                applications.append(cohesity_management_sdk.models.application_info.ApplicationInfo.from_dictionary(structure))
        entity_permission_info = cohesity_management_sdk.models.entity_permission_information.EntityPermissionInformation.from_dictionary(dictionary.get('entityPermissionInfo')) if dictionary.get('entityPermissionInfo') else None
        logical_size_bytes = dictionary.get('logicalSizeBytes')
        registration_info = cohesity_management_sdk.models.registered_source_info.RegisteredSourceInfo.from_dictionary(dictionary.get('registrationInfo')) if dictionary.get('registrationInfo') else None
        root_node = cohesity_management_sdk.models.protection_source.ProtectionSource.from_dictionary(dictionary.get('rootNode')) if dictionary.get('rootNode') else None
        stats = cohesity_management_sdk.models.protection_summary.ProtectionSummary.from_dictionary(dictionary.get('stats')) if dictionary.get('stats') else None
        stats_by_env = None
        if dictionary.get('statsByEnv') != None:
            stats_by_env = list()
            for structure in dictionary.get('statsByEnv'):
                stats_by_env.append(cohesity_management_sdk.models.protection_summary_by_env.ProtectionSummaryByEnv.from_dictionary(structure))
        total_downtiered_size_in_bytes = dictionary.get('totalDowntieredSizeInBytes')
        total_uptiered_size_in_bytes = dictionary.get('totalUptieredSizeInBytes')

        # Return an object of this model
        return cls(applications,
                   entity_permission_info,
                   logical_size_bytes,
                   registration_info,
                   root_node,
                   stats,
                   stats_by_env,
                   total_downtiered_size_in_bytes,
                   total_uptiered_size_in_bytes)


