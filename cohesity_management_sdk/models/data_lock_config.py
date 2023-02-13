# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class DataLockConfig(object):

    """Implementation of the 'DataLockConfig' model.

    Specifies WORM retention type for the snapshots. When a WORM retention type
    is specified, the snapshots of the Protection Groups using this policy will
    be kept for the last N days as specified in the duration of the datalock.
    During that time, the snapshots cannot be deleted.

    Attributes:
        days_to_keep (long|int): Specifies last N days to keep Snapshots under
            datalock in a protection group.
        worm_retention_type (WormRetentionTypeEnum): Specifies WORM retention
            type for the snapshots. When a WORM retention
            type is specified, the snapshots of the Protection Jobs using this policy
            will be kept until the maximum of the snapshot retention time. During
            that time, the snapshots cannot be deleted.
            'kNone' implies there is no WORM retention set.
            'kCompliance' implies WORM retention is set for compliance reason.
            'kAdministrative' implies WORM retention is set for administrative
            purposes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "days_to_keep": 'daysToKeep',
        "worm_retention_type": 'wormRetentionType'
    }

    def __init__(self,
                 days_to_keep=None,
                 worm_retention_type=None):
        """Constructor for the DataLockConfig class"""

        # Initialize members of the class
        self.days_to_keep = days_to_keep
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
        days_to_keep = dictionary.get('daysToKeep', None)
        worm_retention_type = dictionary.get('wormRetentionType', None)

        # Return an object of this model
        return cls(days_to_keep,
                   worm_retention_type)


