# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class GranteeProto(object):

    """Implementation of the 'GranteeProto' model.

    Message to define a grantee to which ACL permissions can be granted.

    Attributes:
        email_address (string): If grantee is of type 'kEmailUser', this
            field will contain the email address of the user.
        group (int): If grantee is of type 'kGroup', this field will contain
            the group to which permission is granted.
        mtype (int): TODO: Type description here.
        user_id (string): If grantee is of type 'kRegisteredUser', this field
            will contain the canonical id of the user.


    """

    # Create a mapping from Model property names to API property names
    _names = {
        "email_address":'emailAddress',
        "group":'group',
        "mtype":'type',
        "user_id":'userId'
    }

    def __init__(self,
                 email_address=None,
                 group=None,
                 mtype=None,
                 user_id=None):
        """Constructor for the GranteeProto class"""

        # Initialize members of the class
        self.email_address = email_address
        self.group = group
        self.mtype = mtype
        self.user_id = user_id


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
        email_address = dictionary.get('emailAddress')
        group = dictionary.get('group')
        mtype = dictionary.get('type')
        user_id = dictionary.get('userId')

        # Return an object of this model
        return cls(email_address,
                   group,
                   mtype,
                   user_id)


