# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ValueData(object):

    """Implementation of the 'Value_Data' model.

    Specifies the fields to store data of a given type.
    Specify data in the appropriate field for the current data type.

    Attributes:
        bytes_value (list of int): Specifies the field to store an array of
            bytes if the current data type is bytes. Specify a value for this
            field when type is equal to 4.
        double_value (float): Specifies the field to store data if the current
            data type is a double value. Specify a value for this field when
            type is equal to 2.
        int_64_value (long|int): Specifies the field to store data if the
            current data type is a int64 value. Specify a value for this field
            when type is equal to 1.
        string_value (string): Specifies the field to store data if the
            current data type is a string value. Specify a value for this
            field when type is equal to 3.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bytes_value":'bytesValue',
        "double_value":'doubleValue',
        "int_64_value":'int64Value',
        "string_value":'stringValue'
    }

    def __init__(self,
                 bytes_value=None,
                 double_value=None,
                 int_64_value=None,
                 string_value=None):
        """Constructor for the ValueData class"""

        # Initialize members of the class
        self.bytes_value = bytes_value
        self.double_value = double_value
        self.int_64_value = int_64_value
        self.string_value = string_value


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
        bytes_value = dictionary.get('bytesValue')
        double_value = dictionary.get('doubleValue')
        int_64_value = dictionary.get('int64Value')
        string_value = dictionary.get('stringValue')

        # Return an object of this model
        return cls(bytes_value,
                   double_value,
                   int_64_value,
                   string_value)


