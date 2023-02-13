# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ProtectionSummary(object):

    """Implementation of the 'ProtectionSummary' model.

    Specifies the number of protected and unprotected
    objects, and their sizes information of the given entity.

    Attributes:
        protected_count (long|int): Specifies the number of objects that are
            protected under the given entity.
        protected_size (long|int): Specifies the total size of the protected
            objects under the given entity.
        unprotected_count (long|int): Specifies the number of objects that are
            not protected under the given entity.
        unprotected_size (long|int): Specifies the total size of the
            unprotected objects under the given entity.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "protected_count":'protectedCount',
        "protected_size":'protectedSize',
        "unprotected_count":'unprotectedCount',
        "unprotected_size":'unprotectedSize'
    }

    def __init__(self,
                 protected_count=None,
                 protected_size=None,
                 unprotected_count=None,
                 unprotected_size=None):
        """Constructor for the ProtectionSummary class"""

        # Initialize members of the class
        self.protected_count = protected_count
        self.protected_size = protected_size
        self.unprotected_count = unprotected_count
        self.unprotected_size = unprotected_size


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
        protected_count = dictionary.get('protectedCount')
        protected_size = dictionary.get('protectedSize')
        unprotected_count = dictionary.get('unprotectedCount')
        unprotected_size = dictionary.get('unprotectedSize')

        # Return an object of this model
        return cls(protected_count,
                   protected_size,
                   unprotected_count,
                   unprotected_size)


