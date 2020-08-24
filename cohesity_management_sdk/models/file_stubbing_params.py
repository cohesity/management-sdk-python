# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.filtering_policy_proto

class FileStubbingParams(object):

    """Implementation of the 'FileStubbingParams' model.

    File Stubbing Parameters
    Message to capture the additional stubbing params for a file-based
    environment.

    Attributes:
        cold_file_window (long|int): Identifies the cold files in the NAS
            source. Files that haven't been accessed/modified in the last
            cold_file_window msecs or are older than cold_window_msecs are
            migrated.
        delete_orphan_data (bool): Delete migrated data if no symlink at
            source is pointing to it.
        file_select_policy (int): File migrate policy based on file
            access/modify time and age.
        file_size (long|int): Gives the size criteria to be used for selecting
            the files to be migrated. The cold files that are equal and
            greater than file_size or smaller than file_size are migrated.
        file_size_policy (int): File size policy for selecting files to
            migrate.
        filtering_policy (FilteringPolicyProto): Proto to encapsulate the
            filtering policy for backup objects like files or directories. If
            an object is not matched by any of the 'allow_filters', it will be
            excluded in the backup. If an object is matched by one of the
            'deny_filters', it will always be excluded in the backup.
            Basically 'deny_filters' overwrite 'allow_filters' if they both
            match the same object. Currently we only support two kinds of
            filter: prefix which always starts with '/', or postfix which
            always starts with '*' (cannot be "*" only). We don't support
            regular expression right now. A concrete example is: Allow
            filters: "/" Deny filters: "/tmp", "*.mp4" Using such a policy
            will include everything under the root directory except the /tmp
            directory and all the mp4 files.
        migrate_without_stub (bool): Migrate data without stub.
        nfs_mount_path (string): Mount path where the Cohesity target view
            must be mounted on all NFS clients for accessing the migrated
            data.
        target_view_name (string): The target view name to which the data will
            be migrated.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cold_file_window":'coldFileWindow',
        "delete_orphan_data":'deleteOrphanData',
        "file_select_policy":'fileSelectPolicy',
        "file_size":'fileSize',
        "file_size_policy":'fileSizePolicy',
        "filtering_policy":'filteringPolicy',
        "migrate_without_stub":'migrateWithoutStub',
        "nfs_mount_path":'nfsMountPath',
        "target_view_name":'targetViewName'
    }

    def __init__(self,
                 cold_file_window=None,
                 delete_orphan_data=None,
                 file_select_policy=None,
                 file_size=None,
                 file_size_policy=None,
                 filtering_policy=None,
                 migrate_without_stub=None,
                 nfs_mount_path=None,
                 target_view_name=None):
        """Constructor for the FileStubbingParams class"""

        # Initialize members of the class
        self.cold_file_window = cold_file_window
        self.delete_orphan_data = delete_orphan_data
        self.file_select_policy = file_select_policy
        self.file_size = file_size
        self.file_size_policy = file_size_policy
        self.filtering_policy = filtering_policy
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
        delete_orphan_data = dictionary.get('deleteOrphanData', None)
        file_select_policy = dictionary.get('fileSelectPolicy')
        file_size = dictionary.get('fileSize')
        file_size_policy = dictionary.get('fileSizePolicy')
        filtering_policy = cohesity_management_sdk.models.filtering_policy_proto.FilteringPolicyProto.from_dictionary(dictionary.get('filteringPolicy')) if dictionary.get('filteringPolicy') else None
        migrate_without_stub = dictionary.get('migrateWithoutStub', None)
        nfs_mount_path = dictionary.get('nfsMountPath')
        target_view_name = dictionary.get('targetViewName')

        # Return an object of this model
        return cls(cold_file_window,
                   delete_orphan_data,
                   file_select_policy,
                   file_size,
                   file_size_policy,
                   filtering_policy,
                   migrate_without_stub,
                   nfs_mount_path,
                   target_view_name)


