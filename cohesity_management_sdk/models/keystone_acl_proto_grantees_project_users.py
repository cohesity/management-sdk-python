# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class KeystoneACLProto_Grantees_ProjectUsers(object):

    """Implementation of the 'KeystoneACLProto_Grantees_ProjectUsers' model.

    Attributes:
        user_id_vec (list of string): TODO: Type description here.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "user_id_vec":'userIdVec'
    }

    def __init__(self,
                 user_id_vec=None):
        """Constructor for the KeystoneACLProto_Grantees_ProjectUsers class"""

        # Initialize members of the class
        self.user_id_vec = user_id_vec


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
        user_id_vec = dictionary.get('userIdVec')

        # Return an object of this model
        return cls(user_id_vec)


