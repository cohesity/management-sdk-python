# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.archival_target
import cohesity_management_sdk.models.cloud_deploy_target
import cohesity_management_sdk.models.on_prem_deploy_target
import cohesity_management_sdk.models.replication_target


class SnapshotTarget(object):

    """Implementation of the 'SnapshotTarget' model.

    Message that specifies details about a target (such as a replication or
    archival target) where a backup snapshot may be copied to.


    Attributes:

        archival_target (ArchivalTarget): The archival target for the backup
            snapshot.
        cloud_deploy_target (CloudDeployTarget): The cloud deploy target for
            the backup snapshot. This will be populated for both kCloudDeploy
            and kCloudReplication tasks.
        onprem_deploy_target (OnPremDeployTarget): The on-prem deploy target
            for the snapshots. This will be populated for kOnPremDeploy.
        replication_target (ReplicationTarget): The remote replication target
            for the backup snapshot.
        mtype (int): The type of snapshot target this proto represents.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "archival_target":'archivalTarget',
        "cloud_deploy_target":'cloudDeployTarget',
        "onprem_deploy_target":'onpremDeployTarget',
        "replication_target":'replicationTarget',
        "mtype":'type',
    }
    def __init__(self,
                 archival_target=None,
                 cloud_deploy_target=None,
                 onprem_deploy_target=None,
                 replication_target=None,
                 mtype=None,
            ):

        """Constructor for the SnapshotTarget class"""

        # Initialize members of the class
        self.archival_target = archival_target
        self.cloud_deploy_target = cloud_deploy_target
        self.onprem_deploy_target = onprem_deploy_target
        self.replication_target = replication_target
        self.mtype = mtype

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
        archival_target = cohesity_management_sdk.models.archival_target.ArchivalTarget.from_dictionary(dictionary.get('archivalTarget')) if dictionary.get('archivalTarget') else None
        cloud_deploy_target = cohesity_management_sdk.models.cloud_deploy_target.CloudDeployTarget.from_dictionary(dictionary.get('cloudDeployTarget')) if dictionary.get('cloudDeployTarget') else None
        onprem_deploy_target = cohesity_management_sdk.models.on_prem_deploy_target.OnPremDeployTarget.from_dictionary(dictionary.get('onpremDeployTarget')) if dictionary.get('onpremDeployTarget') else None
        replication_target = cohesity_management_sdk.models.replication_target.ReplicationTarget.from_dictionary(dictionary.get('replicationTarget')) if dictionary.get('replicationTarget') else None
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(
            archival_target,
            cloud_deploy_target,
            onprem_deploy_target,
            replication_target,
            mtype
)