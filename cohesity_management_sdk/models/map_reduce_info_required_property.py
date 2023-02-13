# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class MapReduceInfo_RequiredProperty(object):

    """Implementation of the 'MapReduceInfo_RequiredProperty' model.

    A required property represents a property that user must set before
    invoking a mapreduction instance. e.g., SimpleGrepMapper will require a
    property named searchPattern to be set.

    Attributes:
        default_value (string): Default Value of the property.
        description (string): Description of this property
        is_required (bool): Whether the property is required or optional.
        name (string): Name of the property.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "default_value":'defaultValue',
        "description":'description',
        "is_required":'isRequired',
        "name":'name'
    }

    def __init__(self,
                 default_value=None,
                 description=None,
                 is_required=None,
                 name=None):
        """Constructor for the MapReduceInfo_RequiredProperty class"""

        # Initialize members of the class
        self.default_value = default_value
        self.description = description
        self.is_required = is_required
        self.name = name


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
        default_value = dictionary.get('defaultValue')
        description = dictionary.get('description')
        is_required = dictionary.get('isRequired')
        name = dictionary.get('name')

        # Return an object of this model
        return cls(default_value,
                   description,
                   is_required,
                   name)


