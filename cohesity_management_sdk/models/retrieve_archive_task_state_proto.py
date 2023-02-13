# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.archival_target
import cohesity_management_sdk.models.universal_id_proto
import cohesity_management_sdk.models.retrieve_archive_task_state_proto_download_files_info
import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.error_proto
import cohesity_management_sdk.models.retrieve_archive_info
import cohesity_management_sdk.models.vault_params_restore_params

class RetrieveArchiveTaskStateProto(object):

    """Implementation of the 'RetrieveArchiveTaskStateProto' model.

    Persistent state of a retrieve of an archive task. Only one of either
    entity_vec or download_files_info needs to be specified in this proto,
    where
    entity_vec is for retrieving the whole objects from the archive, and
    download_files_info is for only downloading the specified files from the
    archive.

    Attributes:
        archival_target (ArchivalTarget): Message that specifies the details
            about an archival target (such as cloud or tape) where backup
            snapshots may be archived to.
        archive_task_uid (UniversalIdProto): The uid of the archive to be
            retrieved.
        backup_run_start_time_usecs (long|int): The start time of the backup
            run whose corresponding archive is being retrieved. This field is
            just used for logging purposes.
        cancellation_requested (bool): Whether this retrieval task has a
            pending cancellation request.
        download_files_info (RetrieveArchiveTaskStateProtoDownloadFilesInfo):
            Information required for Icebox when downloading files from an
            archived entity. This proto is specifically just for the current
            temporary solution for downloading a single from an archive, where
            we let icebox download the file for us. In the future once the new
            Yoda APIs for downloading files from archive stub views are ready,
            we will just discard this proto and make field 20 reserved.
        end_time_usecs (long|int): If the retrieval task has finished, this
            field contains the end time for the task.
        entity_vec (list of EntityProto): Information on the exact set of
            objects to retrieve from archive. Even if the user wanted to
            retrieve all objects from the archive, this field will contain all
            individual leaf-level objects.
        error (ErrorProto): The error encountered by task (if any). Only valid
            if the task has finished.
        full_view_name_deprecated (string): The full view name (external).
            This is composed of a Cohesity specific prefix and the user
            provided view name.
        job_uid (UniversalIdProto): The uid of the job to which the archive to
            be retrieved belongs to.
        name (string): The name of the retrieval task.
        progress_monitor_task_path (string): The path of the progress monitor
            for this task.
        restore_archive_files_info
            (RetrieveArchiveTaskStateProtoDownloadFilesInfo): Information
            required for Icebox when downloading files from an archived
            entity. This proto is specifically just for the current temporary
            solution for downloading a single from an archive, where we let
            icebox download the file for us. In the future once the new Yoda
            APIs for downloading files from archive stub views are ready, we
            will just discard this proto and make field 20 reserved.
        restore_task_id (long|int): For retrieve tasks created after the 2.8
            release, this will contain the id of the restore task that created
            this retrieve task.
        retrieval_info (RetrieveArchiveInfo): Proto to describe information
            about the retrieval of an archive task as provided by Icebox.
        start_time_usecs (long|int): The start time for this retrieval task.
        status (int): The status of this task.
        task_uid (UniversalIdProto): The globally unique id for this retrieval
            of an archive task.
        user (string): The user who requested this retrieval task.
        vault_restore_params (VaultParamsRestoreParams): Params to be passed
            to Icebox while restoring data from an archive.
        view_box_id (long|int): The view box id to which 'view_name' belongs
            to.
        view_name_deprecated (string): The view name as provided by the user
            for this retrieval task. Retrieved snapshots of the entities will
            be placed in this view.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "archival_target":'archivalTarget',
        "archive_task_uid":'archiveTaskUid',
        "backup_run_start_time_usecs":'backupRunStartTimeUsecs',
        "cancellation_requested":'cancellationRequested',
        "download_files_info":'downloadFilesInfo',
        "end_time_usecs":'endTimeUsecs',
        "entity_vec":'entityVec',
        "error":'error',
        "full_view_name_deprecated":'fullViewName_DEPRECATED',
        "job_uid":'jobUid',
        "name":'name',
        "progress_monitor_task_path":'progressMonitorTaskPath',
        "restore_archive_files_info":'restoreArchiveFilesInfo',
        "restore_task_id":'restoreTaskId',
        "retrieval_info":'retrievalInfo',
        "start_time_usecs":'startTimeUsecs',
        "status":'status',
        "task_uid":'taskUid',
        "user":'user',
        "vault_restore_params":'vaultRestoreParams',
        "view_box_id":'viewBoxId',
        "view_name_deprecated":'viewName_DEPRECATED'
    }

    def __init__(self,
                 archival_target=None,
                 archive_task_uid=None,
                 backup_run_start_time_usecs=None,
                 cancellation_requested=None,
                 download_files_info=None,
                 end_time_usecs=None,
                 entity_vec=None,
                 error=None,
                 full_view_name_deprecated=None,
                 job_uid=None,
                 name=None,
                 progress_monitor_task_path=None,
                 restore_archive_files_info=None,
                 restore_task_id=None,
                 retrieval_info=None,
                 start_time_usecs=None,
                 status=None,
                 task_uid=None,
                 user=None,
                 vault_restore_params=None,
                 view_box_id=None,
                 view_name_deprecated=None):
        """Constructor for the RetrieveArchiveTaskStateProto class"""

        # Initialize members of the class
        self.archival_target = archival_target
        self.archive_task_uid = archive_task_uid
        self.backup_run_start_time_usecs = backup_run_start_time_usecs
        self.cancellation_requested = cancellation_requested
        self.download_files_info = download_files_info
        self.end_time_usecs = end_time_usecs
        self.entity_vec = entity_vec
        self.error = error
        self.full_view_name_deprecated = full_view_name_deprecated
        self.job_uid = job_uid
        self.name = name
        self.progress_monitor_task_path = progress_monitor_task_path
        self.restore_archive_files_info = restore_archive_files_info
        self.restore_task_id = restore_task_id
        self.retrieval_info = retrieval_info
        self.start_time_usecs = start_time_usecs
        self.status = status
        self.task_uid = task_uid
        self.user = user
        self.vault_restore_params = vault_restore_params
        self.view_box_id = view_box_id
        self.view_name_deprecated = view_name_deprecated


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
        archival_target = cohesity_management_sdk.models.archival_target.ArchivalTarget.from_dictionary(dictionary.get('archivalTarget')) if dictionary.get('archivalTarget') else None
        archive_task_uid = cohesity_management_sdk.models.universal_id_proto.UniversalIdProto.from_dictionary(dictionary.get('archiveTaskUid')) if dictionary.get('archiveTaskUid') else None
        backup_run_start_time_usecs = dictionary.get('backupRunStartTimeUsecs')
        cancellation_requested = dictionary.get('cancellationRequested')
        download_files_info = cohesity_management_sdk.models.retrieve_archive_task_state_proto_download_files_info.RetrieveArchiveTaskStateProtoDownloadFilesInfo.from_dictionary(dictionary.get('downloadFilesInfo')) if dictionary.get('downloadFilesInfo') else None
        end_time_usecs = dictionary.get('endTimeUsecs')
        entity_vec = None
        if dictionary.get('entityVec') != None:
            entity_vec = list()
            for structure in dictionary.get('entityVec'):
                entity_vec.append(cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(structure))
        error = cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(dictionary.get('error')) if dictionary.get('error') else None
        full_view_name_deprecated = dictionary.get('fullViewName_DEPRECATED')
        job_uid = cohesity_management_sdk.models.universal_id_proto.UniversalIdProto.from_dictionary(dictionary.get('jobUid')) if dictionary.get('jobUid') else None
        name = dictionary.get('name')
        progress_monitor_task_path = dictionary.get('progressMonitorTaskPath')
        restore_archive_files_info = cohesity_management_sdk.models.retrieve_archive_task_state_proto_download_files_info.RetrieveArchiveTaskStateProtoDownloadFilesInfo.from_dictionary(dictionary.get('restoreArchiveFilesInfo')) if dictionary.get('restoreArchiveFilesInfo') else None
        restore_task_id = dictionary.get('restoreTaskId')
        retrieval_info = cohesity_management_sdk.models.retrieve_archive_info.RetrieveArchiveInfo.from_dictionary(dictionary.get('retrievalInfo')) if dictionary.get('retrievalInfo') else None
        start_time_usecs = dictionary.get('startTimeUsecs')
        status = dictionary.get('status')
        task_uid = cohesity_management_sdk.models.universal_id_proto.UniversalIdProto.from_dictionary(dictionary.get('taskUid')) if dictionary.get('taskUid') else None
        user = dictionary.get('user')
        vault_restore_params = cohesity_management_sdk.models.vault_params_restore_params.VaultParamsRestoreParams.from_dictionary(dictionary.get('vaultRestoreParams')) if dictionary.get('vaultRestoreParams') else None
        view_box_id = dictionary.get('viewBoxId')
        view_name_deprecated = dictionary.get('viewName_DEPRECATED')

        # Return an object of this model
        return cls(archival_target,
                   archive_task_uid,
                   backup_run_start_time_usecs,
                   cancellation_requested,
                   download_files_info,
                   end_time_usecs,
                   entity_vec,
                   error,
                   full_view_name_deprecated,
                   job_uid,
                   name,
                   progress_monitor_task_path,
                   restore_archive_files_info,
                   restore_task_id,
                   retrieval_info,
                   start_time_usecs,
                   status,
                   task_uid,
                   user,
                   vault_restore_params,
                   view_box_id,
                   view_name_deprecated)


