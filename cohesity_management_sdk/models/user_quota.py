# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.quota_policy

class UserQuota(object):

    """Implementation of the 'UserQuota' model.

    Specifies the quota policy applied to a user.

    Attributes:
        quota_policy (QuotaPolicy): Specifies a quota limit that can be
            optionally applied to Views and View Boxes. At the View level,
            this quota defines a logical limit for usage on the View. At the
            View Box level, this quota defines a physical limit or a default
            logical View limit. If a physical quota is specified for View Box,
            this quota defines a physical limit for the usage on the View Box.
            If a default logical View quota is specified for View Box, this
            limit is inherited by all the Views in that View Box. However,
            this inherited quota can be overwritten at the View level. A new
            write is not allowed if the resource will exceed the specified
            quota. However, it takes time for the Cohesity Cluster to
            calculate the usage across Nodes, so the limit may be exceeded by
            a small amount. In addition, if the limit is increased or data is
            removed, there may be a delay before the Cohesity Cluster allows
            more data to be written to the resource, as the Cluster calculates
            the usage across Nodes.
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
        "quota_policy":'quotaPolicy',
        "sid":'sid',
        "unix_uid":'unixUid'
    }

    def __init__(self,
                 quota_policy=None,
                 sid=None,
                 unix_uid=None):
        """Constructor for the UserQuota class"""

        # Initialize members of the class
        self.quota_policy = quota_policy
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
        quota_policy = cohesity_management_sdk.models.quota_policy.QuotaPolicy.from_dictionary(dictionary.get('quotaPolicy')) if dictionary.get('quotaPolicy') else None
        sid = dictionary.get('sid')
        unix_uid = dictionary.get('unixUid')

        # Return an object of this model
        return cls(quota_policy,
                   sid,
                   unix_uid)


