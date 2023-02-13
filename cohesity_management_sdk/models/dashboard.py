# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.audit_logs_tile
import cohesity_management_sdk.models.health_tile
import cohesity_management_sdk.models.iops_tile
import cohesity_management_sdk.models.job_runs_tile
import cohesity_management_sdk.models.protected_objects_tile
import cohesity_management_sdk.models.protection_tile
import cohesity_management_sdk.models.recoveries_tile
import cohesity_management_sdk.models.storage_efficiency_tile
import cohesity_management_sdk.models.throughput_tile

class Dashboard(object):

    """Implementation of the 'Dashboard' model.

    Data shown on Dashboard.

    Attributes:
        audit_logs (AuditLogsTile):  Audit Logs.
        cluster_id (int|long): Id of the cluster for which dashboard is given.
        health (HealthTile): Cluster Health and alerts.
        iops (IopsTile): IOPs
        job_runs (JobRunsTile): Protection Job Runs.
        protected_objects (ProtectedObjectsTile): ProtectedObjects related
            stats.
        protection (ProtectionTile): Protection related stats.
        recoveries (RecoveriesTile): Recoveries related stats.
        storage_efficiency (StorageEfficiencyTile): Storage efficiency stats.
        throughput (ThroughputTile): Throughput.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "audit_logs":'auditLogs',
        "cluster_id":'clusterId',
        "health":'health',
        "iops":'iops',
        "job_runs":'jobRuns',
        "protected_objects":'protectedObjects',
        "protection":'protection',
        "recoveries":'recoveries',
        "storage_efficiency":'storageEfficiency',
        "throughput":'throughput'
    }

    def __init__(self,
                 audit_logs=None,
                 cluster_id=None,
                 health=None,
                 iops=None,
                 job_runs=None,
                 protected_objects=None,
                 protection=None,
                 recoveries=None,
                 storage_efficiency=None,
                 throughput=None):
        """Constructor for the Dashboard class"""

        # Initialize members of the class
        self.audit_logs = audit_logs
        self.cluster_id = cluster_id
        self.health = health
        self.iops = iops
        self.job_runs = job_runs
        self.protected_objects = protected_objects
        self.protection = protection
        self.recoveries = recoveries
        self.storage_efficiency = storage_efficiency
        self.throughput = throughput


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
        audit_logs = cohesity_management_sdk.models.audit_logs_tile.AuditLogsTile.from_dictionary(dictionary.get('auditLogs')) if dictionary.get('auditLogs') else None
        cluster_id = dictionary.get('clusterId')
        health = cohesity_management_sdk.models.health_tile.HealthTile.from_dictionary(dictionary.get('health')) if dictionary.get('health') else None
        iops = cohesity_management_sdk.models.iops_tile.IopsTile.from_dictionary(dictionary.get('iops', None)) if  dictionary.get('iops', None) else None
        job_runs = cohesity_management_sdk.models.job_runs_tile.JobRunsTile.from_dictionary(dictionary.get('jobRuns')) if dictionary.get('jobRuns') else None
        protected_objects = cohesity_management_sdk.models.protected_objects_tile.ProtectedObjectsTile.from_dictionary(dictionary.get('protectedObjects')) if dictionary.get('protectedObjects') else None
        protection = cohesity_management_sdk.models.protection_tile.ProtectionTile.from_dictionary(dictionary.get('protection')) if dictionary.get('protection') else None
        recoveries = cohesity_management_sdk.models.recoveries_tile.RecoveriesTile.from_dictionary(dictionary.get('recoveries')) if dictionary.get('recoveries') else None
        storage_efficiency = cohesity_management_sdk.models.storage_efficiency_tile.StorageEfficiencyTile.from_dictionary(dictionary.get('storageEfficiency')) if dictionary.get('storageEfficiency') else None
        throughput = cohesity_management_sdk.models.throughput_tile.ThroughputTile.from_dictionary(dictionary.get('throughput')) if dictionary.get('throughput') else None

        # Return an object of this model
        return cls(audit_logs,
                   cluster_id,
                   health,
                   iops,
                   job_runs,
                   protected_objects,
                   protection,
                   recoveries,
                   storage_efficiency,
                   throughput)


