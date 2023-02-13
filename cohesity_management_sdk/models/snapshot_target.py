# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.archival_target
import cohesity_management_sdk.models.cloud_deploy_target
import cohesity_management_sdk.models.replication_target

class SnapshotTarget(object):

    """Implementation of the 'SnapshotTarget' model.

    Message that specifies details about a target (such as a replication or
    archival target) where a backup snapshot may be copied to.

    Attributes:
        archival_target (ArchivalTarget): Message that specifies the details
            about an archival target (such as cloud or tape) where backup
            snapshots may be archived to.
        cloud_deploy_target (CloudDeployTarget): Message that specifies the
            details about CloudDeploy target where backup snapshots may be
            converted and stored.
        replication_target (ReplicationTarget): Message that specifies the
            details about a remote cluster where backup snapshots may be
            replicated to.
        mtype (int): The type of snapshot target this proto represents.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "archival_target":'archivalTarget',
        "cloud_deploy_target":'cloudDeployTarget',
        "replication_target":'replicationTarget',
        "mtype":'type'
    }

    def __init__(self,
                 archival_target=None,
                 cloud_deploy_target=None,
                 replication_target=None,
                 mtype=None):
        """Constructor for the SnapshotTarget class"""

        # Initialize members of the class
        self.archival_target = archival_target
        self.cloud_deploy_target = cloud_deploy_target
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
        replication_target = cohesity_management_sdk.models.replication_target.ReplicationTarget.from_dictionary(dictionary.get('replicationTarget')) if dictionary.get('replicationTarget') else None
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(archival_target,
                   cloud_deploy_target,
                   replication_target,
                   mtype)


