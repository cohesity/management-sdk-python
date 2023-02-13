# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto

class DeployVMsToGCPParams(object):

    """Implementation of the 'DeployVMsToGCPParams' model.

    Contains GCP specific information needed to identify various resources
    when converting and deploying a VM to GCP.

    Attributes:
        project_id (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        region (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        subnet (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        zone (EntityProto): Specifies the attributes and the latest statistics
            about an entity.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "project_id":'projectId',
        "region":'region',
        "subnet":'subnet',
        "zone":'zone'
    }

    def __init__(self,
                 project_id=None,
                 region=None,
                 subnet=None,
                 zone=None):
        """Constructor for the DeployVMsToGCPParams class"""

        # Initialize members of the class
        self.project_id = project_id
        self.region = region
        self.subnet = subnet
        self.zone = zone


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
        project_id = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('projectId')) if dictionary.get('projectId') else None
        region = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('region')) if dictionary.get('region') else None
        subnet = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('subnet')) if dictionary.get('subnet') else None
        zone = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('zone')) if dictionary.get('zone') else None

        # Return an object of this model
        return cls(project_id,
                   region,
                   subnet,
                   zone)


