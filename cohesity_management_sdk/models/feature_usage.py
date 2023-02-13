# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class FeatureUsage(object):

    """Implementation of the 'FeatureUsage' model.

    Structure to hold feature usage on cluster side.

    Attributes:
        current_usage_gib (long|int): Feature usage by the cluster.
        feature_name (string): Name of feature.
        num_vm (long|int): Number of VM spinned.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "current_usage_gib":'currentUsageGiB',
        "feature_name":'featureName',
        "num_vm":'numVm'
    }

    def __init__(self,
                 current_usage_gib=None,
                 feature_name=None,
                 num_vm=None):
        """Constructor for the FeatureUsage class"""

        # Initialize members of the class
        self.current_usage_gib = current_usage_gib
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
        current_usage_gib = dictionary.get('currentUsageGiB')
        feature_name = dictionary.get('featureName')
        num_vm = dictionary.get('numVm')

        # Return an object of this model
        return cls(current_usage_gib,
                   feature_name,
                   num_vm)


