# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class FileLevelDataLockConfig(object):

    """Implementation of the 'FileLevelDataLockConfig' model.

    Specifies a config to lock files in a view - to protect from malicious or
    an accidental attempt to delete or modify the files in this view.

    Attributes:
        auto_lock_after_duration_idle (int): Specifies the duration to lock a
            file that has not been accessed or modified (ie. has been idle)
            for a certain duration of time in milliseconds. Do not set if it
            is required to disable auto lock.
        default_file_retention_duration_msecs (long|int): Specifies a global
            default retention duration for files in this view, if file lock is
            enabled for this view. Also, it is a required field if file lock
            is enabled. Set to -1 if the required default retention period is
            forever.
        expiry_timestamp_msecs (int): Specifies a definite timestamp in
            milliseconds for retaining the file.
        locking_protocol (LockingProtocolEnum): Specifies the supported
            mechanisms to explicity lock a file from NFS/SMB interface.
            Supported locking protocols: kSetReadOnly, kSetAtime.
            'kSetReadOnly' is compatible with Isilon/Netapp behaviour. This
            locks the file and the retention duration is determined in this
            order: 1) atime, if set by user/application and within min and max
            retention duration. 2) Min retention duration, if set. 3)
            Otherwise, file is switched to expired data automatically.
            'kSetAtime' is compatible with Data Domain behaviour.
        max_retention_duration_msecs (long|int): Specifies a maximum duration
            in milliseconds for which any file in this view can be retained
            for. Set to -1 if the required retention duration is forever. If
            set, it should be greater than or equal to the default retention
            period as well as the min retention period.
        min_retention_duration_msecs (long|int): Specifies a minimum retention
            duration in milliseconds after a file gets locked. The file cannot
            be modified or deleted during this timeframe. Set to -1 if the
            required retention duration is forever. This should be set less
            than or equal to the default retention duration.
        mode (ModeFileLevelDataLockConfigEnum): Specifies the mode of file
            level datalock. Enterprise mode can be upgraded to Compliance
            mode, but Compliance mode cannot be downgraded to Enterprise mode,
            unless view's FileLevelDataLockConfig has coexisting_lock_mode set.
            kCompliance: This mode would disallow all user to delete/modify
            file or view under any condition when it 's in locked status
            except for deleting view when the view is empty. kEnterprise: This
            mode would follow the rules as compliance mode for normal users.
            But it would allow the storage admin (1) to delete view or file
            anytime no matter it is in locked status or expired. (2) to rename
            the view (3) to bring back the retention period when it's in
            locked mode A lock mode of a file in a view can be in one of the
            following:  'kCompliance': Default mode of datalock, in this mode,
            Data Security Admin cannot modify/delete this view when datalock
            is in effect. Data Security Admin can delete this view when
            datalock is expired. 'kEnterprise' : In this mode, Data Security
            Admin can change view name or delete view when datalock is in
            effect. Datalock in this mode can be upgraded to 'kCompliance'
            mode.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "auto_lock_after_duration_idle":'autoLockAfterDurationIdle',
        "default_file_retention_duration_msecs":'defaultFileRetentionDurationMsecs',
        "expiry_timestamp_msecs":'expiryTimestampMsecs',
        "locking_protocol":'lockingProtocol',
        "max_retention_duration_msecs":'maxRetentionDurationMsecs',
        "min_retention_duration_msecs":'minRetentionDurationMsecs',
        "mode":'mode'
    }

    def __init__(self,
                 auto_lock_after_duration_idle=None,
                 default_file_retention_duration_msecs=None,
                 expiry_timestamp_msecs=None,
                 locking_protocol=None,
                 max_retention_duration_msecs=None,
                 min_retention_duration_msecs=None,
                 mode=None):
        """Constructor for the FileLevelDataLockConfig class"""

        # Initialize members of the class
        self.auto_lock_after_duration_idle = auto_lock_after_duration_idle
        self.default_file_retention_duration_msecs = default_file_retention_duration_msecs
        self.expiry_timestamp_msecs = expiry_timestamp_msecs
        self.locking_protocol = locking_protocol
        self.max_retention_duration_msecs = max_retention_duration_msecs
        self.min_retention_duration_msecs = min_retention_duration_msecs
        self.mode = mode


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
        auto_lock_after_duration_idle = dictionary.get('autoLockAfterDurationIdle')
        default_file_retention_duration_msecs = dictionary.get('defaultFileRetentionDurationMsecs')
        expiry_timestamp_msecs = dictionary.get('expiryTimestampMsecs')
        locking_protocol = dictionary.get('lockingProtocol')
        max_retention_duration_msecs = dictionary.get('maxRetentionDurationMsecs')
        min_retention_duration_msecs = dictionary.get('minRetentionDurationMsecs')
        mode = dictionary.get('mode')

        # Return an object of this model
        return cls(auto_lock_after_duration_idle,
                   default_file_retention_duration_msecs,
                   expiry_timestamp_msecs,
                   locking_protocol,
                   max_retention_duration_msecs,
                   min_retention_duration_msecs,
                   mode)


