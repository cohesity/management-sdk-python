# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.input_spec_file_time_filter

class InputSpecInputFilesSelector(object):

    """Implementation of the 'InputSpec_InputFilesSelector' model.

    If mapper is going to run over files on SnapFS, this selects the input
    files.

    Attributes:
        file_time_filter (InputSpec_FileTimeFilter): File time filter for
            file's last change time.
        filename_glob (list of string): Glob patterns to match on file. e.g.
            {*.txt, *.cc}
        job_ids (list of int): TODO: add descritpion here.
        max_snapshot_timestamp (long|int):Exclusive end of snapshot_timestamp
            range. If missing, inf will be used as the timestamp range.
        min_snapshot_timestamp (long|int): Specifies the logical size used in
            bytes.
        partition_ids (list of int): TODO: add descritpion here.
        process_latest_only (bool): Boolean flag to indicate if only latest
            snapshot of each object should be processed.
        root_dir (string): Within each volume, traversal will be rooted at
            this directory. A typical value here might be /home
        view_box_ids (long|int): TODO: add descritpion here.
        view_name (string): This is the view name user enters manually. If
            this is set we will process this view only. partition_id and
            view_box_id will be populated only if view_name is present.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "file_time_filter":'fileTimeFilter',
        "filename_glob":'filenameGlob',
        "job_ids":'jobIds',
        "max_snapshot_timestamp":'maxSnapshotTimestamp',
        "min_snapshot_timestamp":'minSnapshotTimestamp',
        "partition_ids":'partitionIds',
        "process_latest_only":'processLatestOnly',
        "root_dir":'rootDir',
        "view_box_ids":'viewBoxIds',
        "view_name":'viewName'
    }

    def __init__(self,
                 file_time_filter=None,
                 filename_glob=None,
                 job_ids=None,
                 max_snapshot_timestamp=None,
                 min_snapshot_timestamp=None,
                 partition_ids=None,
                 process_latest_only=None,
                 root_dir=None,
                 view_box_ids=None,
                 view_name=None):
        """Constructor for the InputSpec_InputFilesSelector class"""

        # Initialize members of the class
        self.file_time_filter = file_time_filter
        self.filename_glob = filename_glob
        self.job_ids = job_ids
        self.max_snapshot_timestamp = max_snapshot_timestamp
        self.min_snapshot_timestamp = min_snapshot_timestamp
        self.partition_ids = partition_ids
        self.process_latest_only = process_latest_only
        self.root_dir = root_dir
        self.view_box_ids = view_box_ids
        self.view_name = view_name


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
        file_time_filter = cohesity_management_sdk.models.input_spec_file_time_filter.InputSpec_FileTimeFilter.from_dictionary( dictionary.get('fileTimeFilter')) if dictionary.get('fileTimeFilter') else None
        filename_glob = dictionary.get('filenameGlob')
        job_ids = dictionary.get('jobIds')
        max_snapshot_timestamp = dictionary.get('maxSnapshotTimestamp')
        min_snapshot_timestamp = dictionary.get('minSnapshotTimestamp')
        partition_ids = dictionary.get('partitionIds')
        process_latest_only = dictionary.get('processLatestOnly')
        root_dir = dictionary.get('rootDir')
        view_box_ids = dictionary.get('viewBoxIds')
        view_name = dictionary.get('viewName')

        # Return an object of this model
        return cls(file_time_filter,
                   filename_glob,
                   job_ids,
                   max_snapshot_timestamp,
                   min_snapshot_timestamp,
                   partition_ids,
                   process_latest_only,
                   root_dir,
                   view_box_ids,
                   view_name)


