# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.aws_params
import cohesity_management_sdk.models.azure_params
import cohesity_management_sdk.models.fleet_params

class DeployVmsToCloud(object):

    """Implementation of the 'DeployVmsToCloud' model.

    Specifies the details about deploying vms to specific clouds where backup
    may be stored and converted.

    Attributes:
        aws_params (AwsParams): Specifies various resources when converting
            and deploying a VM to AWS.
        azure_params (AzureParams): Specifies various resources when
            converting and deploying a VM to Azure.
        fleet_params (FleetParams): Specifies various resources when deploying
            vms to fleet instances.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "aws_params":'awsParams',
        "azure_params":'azureParams',
        "fleet_params":'fleetParams'
    }

    def __init__(self,
                 aws_params=None,
                 azure_params=None,
                 fleet_params=None):
        """Constructor for the DeployVmsToCloud class"""

        # Initialize members of the class
        self.aws_params = aws_params
        self.azure_params = azure_params
        self.fleet_params = fleet_params


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
        aws_params = cohesity_management_sdk.models.aws_params.AwsParams.from_dictionary(dictionary.get('awsParams')) if dictionary.get('awsParams') else None
        azure_params = cohesity_management_sdk.models.azure_params.AzureParams.from_dictionary(dictionary.get('azureParams')) if dictionary.get('azureParams') else None
        fleet_params = cohesity_management_sdk.models.fleet_params.FleetParams.from_dictionary(dictionary.get('fleetParams')) if dictionary.get('fleetParams') else None

        # Return an object of this model
        return cls(aws_params,
                   azure_params,
                   fleet_params)


