# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.error_proto
import cohesity_management_sdk.models.retrieve_archive_info_retrieved_entity

class RetrieveArchiveInfo(object):

    """Implementation of the 'RetrieveArchiveInfo' model.

    Proto to describe information about the retrieval of an archive task as
    provided by Icebox.

    Attributes:
        avg_logical_transfer_rate_bps (long|int): Average logical bytes
            transfer rate in bytes per second as seen by Icebox.
        bytes_transferred (long|int): Number of physical bytes transferred for
            this retrieval task so far.
        end_time_usecs (long|int): Time when this retrieval task ended at
            Icebox side. If not set, then the retrieval has not ended yet.
        error (ErrorProto):If the retrieval task has completed, the following
            indicates whether there was an error in its completion.
        logical_bytes_transferred (long|int): Number of logical bytes
            transferred so far.
        logical_size_bytes (long|int): Total logical size of the retrieval
            task.
        progress_monitor_task_path (string): The root path of the progress
            monitor for this task.
        retrieved_entity_vec (list of RetrieveArchiveInfoRetrievedEntity):
            Contains info about all retrieved entities.
        skip_cloning_view (bool): If true, we will use the view directly
            without cloning it and delete it when the restore is complete.
        start_time_usecs (long|int): Time when this retrieval task was started
            by Icebox. If not set, then retrieval has not been started yet.
        stub_view_name (string): The stub view that Icebox created. Stub view
            can be used for selectively restoring or accessing files from an
            archive location.
        stub_view_relative_dir_name (string): Relative directory inside the
            stub view that corresponds with the archive.
        target_view_name (string): The name of the target view where Icebox
            has retrieved and staged the requested entities.
        user_action_required_msg (string): Message to display in the UI if any
            manual intervention is needed to make forward progress for the
            retrieve from archive task. This message is mainly relevant for
            tape based retrieve from archive tasks where a backup admin might
            be asked to load new media when the tape library does not have the
            relevant media to retrieve the archive from.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "avg_logical_transfer_rate_bps":'avgLogicalTransferRateBps',
        "bytes_transferred":'bytesTransferred',
        "end_time_usecs":'endTimeUsecs',
        "error":'error',
        "logical_bytes_transferred":'logicalBytesTransferred',
        "logical_size_bytes":'logicalSizeBytes',
        "progress_monitor_task_path":'progressMonitorTaskPath',
        "retrieved_entity_vec":'retrievedEntityVec',
        "skip_cloning_view":'skipCloningView',
        "start_time_usecs":'startTimeUsecs',
        "stub_view_name":'stubViewName',
        "stub_view_relative_dir_name":'stubViewRelativeDirName',
        "target_view_name":'targetViewName',
        "user_action_required_msg":'userActionRequiredMsg'
    }

    def __init__(self,
                 avg_logical_transfer_rate_bps=None,
                 bytes_transferred=None,
                 end_time_usecs=None,
                 error=None,
                 logical_bytes_transferred=None,
                 logical_size_bytes=None,
                 progress_monitor_task_path=None,
                 retrieved_entity_vec=None,
                 skip_cloning_view=None,
                 start_time_usecs=None,
                 stub_view_name=None,
                 stub_view_relative_dir_name=None,
                 target_view_name=None,
                 user_action_required_msg=None):
        """Constructor for the RetrieveArchiveInfo class"""

        # Initialize members of the class
        self.avg_logical_transfer_rate_bps = avg_logical_transfer_rate_bps
        self.bytes_transferred = bytes_transferred
        self.end_time_usecs = end_time_usecs
        self.error = error
        self.logical_bytes_transferred = logical_bytes_transferred
        self.logical_size_bytes = logical_size_bytes
        self.progress_monitor_task_path = progress_monitor_task_path
        self.retrieved_entity_vec = retrieved_entity_vec
        self.skip_cloning_view = skip_cloning_view
        self.start_time_usecs = start_time_usecs
        self.stub_view_name = stub_view_name
        self.stub_view_relative_dir_name = stub_view_relative_dir_name
        self.target_view_name = target_view_name
        self.user_action_required_msg = user_action_required_msg


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
        avg_logical_transfer_rate_bps = dictionary.get('avgLogicalTransferRateBps')
        bytes_transferred = dictionary.get('bytesTransferred')
        end_time_usecs = dictionary.get('endTimeUsecs')
        error = cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(dictionary.get('error')) if dictionary.get('error') else None
        logical_bytes_transferred = dictionary.get('logicalBytesTransferred')
        logical_size_bytes = dictionary.get('logicalSizeBytes')
        progress_monitor_task_path = dictionary.get('progressMonitorTaskPath')
        retrieved_entity_vec = None
        if dictionary.get('retrievedEntityVec') != None:
            retrieved_entity_vec = list()
            for structure in dictionary.get('retrievedEntityVec'):
                retrieved_entity_vec.append(cohesity_management_sdk.models.retrieve_archive_info_retrieved_entity.RetrieveArchiveInfoRetrievedEntity.from_dictionary(structure))
        skip_cloning_view = dictionary.get('skipCloningView')
        start_time_usecs = dictionary.get('startTimeUsecs')
        stub_view_name = dictionary.get('stubViewName')
        stub_view_relative_dir_name = dictionary.get('stubViewRelativeDirName')
        target_view_name = dictionary.get('targetViewName')
        user_action_required_msg = dictionary.get('userActionRequiredMsg')

        # Return an object of this model
        return cls(avg_logical_transfer_rate_bps,
                   bytes_transferred,
                   end_time_usecs,
                   error,
                   logical_bytes_transferred,
                   logical_size_bytes,
                   progress_monitor_task_path,
                   retrieved_entity_vec,
                   skip_cloning_view,
                   start_time_usecs,
                   stub_view_name,
                   stub_view_relative_dir_name,
                   target_view_name,
                   user_action_required_msg)


