# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class NfsSquash(object):

    """Implementation of the 'NfsSquash' model.

    TODO: type model description here.

    Attributes:
        gid (int): GID mapped for all clients.
        uid (int): UID mapped for all clients.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "gid":'gid',
        "uid":'uid'
    }

    def __init__(self,
                 gid=None,
                 uid=None):
        """Constructor for the NfsSquash class"""

        # Initialize members of the class
        self.gid = gid
        self.uid = uid


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
        gid = dictionary.get('gid')
        uid = dictionary.get('uid')

        # Return an object of this model
        return cls(gid,
                   uid)


