# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class AWSFleetParams_NetworkParams(object):

    """Implementation of the 'AWSFleetParams_NetworkParams' model.

    Network params for the fleet.

    Attributes:
        subnet (string): Subnet for the fleet.
        vpc (string): VPC for the fleet.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "subnet": 'subnet',
        "vpc": 'vpc'
    }

    def __init__(self,
                 subnet=None,
                 vpc=None):
        """Constructor for the AWSFleetParams_NetworkParams class"""

        # Initialize members of the class
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
        subnet = dictionary.get('subnet', None)
        vpc = dictionary.get('vpc', None)

        # Return an object of this model
        return cls(subnet,
                   vpc)


