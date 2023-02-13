# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class UpgradeClusterParameters(object):

    """Implementation of the 'UpgradeClusterParameters' model.

    Specifies the parameters needed for a Cluster Upgrade request.

    Attributes:
        target_sw_version (string): Specifies the target software version. If
            specified, all Nodes on the Cluster will be searched to see if
            they have had the specified software package uploaded to them. If
            the specified package is found, then it will be used for the
            upgrade.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "target_sw_version":'targetSwVersion'
    }

    def __init__(self,
                 target_sw_version=None):
        """Constructor for the UpgradeClusterParameters class"""

        # Initialize members of the class
        self.target_sw_version = target_sw_version


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
        target_sw_version = dictionary.get('targetSwVersion')

        # Return an object of this model
        return cls(target_sw_version)


