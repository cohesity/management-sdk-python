# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.aws_params
import cohesity_management_sdk.models.azure_params
import cohesity_management_sdk.models.gcp_params

class CloudDeployTargetDetails(object):

    """Implementation of the 'CloudDeployTargetDetails' model.

    Message that specifies the details about CloudDeploy target where backup
    snapshots may be converted and stored.

    Attributes:
        aws_params (AwsParams): Specifies various resources when converting
            and deploying a VM to AWS.
        azure_params (AzureParams): Specifies various resources when
            converting and deploying a VM to Azure.
        gcp_params (GcpParams): Specifies various resources when converting
            and deploying a VM to GCP.
        id (long|int): Entity corresponding to the cloud deploy target.
            Specifies the id field inside the EntityProto.
        name (string): Specifies the inner object's name or a human-readable
            string made off the salient attributes. This is only plumbed when
            Entity objects are exposed to Iris BE or to Yoda.
        mtype (TypeCloudDeployTargetDetailsEnum): Specifies the type of the
            CloudDeploy target. 'kAzure' indicates that Azure as a cloud
            deploy target type. 'kAWS' indicates that AWS as a cloud deploy
            target type. 'kGCP' indicates that GCP as a cloud deploy target
            type.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "aws_params":'awsParams',
        "azure_params":'azureParams',
        "gcp_params":'gcpParams',
        "id":'id',
        "name":'name',
        "mtype":'type'
    }

    def __init__(self,
                 aws_params=None,
                 azure_params=None,
                 gcp_params=None,
                 id=None,
                 name=None,
                 mtype=None):
        """Constructor for the CloudDeployTargetDetails class"""

        # Initialize members of the class
        self.aws_params = aws_params
        self.azure_params = azure_params
        self.gcp_params = gcp_params
        self.id = id
        self.name = name
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
        aws_params = cohesity_management_sdk.models.aws_params.AwsParams.from_dictionary(dictionary.get('awsParams')) if dictionary.get('awsParams') else None
        azure_params = cohesity_management_sdk.models.azure_params.AzureParams.from_dictionary(dictionary.get('azureParams')) if dictionary.get('azureParams') else None
        gcp_params = cohesity_management_sdk.models.gcp_params.GcpParams.from_dictionary(dictionary.get('gcpParams')) if dictionary.get('gcpParams') else None
        id = dictionary.get('id')
        name = dictionary.get('name')
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(aws_params,
                   azure_params,
                   gcp_params,
                   id,
                   name,
                   mtype)


