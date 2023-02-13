# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.aws_fleet_params

class DeployFleetParams(object):

    """Implementation of the 'DeployFleetParams' model.

    Contains Fleet specific params.

    Attributes:
        aws_fleet_params (AWSFleetParams): Contains AWS Fleet specific params.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "aws_fleet_params":'awsFleetParams'
    }

    def __init__(self,
                 aws_fleet_params=None):
        """Constructor for the DeployFleetParams class"""

        # Initialize members of the class
        self.aws_fleet_params = aws_fleet_params


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
        aws_fleet_params = cohesity_management_sdk.models.aws_fleet_params.AWSFleetParams.from_dictionary(dictionary.get('awsFleetParams', None)) if dictionary.get('awsFleetParams', None) else None

        # Return an object of this model
        return cls(aws_fleet_params)


