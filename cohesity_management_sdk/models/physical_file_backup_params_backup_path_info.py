# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class PhysicalFileBackupParamsBackupPathInfo(object):

    """Implementation of the 'PhysicalFileBackupParams_BackupPathInfo' model.

    Describes a set of files rooted under a path that need to be backed up.

    Attributes:
        exclude_paths (list of string): A list of absolute paths on the
            Physical source that should not be backed up. Any path that is a
            descendant of these paths will also be skipped.
        include_path (string): An absolute path on the Physical source that
            should be backed up. Any path that is a descendant of this path
            will also be backed up, unless (a) it is excluded from backup by
            exclude_paths below, OR (b) it belongs to a volume that is
            different from the volume include_path belongs to and there are no
            relevant paths in that volume being backed up.
        skip_nested_volumes (bool): Whether to skip any nested volumes (both
            local and network) that are mounted under 'include_path'. Note
            that if a path to a nested volume is specified as an include_path
            in another BackupPathInfo entry, that path will still get backed
            up.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "exclude_paths":'excludePaths',
        "include_path":'includePath',
        "skip_nested_volumes":'skipNestedVolumes'
    }

    def __init__(self,
                 exclude_paths=None,
                 include_path=None,
                 skip_nested_volumes=None):
        """Constructor for the PhysicalFileBackupParamsBackupPathInfo class"""

        # Initialize members of the class
        self.exclude_paths = exclude_paths
        self.include_path = include_path
        self.skip_nested_volumes = skip_nested_volumes


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
        exclude_paths = dictionary.get('excludePaths')
        include_path = dictionary.get('includePath')
        skip_nested_volumes = dictionary.get('skipNestedVolumes')

        # Return an object of this model
        return cls(exclude_paths,
                   include_path,
                   skip_nested_volumes)


