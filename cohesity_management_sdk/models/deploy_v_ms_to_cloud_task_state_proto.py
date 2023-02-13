# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.deploy_v_ms_to_cloud_params

class DeployVMsToCloudTaskStateProto(object):

    """Implementation of the 'DeployVMsToCloudTaskStateProto' model.

    TODO: type model description here.

    Attributes:
        deploy_vms_to_cloud_params (DeployVMsToCloudParams): Contains Cloud
            specific information needed to identify various resources when
            deploying a VM to Cloud.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "deploy_vms_to_cloud_params":'deployVmsToCloudParams'
    }

    def __init__(self,
                 deploy_vms_to_cloud_params=None):
        """Constructor for the DeployVMsToCloudTaskStateProto class"""

        # Initialize members of the class
        self.deploy_vms_to_cloud_params = deploy_vms_to_cloud_params


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

        # Return an object of this model
        return cls(deploy_vms_to_cloud_params)


