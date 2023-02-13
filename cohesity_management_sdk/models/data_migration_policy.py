# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.scheduling_policy

class DataMigrationPolicy(object):

    """Implementation of the 'DataMigrationPolicy' model.

    Specifies settings for data migration in NAS environment. This also
    specifies the retention policy that should be applied to files after they
    have been moved to cohesity cluster.

    Attributes:
        days_to_keep (long|int): Specifies how many days to retain Snapshots
            on the Cohesity Cluster.
        scheduling_policy (SchedulingPolicy): Specifies settings that define a
            backup schedule for a Protection Job.
        worm_retention_type (WormRetentionTypeDataMigrationPolicyEnum):
            Specifies WORM retention type for the files. When a WORM retention
            type is specified, the files will be kept until the maximum of the
            retention time. During that time, the files cannot be deleted.
            'kNone' implies there is no WORM retention set. 'kCompliance'
            implies WORM retention is set for compliance reason.
            'kAdministrative' implies WORM retention is set for administrative
            purposes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "days_to_keep":'daysToKeep',
        "scheduling_policy":'schedulingPolicy',
        "worm_retention_type":'wormRetentionType'
    }

    def __init__(self,
                 days_to_keep=None,
                 scheduling_policy=None,
                 worm_retention_type=None):
        """Constructor for the DataMigrationPolicy class"""

        # Initialize members of the class
        self.days_to_keep = days_to_keep
        self.scheduling_policy = scheduling_policy
        self.worm_retention_type = worm_retention_type


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
        days_to_keep = dictionary.get('daysToKeep')
        scheduling_policy = cohesity_management_sdk.models.scheduling_policy.SchedulingPolicy.from_dictionary(dictionary.get('schedulingPolicy')) if dictionary.get('schedulingPolicy') else None
        worm_retention_type = dictionary.get('wormRetentionType')

        # Return an object of this model
        return cls(days_to_keep,
                   scheduling_policy,
                   worm_retention_type)


