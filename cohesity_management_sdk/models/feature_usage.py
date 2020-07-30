# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class FeatureUsage(object):

    """Implementation of the 'FeatureUsage' model.

    Structure to hold feature usage on cluster side.

    Attributes:
        current_usage (int): Feature usage by the cluster.
        feature_name (string): Name of feature.
        num_vm (int): Number of VM spinned.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "current_usage":'currentUsage',
        "feature_name":'featureName',
        "num_vm":'numVm'
    }

    def __init__(self,
                 current_usage=None,
                 feature_name=None,
                 num_vm=None):
        """Constructor for the FeatureUsage class"""

        # Initialize members of the class
        self.current_usage = current_usage
        self.feature_name = feature_name
        self.num_vm = num_vm


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
        current_usage = dictionary.get('currentUsage')
        feature_name = dictionary.get('featureName')
        num_vm = dictionary.get('numVm')

        # Return an object of this model
        return cls(current_usage,
                   feature_name,
                   num_vm)


