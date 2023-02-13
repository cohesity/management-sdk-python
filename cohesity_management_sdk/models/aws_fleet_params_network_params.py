# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class AWSFleetParams_NetworkParams(object):

    """Implementation of the 'AWSFleetParams_NetworkParams' model.

    Network params for the fleet.

    Attributes:
        region (string): Region for the VM.
        subnet (string): Subnet for the VM.
        vpc (string): VPC for the VM.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "region": 'region',
        "subnet": 'subnet',
        "vpc": 'vpc'
    }

    def __init__(self,
                 region=None,
                 subnet=None,
                 vpc=None):
        """Constructor for the AWSFleetParams_NetworkParams class"""

        # Initialize members of the class
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
        region = dictionary.get('region')
        subnet = dictionary.get('subnet', None)
        vpc = dictionary.get('vpc', None)

        # Return an object of this model
        return cls(region,
                   subnet,
                   vpc)


