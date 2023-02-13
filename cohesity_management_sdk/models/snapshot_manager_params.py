# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.aws_snapshot_manager_params

class SnapshotManagerParams(object):

    """Implementation of the 'SnapshotManagerParams' model.

    TODO: type model description here.

    Attributes:
        aws_snapshot_manager_params (AWSSnapshotManagerParams): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "aws_snapshot_manager_params":'awsSnapshotManagerParams'
    }

    def __init__(self,
                 aws_snapshot_manager_params=None):
        """Constructor for the SnapshotManagerParams class"""

        # Initialize members of the class
        self.aws_snapshot_manager_params = aws_snapshot_manager_params


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
        aws_snapshot_manager_params = cohesity_management_sdk.models.aws_snapshot_manager_params.AWSSnapshotManagerParams.from_dictionary(dictionary.get('awsSnapshotManagerParams')) if dictionary.get('awsSnapshotManagerParams') else None

        # Return an object of this model
        return cls(aws_snapshot_manager_params)


