# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.file_path_filter

class DataMigrationJobParameters(object):

    """Implementation of the 'DataMigrationJobParameters' model.

    Specifies parameters applicable for data migration jobs in NAS
    environment.

    Attributes:
        cold_file_window (long|int): Identifies the cold files in the NAS
            source. Files that haven't been accessed/modified in the last
            cold_file_window are migrated.
        delete_orphan_data (bool): Delete migrated data if no symlink
            at source is pointing to it.
        file_path_filter (FilePathFilter): Specifies filters to match files
            and directories on a Server. Two kinds of filters are supported.
            a) prefix which always starts with '/'. b) posix which always
            starts with '*' (cannot be "*" only). Regular expressions are not
            supported. If a directory is matched, the action is applicable to
            all of its descendants. File paths not matching any protectFilters
            are not backed up.  An example is: Protect Filters: "/" Exclude
            Filters: "/tmp", "*.mp4" Using such a policy will include
            everything under the root directory except the /tmp directory and
            all the mp4 files.
        file_selection_policy (FileSelectionPolicyEnum): Specifies policy to
            select a file to migrate based on its creation, last access or
            modification time. eg. A file can be selected to migrate if it has
            not been accessed/modified in the ColdFileWindow. enum:
            kOlderThan, kLastAccessed, kLastModified. Specifies policy for
            file selection in data migration jobs based on time. 'kOlderThan':
            Migrate the files that are older than cold file window.
            'kLastAccessed': Migrate the files that are not accessed in cold
            file window. 'kLastModified': Migrate the files that have not been
            modified in cold file window.
        file_size_bytes (long|int): Gives the size criteria to be used for
            selecting the files to be migrated in bytes. The cold files that
            are equal and greater than this size are migrated.
        file_size_policy (FileSizePolicyEnum): Specifies policy to select a
            file to migrate based on its size. eg. A file can be selected to
            migrate if its size is greater than or smaller than the
            FileSizeBytes. enum: kGreaterThan, kSmallerThan. Specifies policy
            for file selection in data migration jobs based on file size.
            'kGreaterThan': Migrate the files whose size are greater than
            specified file size. 'kSmallerThan': Migrate the files whose size
            are smaller than specified file size.
        migrate_without_stub (bool): Specifies if data is to be migrated
            without stub.
        nfs_mount_path (string): Mount path where the target view must be
            mounted on all NFS clients for accessing the migrated data.
        target_view_name (string): The target view name to which the data will
            be migrated.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cold_file_window":'coldFileWindow',
        "delete_orphan_data":'deleteOrphanData',
        "file_path_filter":'filePathFilter',
        "file_selection_policy":'fileSelectionPolicy',
        "file_size_bytes":'fileSizeBytes',
        "file_size_policy":'fileSizePolicy',
        "migrate_without_stub":'migrateWithoutStub',
        "nfs_mount_path":'nfsMountPath',
        "target_view_name":'targetViewName'
    }

    def __init__(self,
                 cold_file_window=None,
                 delete_orphan_data=None,
                 file_path_filter=None,
                 file_selection_policy=None,
                 file_size_bytes=None,
                 file_size_policy=None,
                 migrate_without_stub=None,
                 nfs_mount_path=None,
                 target_view_name=None):
        """Constructor for the DataMigrationJobParameters class"""

        # Initialize members of the class
        self.cold_file_window = cold_file_window
        self.delete_orphan_data = delete_orphan_data
        self.file_path_filter = file_path_filter
        self.file_selection_policy = file_selection_policy
        self.file_size_bytes = file_size_bytes
        self.file_size_policy = file_size_policy
        self.migrate_without_stub = migrate_without_stub
        self.nfs_mount_path = nfs_mount_path
        self.target_view_name = target_view_name


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
        cold_file_window = dictionary.get('coldFileWindow')
        delete_orphan_data = dictionary.get('deleteOrphanData')
        file_path_filter = cohesity_management_sdk.models.file_path_filter.FilePathFilter.from_dictionary(dictionary.get('filePathFilter')) if dictionary.get('filePathFilter') else None
        file_selection_policy = dictionary.get('fileSelectionPolicy')
        file_size_bytes = dictionary.get('fileSizeBytes')
        file_size_policy = dictionary.get('fileSizePolicy')
        migrate_without_stub = dictionary.get('migrateWithoutStub', None)
        nfs_mount_path = dictionary.get('nfsMountPath')
        target_view_name = dictionary.get('targetViewName')

        # Return an object of this model
        return cls(cold_file_window,
                   delete_orphan_data,
                   file_path_filter,
                   file_selection_policy,
                   file_size_bytes,
                   file_size_policy,
                   migrate_without_stub,
                   nfs_mount_path,
                   target_view_name)


