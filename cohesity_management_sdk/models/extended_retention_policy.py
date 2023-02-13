# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.data_lock_config

class ExtendedRetentionPolicy(object):

    """Implementation of the 'ExtendedRetentionPolicy' model.

    Specifies additional retention policies to apply to backup snapshots.

    Attributes:
        id (string): Specified the Id for a snapshot copy policy. This is
            generated when the policy is created.
        backup_run_type (BackupRunTypeEnum): The backup run type to which this
            extended retention applies to. If this is not set, the extended
            retention will be applicable to all non-log backup types.
            Currently, the only value that can be set here is kFull.
            'kRegular' indicates a incremental (CBT) backup. Incremental
            backups utilizing CBT (if supported) are captured of the target
            protection objects. The first run of a kRegular schedule captures
            all the blocks. 'kFull' indicates a full (no CBT) backup. A
            complete backup (all blocks) of the target protection objects are
            always captured and Change Block Tracking (CBT) is not utilized.
            'kLog' indicates a Database Log backup. Capture the database
            transaction logs to allow rolling back to a specific point in
            time. 'kSystem' indicates a system backup. System backups are used
            to do bare metal recovery of the system to a specific point in
            time.
        data_lock_config (DatalockConfig): Specifies WORM retention type for
            snapshots under extended retention.
        days_to_keep (long|int): Specifies the number of days to retain copied
            Snapshots on the target.
        multiplier (int): Specifies a factor to multiply the periodicity by,
            to determine the copy schedule. For example if set to 2 and the
            periodicity is hourly, then Snapshots from the first eligible Job
            Run for every 2 hour period is copied.
        periodicity (PeriodicityExtendedRetentionPolicyEnum): Specifies the
            frequency that Snapshots should be copied to the specified target.
            Used in combination with multipiler. 'kEvery' means that the
            Snapshot copy occurs after the number of Job Runs equals the
            number specified in the multiplier. 'kHour' means that the
            Snapshot copy occurs hourly at the frequency set in the
            multiplier, for example if multiplier is 2, the copy occurs every
            2 hours. 'kDay' means that the Snapshot copy occurs daily at the
            frequency set in the multiplier. 'kWeek' means that the Snapshot
            copy occurs weekly at the frequency set in the multiplier.
            'kMonth' means that the Snapshot copy occurs monthly at the
            frequency set in the multiplier. 'kYear' means that the Snapshot
            copy occurs yearly at the frequency set in the multiplier.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'Id',
        "backup_run_type":'backupRunType',
        "data_lock_config":'dataLockConfig',
        "days_to_keep":'daysToKeep',
        "multiplier":'multiplier',
        "periodicity":'periodicity'
    }

    def __init__(self,
                 id=None,
                 backup_run_type=None,
                 data_lock_config=None,
                 days_to_keep=None,
                 multiplier=None,
                 periodicity=None):
        """Constructor for the ExtendedRetentionPolicy class"""

        # Initialize members of the class
        self.id = id
        self.backup_run_type = backup_run_type
        self.data_lock_config = data_lock_config
        self.days_to_keep = days_to_keep
        self.multiplier = multiplier
        self.periodicity = periodicity


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
        id = dictionary.get('Id')
        backup_run_type = dictionary.get('backupRunType')
        data_lock_config = cohesity_management_sdk.models.data_lock_config.DataLockConfig.from_dictionary(dictionary.get('dataLockConfig')) if dictionary.get('dataLockConfig') else None
        days_to_keep = dictionary.get('daysToKeep')
        multiplier = dictionary.get('multiplier')
        periodicity = dictionary.get('periodicity')

        # Return an object of this model
        return cls(id,
                   backup_run_type,
                   data_lock_config,
                   days_to_keep,
                   multiplier,
                   periodicity)


