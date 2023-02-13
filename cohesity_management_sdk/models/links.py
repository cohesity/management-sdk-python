# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class Links(object):

    """Implementation of the 'Links' model.

    The links proto to a specific resource. For example, resource, can be
    domain, endpoint or service.

    Attributes:
        next (string): TODO: Type description here.
        previous (string): TODO: Type description here.
        mself (string): TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "next":'next',
        "previous":'previous',
        "mself":'self'
    }

    def __init__(self,
                 next=None,
                 previous=None,
                 mself=None):
        """Constructor for the Links class"""

        # Initialize members of the class
        self.next = next
        self.previous = previous
        self.mself = mself


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
        next = dictionary.get('next')
        previous = dictionary.get('previous')
        mself = dictionary.get('self')

        # Return an object of this model
        return cls(next,
                   previous,
                   mself)


