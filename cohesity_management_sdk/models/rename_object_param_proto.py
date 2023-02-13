# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class RenameObjectParamProto(object):

    """Implementation of the 'RenameObjectParamProto' model.

    Message to specify the prefix/suffix added to rename an object. At least
    one
    of prefix or suffix must be specified. Please note that both prefix and
    suffix can be specified.

    Attributes:
        prefix (string): Prefix to be added to a name.
        suffix (string): Suffix to be added to a name.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "prefix":'prefix',
        "suffix":'suffix'
    }

    def __init__(self,
                 prefix=None,
                 suffix=None):
        """Constructor for the RenameObjectParamProto class"""

        # Initialize members of the class
        self.prefix = prefix
        self.suffix = suffix


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
        prefix = dictionary.get('prefix')
        suffix = dictionary.get('suffix')

        # Return an object of this model
        return cls(prefix,
                   suffix)


