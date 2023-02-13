# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class CompareADObjectsResultADAttributeValue(object):

    """Implementation of the 'CompareADObjectsResult_ADAttributeValue' model.

    TODO: type model description here.

    Attributes:
        value_flags (int): Object result flags of type ADAttributeValueFlags.
        value_vec (list of string): String representation of attribute value.
            For single valued property, only one value will be present here.
            For multi-valued properties such as group membership, this field
            will contain values that are in same order as contained in AD.
            Each AD attribute value will be converted to string. If this
            property is not set, then the property has null value.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "value_flags":'valueFlags',
        "value_vec":'valueVec'
    }

    def __init__(self,
                 value_flags=None,
                 value_vec=None):
        """Constructor for the CompareADObjectsResultADAttributeValue class"""

        # Initialize members of the class
        self.value_flags = value_flags
        self.value_vec = value_vec


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
        value_flags = dictionary.get('valueFlags')
        value_vec = dictionary.get('valueVec')

        # Return an object of this model
        return cls(value_flags,
                   value_vec)


