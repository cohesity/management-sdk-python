# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.quota_policy


class UserQuotaAndUsage(object):

    """Implementation of the 'UserQuotaAndUsage' model.

    Specifies the quota override and usage statistics for a particular user.


    Attributes:

        quota_policy (QuotaPolicy): User quota policy applied to this user.
        sid (string): If interested in a user via smb_client, include SID.
            Otherwise, If a valid unix-id to SID mappings are available (i.e.,
            when mixed mode is enabled) the server will perform the necessary
            id mapping and return the correct usage irrespective of whether the
            unix id / SID is provided. The string is of following format -
            S-1-IdentifierAuthority-SubAuthority1-SubAuthority2-...-SubAuthorityn.
        unix_uid (int): If interested in a user via unix-identifier, include
            UnixUid. Otherwise, If a valid unix-id to SID mappings are
            available (i.e., when mixed mode is enabled) the server will
            perform the necessary id mapping and return the correct usage
            irrespective of whether the unix id / SID is provided.
        usage_bytes (long|int): Current logical usage of user id in the input
            view.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "quota_policy":'quotaPolicy',
        "sid":'sid',
        "unix_uid":'unixUid',
        "usage_bytes":'usageBytes',
    }
    def __init__(self,
                 quota_policy=None,
                 sid=None,
                 unix_uid=None,
                 usage_bytes=None,
            ):

        """Constructor for the UserQuotaAndUsage class"""

        # Initialize members of the class
        self.quota_policy = quota_policy
        self.sid = sid
        self.unix_uid = unix_uid
        self.usage_bytes = usage_bytes

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
        quota_policy = cohesity_management_sdk.models.quota_policy.QuotaPolicy.from_dictionary(dictionary.get('quotaPolicy')) if dictionary.get('quotaPolicy') else None
        sid = dictionary.get('sid')
        unix_uid = dictionary.get('unixUid')
        usage_bytes = dictionary.get('usageBytes')

        # Return an object of this model
        return cls(
            quota_policy,
            sid,
            unix_uid,
            usage_bytes
)