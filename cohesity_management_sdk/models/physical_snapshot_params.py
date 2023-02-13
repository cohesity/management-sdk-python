# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class PhysicalSnapshotParams(object):

    """Implementation of the 'PhysicalSnapshotParams' model.

    This message contains params that controls the snapshot process for a
    physical host.

    Attributes:
        fetch_snapshot_metadata_disabled (bool): Whether fetching and storing
            of snapshot metadata was disabled.
        notify_backup_complete_disabled (bool): Whether notify backup complete
            step was disabled.
        vss_copy_only_backup (bool): If copy_only_backup option is requrested
            at the time of the snapshot.
        vss_excluded_writers (list of string): List of VSS writers that were
            excluded.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "fetch_snapshot_metadata_disabled":'fetchSnapshotMetadataDisabled',
        "notify_backup_complete_disabled":'notifyBackupCompleteDisabled',
        "vss_copy_only_backup":'vssCopyOnlyBackup',
        "vss_excluded_writers":'vssExcludedWriters'
    }

    def __init__(self,
                 fetch_snapshot_metadata_disabled=None,
                 notify_backup_complete_disabled=None,
                 vss_copy_only_backup=None,
                 vss_excluded_writers=None):
        """Constructor for the PhysicalSnapshotParams class"""

        # Initialize members of the class
        self.fetch_snapshot_metadata_disabled = fetch_snapshot_metadata_disabled
        self.notify_backup_complete_disabled = notify_backup_complete_disabled
        self.vss_copy_only_backup = vss_copy_only_backup
        self.vss_excluded_writers = vss_excluded_writers


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
        fetch_snapshot_metadata_disabled = dictionary.get('fetchSnapshotMetadataDisabled')
        notify_backup_complete_disabled = dictionary.get('notifyBackupCompleteDisabled')
        vss_copy_only_backup = dictionary.get('vssCopyOnlyBackup')
        vss_excluded_writers = dictionary.get('vssExcludedWriters')

        # Return an object of this model
        return cls(fetch_snapshot_metadata_disabled,
                   notify_backup_complete_disabled,
                   vss_copy_only_backup,
                   vss_excluded_writers)


