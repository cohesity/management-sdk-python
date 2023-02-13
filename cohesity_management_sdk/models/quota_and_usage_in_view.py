# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.quota_policy

class QuotaAndUsageInView(object):

    """Implementation of the 'QuotaAndUsageInView' model.

    Specifies the usage and quota information for a specific view.

    Attributes:
        quota (QuotaPolicy): Specifies a quota limit that can be optionally
            applied to Views and View Boxes. At the View level, this quota
            defines a logical limit for usage on the View. At the View Box
            level, this quota defines a physical limit or a default logical
            View limit. If a physical quota is specified for View Box, this
            quota defines a physical limit for the usage on the View Box. If a
            default logical View quota is specified for View Box, this limit
            is inherited by all the Views in that View Box. However, this
            inherited quota can be overwritten at the View level. A new write
            is not allowed if the resource will exceed the specified quota.
            However, it takes time for the Cohesity Cluster to calculate the
            usage across Nodes, so the limit may be exceeded by a small
            amount. In addition, if the limit is increased or data is removed,
            there may be a delay before the Cohesity Cluster allows more data
            to be written to the resource, as the Cluster calculates the usage
            across Nodes.
        usage_bytes (long|int): Usage in bytes of this user in this view.
        view_id (long|int): The usage and quota policy information of this
            user for this view.
        view_name (string): View name.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "quota":'quota',
        "usage_bytes":'usageBytes',
        "view_id":'viewId',
        "view_name":'viewName'
    }

    def __init__(self,
                 quota=None,
                 usage_bytes=None,
                 view_id=None,
                 view_name=None):
        """Constructor for the QuotaAndUsageInView class"""

        # Initialize members of the class
        self.quota = quota
        self.usage_bytes = usage_bytes
        self.view_id = view_id
        self.view_name = view_name


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
        quota = cohesity_management_sdk.models.quota_policy.QuotaPolicy.from_dictionary(dictionary.get('quota')) if dictionary.get('quota') else None
        usage_bytes = dictionary.get('usageBytes')
        view_id = dictionary.get('viewId')
        view_name = dictionary.get('viewName')

        # Return an object of this model
        return cls(quota,
                   usage_bytes,
                   view_id,
                   view_name)


