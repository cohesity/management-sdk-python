# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.lifecycle_rule_filter_and
import cohesity_management_sdk.models.lifecycle_rule_filter_tag

class LifecycleRuleFilter(object):

    """Implementation of the 'LifecycleRuleFilter' model.

    Attributes:
        mand (LifecycleRuleFilterAnd): This is used in a Lifecycle Rule Filter
            to apply a logical AND to two or more predicates. The Lifecycle
            Rule will apply to any object matching all of the predicates
            configured inside the And operator.
        prefix (string): Prefix identifying one or more objects to which the
            rule applies.
        tag (LifecycleRuleFilterTag):This tag must exist in the object's tag set in order for the rule to
          apply.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mand":'and',
        "prefix":'prefix',
        "tag":'tag'
    }

    def __init__(self,
                 mand=None,
                 prefix=None,
                 tag=None):
        """Constructor for the LifecycleRuleFilter class"""

        # Initialize members of the class
        self.mand = mand
        self.prefix = prefix
        self.tag = tag


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
        mand = cohesity_management_sdk.models.lifecycle_rule_filter_and.LifecycleRuleFilterAnd.from_dictionary(dictionary.get('and')) if dictionary.get('and') else None
        prefix = dictionary.get('prefix')
        tag = cohesity_management_sdk.models.lifecycle_rule_filter_tag.LifecycleRuleFilterTag.from_dictionary(dictionary.get('tag')) if dictionary.get('tag') else None

        # Return an object of this model
        return cls(mand,
                   prefix,
                   tag)


