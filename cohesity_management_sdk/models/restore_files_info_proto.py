# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.error_proto
import cohesity_management_sdk.models.connector_params
import cohesity_management_sdk.models.restore_file_result_info

class RestoreFilesInfoProto(object):

    """Implementation of the 'RestoreFilesInfoProto' model.

    Each available extension is listed below along with the location of the
    proto file (relative to magneto/connectors) where it is defined.
    RestoreFilesInfoProto extension                  Location
    Extn
    ===========================================================================
    ==
    vmware::RestoreFilesInfo::vmware_restore_files_info
    vmware/vmware.proto     100
    AgentRestoreFilesInfo::agent_restore_files_info  base/agent.proto
    101
    file::RestoreFilesInfo::restore_files_info
    file/file.proto         102
    hyperv::RestoreFilesInfo::hyperv_restore_files_info
    hyperv/hyperv.proto     103
    ===========================================================================
    ==

    Attributes:
        download_files_path (string): The path that the user should use to
            download files through the UI. If only a single file needs to be
            downloaded, this will be the path to that file. If a directory or
            multiple files & directories need to be downloaded, this will be
            the path to the .zip file to download. Only applicable to a
            download files task.
        error (ErrorProto): TODO: type description here.
        proxy_entity_connector_params (ConnectorParams): Message that
            encapsulates the various params required to establish a connection
            with a particular environment.
        restore_files_result_vec (list of RestoreFileResultInfo): Contains the
            result information of the restored files.
        slave_task_start_time_usecs (long|int): This is the timestamp at which
            the slave task started.
        target_type (int): Specifies the target type for the task. The field
            is only valid if the task has got a permit.
        teardown_error (ErrorProto): TODO: type description here.
        mtype (int): The type of environment this restore files info pertains
            to.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "download_files_path":'downloadFilesPath',
        "error":'error',
        "proxy_entity_connector_params":'proxyEntityConnectorParams',
        "restore_files_result_vec":'restoreFilesResultVec',
        "slave_task_start_time_usecs":'slaveTaskStartTimeUsecs',
        "target_type":'targetType',
        "teardown_error":'teardownError',
        "mtype":'type'
    }

    def __init__(self,
                 download_files_path=None,
                 error=None,
                 proxy_entity_connector_params=None,
                 restore_files_result_vec=None,
                 slave_task_start_time_usecs=None,
                 target_type=None,
                 teardown_error=None,
                 mtype=None):
        """Constructor for the RestoreFilesInfoProto class"""

        # Initialize members of the class
        self.download_files_path = download_files_path
        self.error = error
        self.proxy_entity_connector_params = proxy_entity_connector_params
        self.restore_files_result_vec = restore_files_result_vec
        self.slave_task_start_time_usecs = slave_task_start_time_usecs
        self.target_type = target_type
        self.teardown_error = teardown_error
        self.mtype = mtype


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
        download_files_path = dictionary.get('downloadFilesPath')
        error = cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(dictionary.get('error')) if dictionary.get('error') else None
        proxy_entity_connector_params = cohesity_management_sdk.models.connector_params.ConnectorParams.from_dictionary(dictionary.get('proxyEntityConnectorParams')) if dictionary.get('proxyEntityConnectorParams') else None
        restore_files_result_vec = None
        if dictionary.get('restoreFilesResultVec') != None:
            restore_files_result_vec = list()
            for structure in dictionary.get('restoreFilesResultVec'):
                restore_files_result_vec.append(cohesity_management_sdk.models.restore_file_result_info.RestoreFileResultInfo.from_dictionary(structure))
        slave_task_start_time_usecs = dictionary.get('slaveTaskStartTimeUsecs')
        target_type = dictionary.get('targetType')
        teardown_error = cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(dictionary.get('teardownError')) if dictionary.get('teardownError') else None
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(download_files_path,
                   error,
                   proxy_entity_connector_params,
                   restore_files_result_vec,
                   slave_task_start_time_usecs,
                   target_type,
                   teardown_error,
                   mtype)


