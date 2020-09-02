# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class ViewIdMappingProto_FileLevelDataLockConfig(object):

    """Implementation of the 'ViewIdMappingProto_FileLevelDataLockConfig' model.

    TODO: Type model description here.

    Attributes:
        auto_lock_duration_usecs (long|int): Auto-lock automatically commit
            files to WORM state in the filesystem if they have not been
            modified for an administrator-specified period of time. When the
            auto-lock is enabled, this field must be set to idle time duration
            after which file would be automatically locked. Auto locking will
            be disabled when configured with default value of -1.
        default_retention_duration_usecs (long|int): Default retention
            duration is used when an explicit retention timestamp is not set
            by user/application when locking a file. If the administrator does
            not want to enforce this, this field must not be set. If file
            requires being retained forever by default, this must be set to
            INT64_MAX. If minimum and maximum retention are enforced, then
            this must be always between these two durations.
        hold_timestamp_usecs (long|int): Specifies timestamp to protect
            locked files until a specific date. This would override retention
            periods and deny any mutable or remove operations on locked files
            until a specific date.
        max_retention_duration_usecs (long|int): Specifies maximum retention
            duration of worm locked file. If the administrator does not want
            to enforce this, this must not be set. If default and max
            retention duration are enforced, max retention duration must be
            greater than or equal to default retention duration. If min and
            max retention duration are enforced, max retention duration must
            be greater than and equal to min retention duration.
        min_retention_duration_usecs (long|int): Minimum and maximum retention
            duration allow the administrator to enforce retention duration
            that falls within a specified range. If the administrator does not
            want to enforce this, this must not be set. If the file requires
            being retained forever, this must be set to INT64_MAX. If default
            retention is enforced, this must be less than or equal to default
            retention. If max retention are enforced, default retention
            duration must be less than and equal to max retention duration.
        mode (int): Explicit locking mode.
        protocol (int): Explicit locking protocol.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "auto_lock_duration_usecs": 'autoLockDurationUsecs',
        "default_retention_duration_usecs": 'defaultRetentionDurationUsecs',
        "hold_timestamp_usecs": 'holdTimestampUsecs',
        "max_retention_duration_usecs": 'maxRetentionDurationUsecs',
        "min_retention_duration_usecs":'minRetentionDurationUsecs',
        "mode":'mode',
        "protocol":'protocol'
    }

    def __init__(self,
                 auto_lock_duration_usecs=None,
                 default_retention_duration_usecs=None,
                 hold_timestamp_usecs=None,
                 max_retention_duration_usecs=None,
                 min_retention_duration_usecs=None,
                 mode=None,
                 protocol=None):
        """Constructor for the ViewIdMappingProto_FileLevelDataLockConfig class"""

        # Initialize members of the class
        self.auto_lock_duration_usecs = auto_lock_duration_usecs
        self.default_retention_duration_usecs = default_retention_duration_usecs
        self.hold_timestamp_usecs = hold_timestamp_usecs
        self.max_retention_duration_usecs = max_retention_duration_usecs
        self.min_retention_duration_usecs = min_retention_duration_usecs
        self.mode = mode
        self.protocol = protocol

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
        auto_lock_duration_usecs = dictionary.get('autoLockDurationUsecs')
        default_retention_duration_usecs = dictionary.get('defaultRetentionDurationUsecs')
        hold_timestamp_usecs = dictionary.get('holdTimestampUsecs')
        max_retention_duration_usecs = dictionary.get('maxRetentionDurationUsecs')
        min_retention_duration_usecs = dictionary.get('minRetentionDurationUsecs')
        mode = dictionary.get('mode')
        protocol = dictionary.get('protocol')

        # Return an object of this model
        return cls(auto_lock_duration_usecs,
                   default_retention_duration_usecs,
                   hold_timestamp_usecs,
                   max_retention_duration_usecs,
                   min_retention_duration_usecs,
                   mode,
                   protocol)


