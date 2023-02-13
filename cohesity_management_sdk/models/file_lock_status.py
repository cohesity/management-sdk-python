# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class FileLockStatus(object):

    """Implementation of the 'FileLockStatus' model.

    Specifies the information of lock status for a file.

    Attributes:
        expiry_timestamp_msecs (long|int): Specifies a expiry timestamp in
            milliseconds until the file is locked.
        hold_timestamp_msecs (long|int): Specifies a override timestamp in
            milliseconds when an expired file is kept on hold.
        lock_timestamp_msecs (long|int): Specifies the timestamp at which the
            file was locked.
        mode (ModeFileLockStatusEnum): Specifies the mode of the file lock.
            'kCompliance', 'kEnterprise'. A lock mode of a file in a view can
            be in one of the following:  'kCompliance': Default mode of
            datalock, in this mode, Data Security Admin cannot modify/delete
            this view when datalock is in effect. Data Security Admin can
            delete this view when datalock is expired. 'kEnterprise' : In this
            mode, Data Security Admin can change view name or delete view when
            datalock is in effect. Datalock in this mode can be upgraded to
            'kCompliance' mode.
        state (int): Specifies the lock state of the file.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "expiry_timestamp_msecs":'expiryTimestampMsecs',
        "hold_timestamp_msecs":'holdTimestampMsecs',
        "lock_timestamp_msecs":'lockTimestampMsecs',
        "mode":'mode',
        "state":'state'
    }

    def __init__(self,
                 expiry_timestamp_msecs=None,
                 hold_timestamp_msecs=None,
                 lock_timestamp_msecs=None,
                 mode=None,
                 state=None):
        """Constructor for the FileLockStatus class"""

        # Initialize members of the class
        self.expiry_timestamp_msecs = expiry_timestamp_msecs
        self.hold_timestamp_msecs = hold_timestamp_msecs
        self.lock_timestamp_msecs = lock_timestamp_msecs
        self.mode = mode
        self.state = state


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
        expiry_timestamp_msecs = dictionary.get('expiryTimestampMsecs')
        hold_timestamp_msecs = dictionary.get('holdTimestampMsecs')
        lock_timestamp_msecs = dictionary.get('lockTimestampMsecs')
        mode = dictionary.get('mode')
        state = dictionary.get('state')

        # Return an object of this model
        return cls(expiry_timestamp_msecs,
                   hold_timestamp_msecs,
                   lock_timestamp_msecs,
                   mode,
                   state)


