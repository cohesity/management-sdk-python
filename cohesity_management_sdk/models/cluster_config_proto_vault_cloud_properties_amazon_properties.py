# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ClusterConfigProto_Vault_CloudProperties_AmazonProperties(object):

    """Implementation of the 'ClusterConfigProto_Vault_CloudProperties_AmazonProperties' model.

    Attributes:
        enable_lambda_based_gc (bool): Whether this vault supports AWS Lambda
            based GC. A Lambda function needs to be deployed in the customer's AWS
            environment or the IAM user should have permissions to create one.
        lambda_function_version (int): Version of the Lambda function deployed in the cloud.
        tier_type (int): TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enable_lambda_based_gc":'enableLambdaBasedGc',
        "lambda_function_version":'lambdaFunctionVersion',
        "tier_type":'tierType'
    }

    def __init__(self,
                 enable_lambda_based_gc=None,
                 lambda_function_version=None,
                 tier_type=None):
        """Constructor for the ClusterConfigProto_Vault_CloudProperties_AmazonProperties class"""

        # Initialize members of the class
        self.enable_lambda_based_gc = enable_lambda_based_gc
        self.lambda_function_version = lambda_function_version
        self.tier_type = tier_type


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
        enable_lambda_based_gc = dictionary.get('enableLambdaBasedGc')
        lambda_function_version = dictionary.get('lambdaFunctionVersion')
        tier_type = dictionary.get('tierType')

        # Return an object of this model
        return cls(enable_lambda_based_gc,
                   lambda_function_version,
                   tier_type)


