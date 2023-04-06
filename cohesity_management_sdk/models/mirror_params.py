# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class MirrorParams(object):

    """Implementation of the 'MirrorParams' model.

    TODO: type description here.


    Attributes:

        finalized (bool): TODO: Type description here.
        paused (bool): Is mirroring paused.
        previous_view_name (string): View to be used as previous view.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "finalized":'finalized',
        "paused":'paused',
        "previous_view_name":'previousViewName',
    }
    def __init__(self,
                 finalized=None,
                 paused=None,
                 previous_view_name=None,
            ):

        """Constructor for the MirrorParams class"""

        # Initialize members of the class
        self.finalized = finalized
        self.paused = paused
        self.previous_view_name = previous_view_name

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
        finalized = dictionary.get('finalized')
        paused = dictionary.get('paused')
        previous_view_name = dictionary.get('previousViewName')

        # Return an object of this model
        return cls(
            finalized,
            paused,
            previous_view_name
)