# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class CommonACLProto_Grantees(object):

    """Implementation of the 'CommonACLProto_Grantees' model.

    Attributes:
        all_users (bool): This field indicates if all users are granted ACL
            permission.
        denied_referrer_vec (list of string): This field holds a list of
            referers who are denied ACL permission.
        granted_referrer_vec (list of string): This field holds a list of
            referers who are granted ACL permission.
        rlistings (bool): This fields indicates if container GET and HEAD
            operations are permitted provided that read access is granted
            (using referer ACL) on objects.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "all_users":'allUsers',
        "denied_referrer_vec":'deniedReferrerVec',
        "granted_referrer_vec":'grantedReferrerVec',
        "rlistings":'rlistings'
    }

    def __init__(self,
                 all_users=None,
                 denied_referrer_vec=None,
                 granted_referrer_vec=None,
                 rlistings=None):
        """Constructor for the CommonACLProto_Grantees class"""

        # Initialize members of the class
        self.all_users = all_users
        self.denied_referrer_vec = denied_referrer_vec
        self.granted_referrer_vec = granted_referrer_vec
        self.rlistings = rlistings


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
        all_users = dictionary.get('allUsers')
        denied_referrer_vec = dictionary.get('deniedReferrerVec')
        granted_referrer_vec = dictionary.get('grantedReferrerVec')
        rlistings = dictionary.get('rlistings')

        # Return an object of this model
        return cls(all_users,
                   denied_referrer_vec,
                   granted_referrer_vec,
                   rlistings)


