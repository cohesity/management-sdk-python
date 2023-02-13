# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class AttributeValue(object):

    """Implementation of the 'AttributeValue' model.

    Represents the information about the values of attribute of the ADObject.

    Attributes:
        flags (list of FlagEnum): Specifies the flags related to the attribute
            values of the AD object. 'kError' indicates error in conversion of
            AD Object value to string. The value in the AdAttributValue
            contains the error message. 'kTruncated' indicates the multi
            valued attribute is truncated when value exceeded
            'truncate_multivalues' value specified in the request. 'kCSV'
            indicates content in 'values' is a comma separated value (CSV)
            format of a complex object.
        values (list of string): Specifies list of values for the attribute.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "flags":'flags',
        "values":'values'
    }

    def __init__(self,
                 flags=None,
                 values=None):
        """Constructor for the AttributeValue class"""

        # Initialize members of the class
        self.flags = flags
        self.values = values


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
        flags = dictionary.get('flags')
        values = dictionary.get('values')

        # Return an object of this model
        return cls(flags,
                   values)


