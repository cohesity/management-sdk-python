# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class UserId(object):

    """Implementation of the 'UserId' model.

    Specifies the mapping between an Unix and an SMB SID.

    Attributes:
        sid (string): If interested in a user via smb_client, include SID.
            Otherwise, If valid unix-id to SID mappings are available (i.e.,
            when mixed mode is enabled) the server will perform the necessary
            id mapping and return the correct usage irrespective of whether
            the unix id / SID is provided. The string is of following format -
            S-1-IdentifierAuthority-SubAuthority1-SubAuthority2-...-SubAuthorit
            yn.
        unix_uid (int): If interested in a user via unix-identifier, include
            UnixUid. Otherwise, If valid unix-id to SID mappings are available
            (i.e., when mixed mode is enabled) the server will perform the
            necessary id mapping and return the correct usage irrespective of
            whether the unix id / SID is provided.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "sid":'sid',
        "unix_uid":'unixUid'
    }

    def __init__(self,
                 sid=None,
                 unix_uid=None):
        """Constructor for the UserId class"""

        # Initialize members of the class
        self.sid = sid
        self.unix_uid = unix_uid


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
        sid = dictionary.get('sid')
        unix_uid = dictionary.get('unixUid')

        # Return an object of this model
        return cls(sid,
                   unix_uid)


