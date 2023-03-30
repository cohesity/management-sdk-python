# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.condition_condition_key_values_map_entry


class Condition(object):

    """Implementation of the 'Condition' model.

    TODO: type description here.


    Attributes:

        cond_operator (int): This field describes the operator to use to
            perform the condition checks.
        condition_key_values_map (list of
            Condition_ConditionKeyValuesMapEntry): This field describes the
            condition keys and the values specified for that key. An example of
            key is "s3:x-amz-acl" with values like "public-read", meaning that
            the request should include "public-read" in the ACL header.
        for_all_values (bool): This field describes whether the condition
            matches all of the input values matches against any at least one of
            the values in 'condition_key_values_map'.
        for_any_value (bool): This field describes whether the condition
            matches any of the input values matches against any one of the
            values in 'condition_key_values_map'.
        if_exists (bool): This field describes whether to evaluate condition as
            true if the condition key does not exist and if it exists then it
            should match the values from 'condition_key_values_map'.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "cond_operator":'condOperator',
        "condition_key_values_map":'conditionKeyValuesMap',
        "for_all_values":'forAllValues',
        "for_any_value":'forAnyValue',
        "if_exists":'ifExists',
    }
    def __init__(self,
                 cond_operator=None,
                 condition_key_values_map=None,
                 for_all_values=None,
                 for_any_value=None,
                 if_exists=None,
            ):

        """Constructor for the Condition class"""

        # Initialize members of the class
        self.cond_operator = cond_operator
        self.condition_key_values_map = condition_key_values_map
        self.for_all_values = for_all_values
        self.for_any_value = for_any_value
        self.if_exists = if_exists

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
        cond_operator = dictionary.get('condOperator')
        condition_key_values_map = None
        if dictionary.get('conditionKeyValuesMap') != None:
            condition_key_values_map = list()
            for structure in dictionary.get('conditionKeyValuesMap'):
                condition_key_values_map.append(cohesity_management_sdk.models.condition_condition_key_values_map_entry.Condition_ConditionKeyValuesMapEntry.from_dictionary(structure))
        for_all_values = dictionary.get('forAllValues')
        for_any_value = dictionary.get('forAnyValue')
        if_exists = dictionary.get('ifExists')

        # Return an object of this model
        return cls(
            cond_operator,
            condition_key_values_map,
            for_all_values,
            for_any_value,
            if_exists
)