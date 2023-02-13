# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ObjectSnapshotType(object):

    """Implementation of the 'ObjectSnapshotType' model.

    TODO: type model description here.

    Attributes:
        msg (string): This captures any additional message about the snapshot
            itself, e.g. if the app-consistent snapshot had to fallback to
            crash consistent, this will contain that.
        mtype (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "msg":'msg',
        "mtype":'type'
    }

    def __init__(self,
                 msg=None,
                 mtype=None):
        """Constructor for the ObjectSnapshotType class"""

        # Initialize members of the class
        self.msg = msg
        self.mtype = mtype


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
        msg = dictionary.get('msg')
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(msg,
                   mtype)


