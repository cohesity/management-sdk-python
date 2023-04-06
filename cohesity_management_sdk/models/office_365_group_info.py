# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class Office365GroupInfo(object):

    """Implementation of the 'Office365GroupInfo' model.

    Specifies information about a M365 Group.


    Attributes:

        is_mail_enabled (bool): Specifies whether the Group is mail enabled.
            Mail enabled groups are used within Microsoft to distribute
            messages.
        is_security_enabled (bool): Specifies whether the Group is security
            enabled. Security enabled groups are used to grant access
            permissions to resources in Exchange and Active Directory.
        member_count (long|int): Specifies the count of members within the
            Group.
        visibility (string): Specifies the visibility of the Group.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "is_mail_enabled":'isMailEnabled',
        "is_security_enabled":'isSecurityEnabled',
        "member_count":'memberCount',
        "visibility":'visibility',
    }
    def __init__(self,
                 is_mail_enabled=None,
                 is_security_enabled=None,
                 member_count=None,
                 visibility=None,
            ):

        """Constructor for the Office365GroupInfo class"""

        # Initialize members of the class
        self.is_mail_enabled = is_mail_enabled
        self.is_security_enabled = is_security_enabled
        self.member_count = member_count
        self.visibility = visibility

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
        is_mail_enabled = dictionary.get('isMailEnabled')
        is_security_enabled = dictionary.get('isSecurityEnabled')
        member_count = dictionary.get('memberCount')
        visibility = dictionary.get('visibility')

        # Return an object of this model
        return cls(
            is_mail_enabled,
            is_security_enabled,
            member_count,
            visibility
)