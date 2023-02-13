# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.universal_id
import cohesity_management_sdk.models.protection_source
import cohesity_management_sdk.models.snapshot_version

class ObjectSnapshotInfo(object):

    """Implementation of the 'ObjectSnapshotInfo' model.

    Specifies information about an object that has been backed up.

    Attributes:
        cluster_partition_id (long|int): Specifies the Cohesity Cluster
            partition id where this object is stored.
        job_id (long|int): Specifies the id for the Protection Job that is
            currently associated with the object. If the object was backed up
            on current Cohesity Cluster, this field contains the id for the
            Job that captured this backup object. If the object was backed up
            on a Primary Cluster and replicated to this Cohesity Cluster, a
            new Inactive Job is created, the object is now associated with new
            Inactive Job, and this field contains the id of the new Inactive
            Job.
        job_name (string): Specifies the name of the Protection Job that
            captured the backup.
        job_uid (UniversalId): Specifies the globally unique id of the
            Protection Job that backed up this object. This id is unique
            across Cohesity Clusters. Even if this object is replicated to a
            Remote Cohesity Cluster and the object is associated with a new
            Job, the value specified in this field does not change.
        object_name (string): Specifies the primary name of the object.
        os_type (string): Specifies the inferred OS type.
        registered_source (ProtectionSource): Specifies a generic structure
            that represents a node in the Protection Source tree. Node details
            will depend on the environment of the Protection Source.
        snapshotted_source (ProtectionSource): Specifies a generic structure
            that represents a node in the Protection Source tree. Node details
            will depend on the environment of the Protection Source.
        versions (list of SnapshotVersion): Array of Snapshots.  Specifies all
            snapshot versions of this object. Each time a Job Run of a Job
            executes, it may create a new snapshot version of an object. This
            array stores the different snapshots versions of the object.
        view_box_id (long|int): Specifies the id of the Domain (View Box)
            where this object is stored.
        view_name (string): Specifies the View name where this object is
            stored.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cluster_partition_id":'clusterPartitionId',
        "job_id":'jobId',
        "job_name":'jobName',
        "job_uid":'jobUid',
        "object_name":'objectName',
        "os_type":'osType',
        "registered_source":'registeredSource',
        "snapshotted_source":'snapshottedSource',
        "versions":'versions',
        "view_box_id":'viewBoxId',
        "view_name":'viewName'
    }

    def __init__(self,
                 cluster_partition_id=None,
                 job_id=None,
                 job_name=None,
                 job_uid=None,
                 object_name=None,
                 os_type=None,
                 registered_source=None,
                 snapshotted_source=None,
                 versions=None,
                 view_box_id=None,
                 view_name=None):
        """Constructor for the ObjectSnapshotInfo class"""

        # Initialize members of the class
        self.cluster_partition_id = cluster_partition_id
        self.job_id = job_id
        self.job_name = job_name
        self.job_uid = job_uid
        self.object_name = object_name
        self.os_type = os_type
        self.registered_source = registered_source
        self.snapshotted_source = snapshotted_source
        self.versions = versions
        self.view_box_id = view_box_id
        self.view_name = view_name


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
        cluster_partition_id = dictionary.get('clusterPartitionId')
        job_id = dictionary.get('jobId')
        job_name = dictionary.get('jobName')
        job_uid = cohesity_management_sdk.models.universal_id.UniversalId.from_dictionary(dictionary.get('jobUid')) if dictionary.get('jobUid') else None
        object_name = dictionary.get('objectName')
        os_type = dictionary.get('osType')
        registered_source = cohesity_management_sdk.models.protection_source.ProtectionSource.from_dictionary(dictionary.get('registeredSource')) if dictionary.get('registeredSource') else None
        snapshotted_source = cohesity_management_sdk.models.protection_source.ProtectionSource.from_dictionary(dictionary.get('snapshottedSource')) if dictionary.get('snapshottedSource') else None
        versions = None
        if dictionary.get('versions') != None:
            versions = list()
            for structure in dictionary.get('versions'):
                versions.append(cohesity_management_sdk.models.snapshot_version.SnapshotVersion.from_dictionary(structure))
        view_box_id = dictionary.get('viewBoxId')
        view_name = dictionary.get('viewName')

        # Return an object of this model
        return cls(cluster_partition_id,
                   job_id,
                   job_name,
                   job_uid,
                   object_name,
                   os_type,
                   registered_source,
                   snapshotted_source,
                   versions,
                   view_box_id,
                   view_name)


