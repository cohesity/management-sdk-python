# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class FleetNetworkParams(object):

    """Implementation of the 'FleetNetworkParams' model.

    Specifies the various network params for the fleet.


    Attributes:

        project_id (string): Specifies the project id for the fleet in case of
            GCP Source.
        region (string): Specifies the region for the fleet.
        subnet (string): Specifies the subnet for the fleet.
        vpc (string): Specifies the vpc for the fleet.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "project_id":'projectId',
        "region":'region',
        "subnet":'subnet',
        "vpc":'vpc',
    }
    def __init__(self,
                 project_id=None,
                 region=None,
                 subnet=None,
                 vpc=None,
            ):

        """Constructor for the FleetNetworkParams class"""

        # Initialize members of the class
        self.project_id = project_id
        self.region = region
        self.subnet = subnet
        self.vpc = vpc

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
        project_id = dictionary.get('projectId')
        region = dictionary.get('region')
        subnet = dictionary.get('subnet')
        vpc = dictionary.get('vpc')

        # Return an object of this model
        return cls(
            project_id,
            region,
            subnet,
            vpc
)