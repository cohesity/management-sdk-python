# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class LockRange(object):

    """Implementation of the 'LockRange' model.

    TODO: type model description here.

    Attributes:
        is_exclusive (bool): TODO: type description here.
        length (int): TODO: type description here.
        offset (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "is_exclusive":'isExclusive',
        "length":'length',
        "offset":'offset'
    }

    def __init__(self,
                 is_exclusive=None,
                 length=None,
                 offset=None):
        """Constructor for the LockRange class"""

        # Initialize members of the class
        self.is_exclusive = is_exclusive
        self.length = length
        self.offset = offset


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
        is_exclusive = dictionary.get('isExclusive')
        length = dictionary.get('length')
        offset = dictionary.get('offset')

        # Return an object of this model
        return cls(is_exclusive,
                   length,
                   offset)


