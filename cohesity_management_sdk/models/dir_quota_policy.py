# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.quota_policy


class DirQuotaPolicy(object):

    """Implementation of the 'DirQuotaPolicy' model.

    Specifies a policy configuration for the directory quota. A policy is the
    sole entity which describes the usage limits of a directory in a view. 
    `DirPath` is the identifier of a policy. It must be specified for adding,
    updating or removing a policy. If `Policy` is not set, then it is
    considered to be removed.


    Attributes:

        dir_path (string): Specifies the path of the directory in the view.
        dir_walk_pending (bool): Denotes directory quota walk is pending or
            not.
        policy (QuotaPolicy): Specifies the quota policy to be applied to the
            directory.
        usage_bytes (long|int): Specifies the current usage (in bytes) by the
            directory in the view. This is set by the response received from
            bridge when querying directory quota usage.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "dir_path":'dirPath',
        "dir_walk_pending":'dirWalkPending',
        "policy":'policy',
        "usage_bytes":'usageBytes',
    }
    def __init__(self,
                 dir_path=None,
                 dir_walk_pending=None,
                 policy=None,
                 usage_bytes=None,
            ):

        """Constructor for the DirQuotaPolicy class"""

        # Initialize members of the class
        self.dir_path = dir_path
        self.dir_walk_pending = dir_walk_pending
        self.policy = policy
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
        dir_path = dictionary.get('dirPath')
        dir_walk_pending = dictionary.get('dirWalkPending')
        policy = cohesity_management_sdk.models.quota_policy.QuotaPolicy.from_dictionary(dictionary.get('policy')) if dictionary.get('policy') else None
        usage_bytes = dictionary.get('usageBytes')

        # Return an object of this model
        return cls(
            dir_path,
            dir_walk_pending,
            policy,
            usage_bytes
)