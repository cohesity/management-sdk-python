# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class Overusage(object):

    """Implementation of the 'Overusage' model.

    Structure to hold feature usage on cluster side.

    Attributes:
        feature_name (string):  Name of feature.
        overused_gb (int|long): Feature overusage by the cluster.
        overused_vm (int|long): Number of overused VM spinned.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "feature_name":'featureName',
        "overused_gb":'overusedGB',
        "overused_vm":'overusedVm'
    }

    def __init__(self,
                 feature_name=None,
                 overused_gb=None,
                 overused_vm=None):
        """Constructor for the Overusage class"""

        # Initialize members of the class
        self.feature_name = feature_name
        self.overused_gb = overused_gb
        self.overused_vm = overused_vm


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
        feature_name = dictionary.get('featureName')
        overused_gb = dictionary.get('overusedGB')
        overused_vm = dictionary.get('overusedVm')

        # Return an object of this model
        return cls(feature_name,
                   overused_gb,
                   overused_vm)


