# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.deploy_fleet_params
import cohesity_management_sdk.models.deploy_vms_to_aws_params
import cohesity_management_sdk.models.deploy_vms_to_azure_params
import cohesity_management_sdk.models.deploy_vms_to_gcp_params
import cohesity_management_sdk.models.replicate_snapshots_to_aws_params
import cohesity_management_sdk.models.replicate_snapshots_to_azure_params


class DeployVMsToCloudParams(object):

    """Implementation of the 'DeployVMsToCloudParams' model.

    Contains Cloud specific information needed to identify various resources
    when deploying a VM to Cloud.


    Attributes:

        deploy_fleet_params (DeployFleetParams): TODO: Type description here.
        deploy_vms_to_aws_params (DeployVMsToAWSParams): TODO: Type description
            here.
        deploy_vms_to_azure_params (DeployVMsToAzureParams): TODO: Type
            description here.
        deploy_vms_to_gcp_params (DeployVMsToGCPParams): TODO: Type description
            here.
        replicate_snapshots_to_aws_params (ReplicateSnapshotsToAWSParams):
            TODO: Type description here.
        replicate_snapshots_to_azure_params (ReplicateSnapshotsToAzureParams):
            TODO: Type description here.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "deploy_fleet_params":'deployFleetParams',
        "deploy_vms_to_aws_params":'deployVmsToAwsParams',
        "deploy_vms_to_azure_params":'deployVmsToAzureParams',
        "deploy_vms_to_gcp_params":'deployVmsToGcpParams',
        "replicate_snapshots_to_aws_params":'replicateSnapshotsToAwsParams',
        "replicate_snapshots_to_azure_params":'replicateSnapshotsToAzureParams',
    }
    def __init__(self,
                 deploy_fleet_params=None,
                 deploy_vms_to_aws_params=None,
                 deploy_vms_to_azure_params=None,
                 deploy_vms_to_gcp_params=None,
                 replicate_snapshots_to_aws_params=None,
                 replicate_snapshots_to_azure_params=None,
            ):

        """Constructor for the DeployVMsToCloudParams class"""

        # Initialize members of the class
        self.deploy_fleet_params = deploy_fleet_params
        self.deploy_vms_to_aws_params = deploy_vms_to_aws_params
        self.deploy_vms_to_azure_params = deploy_vms_to_azure_params
        self.deploy_vms_to_gcp_params = deploy_vms_to_gcp_params
        self.replicate_snapshots_to_aws_params = replicate_snapshots_to_aws_params
        self.replicate_snapshots_to_azure_params = replicate_snapshots_to_azure_params

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
        deploy_fleet_params = cohesity_management_sdk.models.deploy_fleet_params.DeployFleetParams.from_dictionary(dictionary.get('deployFleetParams')) if dictionary.get('deployFleetParams') else None
        deploy_vms_to_aws_params = cohesity_management_sdk.models.deploy_vms_to_aws_params.DeployVMsToAWSParams.from_dictionary(dictionary.get('deployVmsToAwsParams')) if dictionary.get('deployVmsToAwsParams') else None
        deploy_vms_to_azure_params = cohesity_management_sdk.models.deploy_vms_to_azure_params.DeployVMsToAzureParams.from_dictionary(dictionary.get('deployVmsToAzureParams')) if dictionary.get('deployVmsToAzureParams') else None
        deploy_vms_to_gcp_params = cohesity_management_sdk.models.deploy_vms_to_gcp_params.DeployVMsToGCPParams.from_dictionary(dictionary.get('deployVmsToGcpParams')) if dictionary.get('deployVmsToGcpParams') else None
        replicate_snapshots_to_aws_params = cohesity_management_sdk.models.replicate_snapshots_to_aws_params.ReplicateSnapshotsToAWSParams.from_dictionary(dictionary.get('replicateSnapshotsToAwsParams')) if dictionary.get('replicateSnapshotsToAwsParams') else None
        replicate_snapshots_to_azure_params = cohesity_management_sdk.models.replicate_snapshots_to_azure_params.ReplicateSnapshotsToAzureParams.from_dictionary(dictionary.get('replicateSnapshotsToAzureParams')) if dictionary.get('replicateSnapshotsToAzureParams') else None

        # Return an object of this model
        return cls(
            deploy_fleet_params,
            deploy_vms_to_aws_params,
            deploy_vms_to_azure_params,
            deploy_vms_to_gcp_params,
            replicate_snapshots_to_aws_params,
            replicate_snapshots_to_azure_params
)