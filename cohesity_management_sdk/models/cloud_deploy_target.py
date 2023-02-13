# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.deploy_v_ms_to_cloud_params
import cohesity_management_sdk.models.entity_proto

class CloudDeployTarget(object):

    """Implementation of the 'CloudDeployTarget' model.

    Message that specifies the details about CloudDeploy target where backup
    snapshots may be converted and stored.

    Attributes:
        deploy_vms_to_cloud_params (DeployVMsToCloudParams): Contains Cloud
            specific information needed to identify various resources when
            deploying a VM to Cloud.
        target_entity (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        mtype (int): The type of the CloudDeploy target.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "deploy_vms_to_cloud_params":'deployVmsToCloudParams',
        "target_entity":'targetEntity',
        "mtype":'type'
    }

    def __init__(self,
                 deploy_vms_to_cloud_params=None,
                 target_entity=None,
                 mtype=None):
        """Constructor for the CloudDeployTarget class"""

        # Initialize members of the class
        self.deploy_vms_to_cloud_params = deploy_vms_to_cloud_params
        self.target_entity = target_entity
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
        deploy_vms_to_cloud_params = cohesity_management_sdk.models.deploy_v_ms_to_cloud_params.DeployVMsToCloudParams.from_dictionary(dictionary.get('deployVmsToCloudParams')) if dictionary.get('deployVmsToCloudParams') else None
        target_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('targetEntity')) if dictionary.get('targetEntity') else None
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(deploy_vms_to_cloud_params,
                   target_entity,
                   mtype)


