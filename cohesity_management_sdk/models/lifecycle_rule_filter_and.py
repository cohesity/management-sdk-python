# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.lifecycle_rule_filter_tag

class LifecycleRuleFilterAnd(object):

    """Implementation of the 'LifecycleRuleFilterAnd' model.

    Attributes:
        prefix (string): Prefix identifying one or more objects to which the
            rule applies.
        tag_vec (list of LifecycleRuleFilterTag): All of these tags must exist
            in the object's tag set in order for the rule to apply.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "prefix":'prefix',
        "tag_vec":'tagVec'
    }

    def __init__(self,
                 prefix=None,
                 tag_vec=None):
        """Constructor for the LifecycleRuleFilterAnd class"""

        # Initialize members of the class
        self.prefix = prefix
        self.tag_vec = tag_vec


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
        prefix = dictionary.get('prefix', None)
        tag_vec = None
        if dictionary.get('tagVec', None) != None:
            tag_vec = list()
            for structure in dictionary.get('tagVec'):
                tag_vec.append(cohesity_management_sdk.models.lifecycle_rule_filter_tag.LifecycleRuleFilterTag.from_dictionary(structure))

        # Return an object of this model
        return cls(prefix, tag_vec)


