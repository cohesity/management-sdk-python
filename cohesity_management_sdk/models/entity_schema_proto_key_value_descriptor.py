# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class EntitySchemaProtoKeyValueDescriptor(object):

    """Implementation of the 'EntitySchemaProto_KeyValueDescriptor' model.

    Specifies a key/value pair.

    Attributes:
        key_name (string): Specifies the name of a key.
        value_type (int): Specifies the type of the value that is associated
            with the key. 0 specifies a value type of Int64. 1 specifies a
            value type of Double. 2 specifies a value type of String. 3
            specifies a value type of Bytes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "key_name":'keyName',
        "value_type":'valueType'
    }

    def __init__(self,
                 key_name=None,
                 value_type=None):
        """Constructor for the EntitySchemaProtoKeyValueDescriptor class"""

        # Initialize members of the class
        self.key_name = key_name
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
        key_name = dictionary.get('keyName')
        value_type = dictionary.get('valueType')

        # Return an object of this model
        return cls(key_name,
                   value_type)


