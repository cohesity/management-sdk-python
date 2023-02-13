# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class CloudParameters(object):

    """Implementation of the 'CloudParameters' model.

    Specifies Cloud parameters that are applicable to all Protection
    Sources in a Protection Job in certain scenarios.

    Attributes:
        failover_to_cloud (bool): Specifies whether the Protection Sources in
            this Protection Job will be failed over to Cloud. This flag is
            applicable to backup on-prem Sources.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "failover_to_cloud":'failoverToCloud'
    }

    def __init__(self,
                 failover_to_cloud=None):
        """Constructor for the CloudParameters class"""

        # Initialize members of the class
        self.failover_to_cloud = failover_to_cloud


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
        failover_to_cloud = dictionary.get('failoverToCloud')

        # Return an object of this model
        return cls(failover_to_cloud)


