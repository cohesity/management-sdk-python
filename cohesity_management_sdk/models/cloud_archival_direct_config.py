# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.quota_policy

class CloudArchivalDirectConfig(object):

    """Implementation of the 'CloudArchivalDirectConfig' model.

    CloudArchivalDirectConfig specifies the properties of vaults used to
    perform Cloud Archive Direct (CAD)

    Attributes:
        bucket_namesapce (string): Specifies a namespace under the bucket used
            for archival.
        physical_quota (QuotaPolicy): Specifies quota limit in bytes for
            physical usage associated with this vault during the first CAD
            job.


    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bucket_namesapce": 'bucketNamesapce',
        "physical_quota": 'physicalQuota'
    }

    def __init__(self,
                 bucket_namesapce=None,
                 physical_quota=None):
        """Constructor for the CloudArchivalDirectConfig class"""

        # Initialize members of the class
        self.bucket_namesapce = bucket_namesapce
        self.physical_quota = physical_quota


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
        bucket_namesapce = dictionary.get('bucketNamesapce')
        physical_quota = cohesity_management_sdk.models.quota_policy.QuotaPolicy.from_dictionary(dictionary.get('physicalQuota')) if dictionary.get('physicalQuota') else None

        # Return an object of this model
        return cls(bucket_namesapce,
                   physical_quota)


