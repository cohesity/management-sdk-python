# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class TaskAttribute(object):

    """Implementation of the 'TaskAttribute' model.

    This contains a string name, a value, and a type for the value.

    Attributes:
        name (string): Specifies the name of this Task Attribute.
        value (string): Specifies the value of this Task Attribute.
        value_type (ValueTypeEnum): Specifies the type of the value contained
            here. All values are returned as pointers to strings, but they can
            be casted to the type indicated here. 'kInt64' indicates that the
            value stored in the Task Attribute is a 64-bit integer. 'kDouble'
            indicates that the value stored in the Task Attribute is a 64 bit
            floating point number. 'kString' indicates that the value stored
            in the Task Attribute is a string. 'kBytes' indicates that the
            value stored in the Task Attribute is an array of bytes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "value":'value',
        "value_type":'valueType'
    }

    def __init__(self,
                 name=None,
                 value=None,
                 value_type=None):
        """Constructor for the TaskAttribute class"""

        # Initialize members of the class
        self.name = name
        self.value = value
        self.value_type = value_type


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
        name = dictionary.get('name')
        value = dictionary.get('value')
        value_type = dictionary.get('valueType')

        # Return an object of this model
        return cls(name,
                   value,
                   value_type)


