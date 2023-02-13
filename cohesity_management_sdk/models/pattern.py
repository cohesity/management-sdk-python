# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class Pattern(object):

    """Implementation of the 'Pattern' model.

    TODO: type model description here.

    Attributes:
        is_system_defined (bool): Whether this pattern is system defined.
        name (string): Name of the pattern. This is marked optional but is
            required.
        mtype (int): Pattern type.
        value (string): Value of the pattern. This is marked optional but is
            required.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "is_system_defined":'isSystemDefined',
        "name":'name',
        "mtype":'type',
        "value":'value'
    }

    def __init__(self,
                 is_system_defined=None,
                 name=None,
                 mtype=None,
                 value=None):
        """Constructor for the Pattern class"""

        # Initialize members of the class
        self.is_system_defined = is_system_defined
        self.name = name
        self.mtype = mtype
        self.value = value


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
        is_system_defined = dictionary.get('isSystemDefined')
        name = dictionary.get('name')
        mtype = dictionary.get('type')
        value = dictionary.get('value')

        # Return an object of this model
        return cls(is_system_defined,
                   name,
                   mtype,
                   value)


