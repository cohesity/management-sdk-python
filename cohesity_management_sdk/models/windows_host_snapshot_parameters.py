# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class WindowsHostSnapshotParameters(object):

    """Implementation of the 'WindowsHostSnapshotParameters' model.

    Specifies settings that are meaningful only on Windows hosts.

    Attributes:
        copy_only_backup (bool): Specifies whether to backup regardless of the
            state of each file's backup history. Backup history will not be
            updated. Refer Microsoft documentation on VSS_BT_COPY.
        disable_metadata (bool): Specifies whether to disable fetching and
            storing of some metadata on Cohesity Cluster to save storage
            space. Otherwise, there will be some metadata fetched and stored
            on Cohesity Cluster.
        disable_notification (bool): Specifies whether to disable some
            notification steps when taking snapshots.
        excluded_vss_writers (list of string): Specifies a list of Windows VSS
            writers that are excluded from backups. For example, "ASR Writer",
            "System Writer". Refer Microsoft documentaion for a complete
            list.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "copy_only_backup":'copyOnlyBackup',
        "disable_metadata":'disableMetadata',
        "disable_notification":'disableNotification',
        "excluded_vss_writers":'excludedVssWriters'
    }

    def __init__(self,
                 copy_only_backup=None,
                 disable_metadata=None,
                 disable_notification=None,
                 excluded_vss_writers=None):
        """Constructor for the WindowsHostSnapshotParameters class"""

        # Initialize members of the class
        self.copy_only_backup = copy_only_backup
        self.disable_metadata = disable_metadata
        self.disable_notification = disable_notification
        self.excluded_vss_writers = excluded_vss_writers


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
        copy_only_backup = dictionary.get('copyOnlyBackup')
        disable_metadata = dictionary.get('disableMetadata')
        disable_notification = dictionary.get('disableNotification')
        excluded_vss_writers = dictionary.get('excludedVssWriters')

        # Return an object of this model
        return cls(copy_only_backup,
                   disable_metadata,
                   disable_notification,
                   excluded_vss_writers)


