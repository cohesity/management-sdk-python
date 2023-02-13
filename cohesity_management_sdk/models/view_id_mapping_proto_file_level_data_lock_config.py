# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


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
        coexisting_lock_mode (bool): If set, inodes in the view can be locked
            in different modes
            (Compliance/Enterprise) independently. The locking mode is stored
            explicitly on each inode. The mode field on inode
            FileLevelDataLockMetadata identifies the lock mode for the individual
            inode, whereas the mode field in view FileLevelDataLockConfig denotes
            the default lock mode for implicit locking. The field can be set only at
            view fld enable time and is immutable later.
            Also if this is set, the view can be deleted only if it does not
            have any inode.
        default_retention_duration_usecs (long|int): Default retention
            duration is used when an explicit retention timestamp is not set
            by user/application when locking a file. If the administrator does
            not want to enforce this, this field must not be set. If file
            requires being retained forever by default, this must be set to
            INT64_MAX. If minimum and maximum retention are enforced, then
            this must be always between these two durations.
        default_retention_duration_years (long|int): Default retention duration
            in years. Follows the same conditions specified for
            default_retention_duration_usecs.
        hold_timestamp_usecs (long|int): Specifies timestamp to protect
            locked files until a specific date. This would override retention
            periods and deny any mutable or remove operations on locked files
            until a specific date.
        ignore_existing_files (bool): If set, implicit locking will be applied
            only to the newly created or updated inodes.
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
        "coexisting_lock_mode":'coexistingLockMode',
        "default_retention_duration_usecs": 'defaultRetentionDurationUsecs',
        "default_retention_duration_years":'defaultRetentionDurationYears',
        "hold_timestamp_usecs": 'holdTimestampUsecs',
        "ignore_existing_files":'ignoreExistingFiles',
        "max_retention_duration_usecs": 'maxRetentionDurationUsecs',
        "min_retention_duration_usecs":'minRetentionDurationUsecs',
        "mode":'mode',
        "protocol":'protocol'
    }

    def __init__(self,
                 auto_lock_duration_usecs=None,
                 coexisting_lock_mode=None,
                 default_retention_duration_usecs=None,
                 default_retention_duration_years=None,
                 hold_timestamp_usecs=None,
                 ignore_existing_files=None,
                 max_retention_duration_usecs=None,
                 min_retention_duration_usecs=None,
                 mode=None,
                 protocol=None):
        """Constructor for the ViewIdMappingProto_FileLevelDataLockConfig class"""

        # Initialize members of the class
        self.auto_lock_duration_usecs = auto_lock_duration_usecs
        self.coexisting_lock_mode = coexisting_lock_mode
        self.default_retention_duration_usecs = default_retention_duration_usecs
        self.default_retention_duration_years = default_retention_duration_years
        self.hold_timestamp_usecs = hold_timestamp_usecs
        self.ignore_existing_files = ignore_existing_files
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
        coexisting_lock_mode = dictionary.get('coexistingLockMode')
        default_retention_duration_usecs = dictionary.get('defaultRetentionDurationUsecs')
        default_retention_duration_years = dictionary.get('defaultRetentionDurationYears')
        hold_timestamp_usecs = dictionary.get('holdTimestampUsecs')
        ignore_existing_files = dictionary.get('ignoreExistingFiles')
        max_retention_duration_usecs = dictionary.get('maxRetentionDurationUsecs')
        min_retention_duration_usecs = dictionary.get('minRetentionDurationUsecs')
        mode = dictionary.get('mode')
        protocol = dictionary.get('protocol')

        # Return an object of this model
        return cls(auto_lock_duration_usecs,
                   coexisting_lock_mode,
                   default_retention_duration_usecs,
                   default_retention_duration_years,
                   hold_timestamp_usecs,
                   ignore_existing_files,
                   max_retention_duration_usecs,
                   min_retention_duration_usecs,
                   mode,
                   protocol)


