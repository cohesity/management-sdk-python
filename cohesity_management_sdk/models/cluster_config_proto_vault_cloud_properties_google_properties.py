# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ClusterConfigProto_Vault_CloudProperties_GoogleProperties(object):

    """Implementation of the 'ClusterConfigProto_Vault_CloudProperties_GoogleProperties' model.

    Attributes:
        tier_type (int): TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "tier_type": 'tierType'
    }

    def __init__(self,
                 tier_type=None):
        """Constructor for the ClusterConfigProto_Vault_CloudProperties_GoogleProperties class"""

        # Initialize members of the class
        self.tier_type = tier_type


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
        tier_type = dictionary.get('tierType', None)

        # Return an object of this model
        return cls(tier_type)


