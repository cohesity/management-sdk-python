# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.protection_source
import cohesity_management_sdk.models.protection_run_instance
import cohesity_management_sdk.models.protection_policy

class ProtectionObjectSummary(object):

    """Implementation of the 'ProtectionObjectSummary' model.

    TODO: type model description here.

    Attributes:
        latest_archival_snapshot_time_usecs (long|int): Specifies the Unix
            epoch Timestamp (in microseconds) of the latest Archival
            Snapshot.
        latest_local_snapshot_time_usecs (long|int): Specifies the Unix epoch
            Timestamp (in microseconds) of the latest Local Snapshot.
        latest_replication_snapshot_time_usecs (long|int): Specifies the Unix
            epoch Timestamp (in microseconds) of the latest Replication
            Snapshot.
        parent_protection_source (ProtectionSource): Specifies a generic
            structure that represents a node in the Protection Source tree.
            Node details will depend on the environment of the Protection
            Source.
        protection_jobs (list of ProtectionRunInstance): Returns the list of
            Protection Jobs with summary Information.
        protection_source (ProtectionSource): Specifies the leaf Protection
            Source Object such as a VM.
        rpo_policies (list of ProtectionPolicy): Specifies the id of the RPO
            policy protecting this object.
        total_archival_snapshots (int): Specifies the total number of Archival
            Snapshots.
        total_local_snapshots (int): Specifies the total number of Local
            Snapshots.
        total_replication_snapshots (int): Specifies the total number of
            Replication Snapshots.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "latest_archival_snapshot_time_usecs":'latestArchivalSnapshotTimeUsecs',
        "latest_local_snapshot_time_usecs":'latestLocalSnapshotTimeUsecs',
        "latest_replication_snapshot_time_usecs":'latestReplicationSnapshotTimeUsecs',
        "parent_protection_source":'parentProtectionSource',
        "protection_jobs":'protectionJobs',
        "protection_source":'protectionSource',
        "rpo_policies":'rpoPolicies',
        "total_archival_snapshots":'totalArchivalSnapshots',
        "total_local_snapshots":'totalLocalSnapshots',
        "total_replication_snapshots":'totalReplicationSnapshots'
    }

    def __init__(self,
                 latest_archival_snapshot_time_usecs=None,
                 latest_local_snapshot_time_usecs=None,
                 latest_replication_snapshot_time_usecs=None,
                 parent_protection_source=None,
                 protection_jobs=None,
                 protection_source=None,
                 rpo_policies=None,
                 total_archival_snapshots=None,
                 total_local_snapshots=None,
                 total_replication_snapshots=None):
        """Constructor for the ProtectionObjectSummary class"""

        # Initialize members of the class
        self.latest_archival_snapshot_time_usecs = latest_archival_snapshot_time_usecs
        self.latest_local_snapshot_time_usecs = latest_local_snapshot_time_usecs
        self.latest_replication_snapshot_time_usecs = latest_replication_snapshot_time_usecs
        self.parent_protection_source = parent_protection_source
        self.protection_jobs = protection_jobs
        self.protection_source = protection_source
        self.rpo_policies = rpo_policies
        self.total_archival_snapshots = total_archival_snapshots
        self.total_local_snapshots = total_local_snapshots
        self.total_replication_snapshots = total_replication_snapshots


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
        latest_archival_snapshot_time_usecs = dictionary.get('latestArchivalSnapshotTimeUsecs')
        latest_local_snapshot_time_usecs = dictionary.get('latestLocalSnapshotTimeUsecs')
        latest_replication_snapshot_time_usecs = dictionary.get('latestReplicationSnapshotTimeUsecs')
        parent_protection_source = cohesity_management_sdk.models.protection_source.ProtectionSource.from_dictionary(dictionary.get('parentProtectionSource')) if dictionary.get('parentProtectionSource') else None
        protection_jobs = None
        if dictionary.get('protectionJobs') != None:
            protection_jobs = list()
            for structure in dictionary.get('protectionJobs'):
                protection_jobs.append(cohesity_management_sdk.models.protection_run_instance.ProtectionRunInstance.from_dictionary(structure))
        protection_source = cohesity_management_sdk.models.protection_source.ProtectionSource.from_dictionary(dictionary.get('protectionSource')) if dictionary.get('protectionSource') else None
        rpo_policies = None
        if dictionary.get('rpoPolicies') != None:
            rpo_policies = list()
            for structure in dictionary.get('rpoPolicies'):
                rpo_policies.append(cohesity_management_sdk.models.protection_policy.ProtectionPolicy.from_dictionary(structure))
        total_archival_snapshots = dictionary.get('totalArchivalSnapshots')
        total_local_snapshots = dictionary.get('totalLocalSnapshots')
        total_replication_snapshots = dictionary.get('totalReplicationSnapshots')

        # Return an object of this model
        return cls(latest_archival_snapshot_time_usecs,
                   latest_local_snapshot_time_usecs,
                   latest_replication_snapshot_time_usecs,
                   parent_protection_source,
                   protection_jobs,
                   protection_source,
                   rpo_policies,
                   total_archival_snapshots,
                   total_local_snapshots,
                   total_replication_snapshots)


