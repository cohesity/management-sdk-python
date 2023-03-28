# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.ownership_controls_rule


class BucketOwnershipControls(object):

    """Implementation of the 'BucketOwnershipControls' model.

    Protobuf that describes the bucket ownership control configuarion that is
    used to manage the ownership of objects in a bucket.


    Attributes:

        rule (OwnershipControlsRule): Rule for bucket ownership control.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "rule":'rule',
    }
    def __init__(self,
                 rule=None,
            ):

        """Constructor for the BucketOwnershipControls class"""

        # Initialize members of the class
        self.rule = rule

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
        rule = cohesity_management_sdk.models.ownership_controls_rule.OwnershipControlsRule.from_dictionary(dictionary.get('rule')) if dictionary.get('rule') else None

        # Return an object of this model
        return cls(
            rule
)