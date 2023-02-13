# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto

class ReplicateSnapshotsToAWSParams(object):

    """Implementation of the 'ReplicateSnapshotsToAWSParams' model.

    Params required to replicate snapshots to another AWS source. This is
    populated for AWS snapshot manager replication.

    Attributes:
        region (EntityProto): Specifies the attributes and the latest
            statistics about an entity.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "region":'region'
    }

    def __init__(self,
                 region=None):
        """Constructor for the ReplicateSnapshotsToAWSParams class"""

        # Initialize members of the class
        self.region = region


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
        region = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('region')) if dictionary.get('region') else None

        # Return an object of this model
        return cls(region)


