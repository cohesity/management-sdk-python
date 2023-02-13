# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.restore_files_info_proto
import cohesity_management_sdk.models.restore_files_params

class RestoreFilesTaskStateProto(object):

    """Implementation of the 'RestoreFilesTaskStateProto' model.

    TODO: type model description here.

    Attributes:
        restore_files_info (RestoreFilesInfoProto): Each available extension
            is listed below along with the location of the proto file
            (relative to magneto/connectors) where it is defined.
            RestoreFilesInfoProto extension                  Location
            Extn
            ===================================================================
            ========== vmware::RestoreFilesInfo::vmware_restore_files_info
            vmware/vmware.proto     100
            AgentRestoreFilesInfo::agent_restore_files_info  base/agent.proto
            101 file::RestoreFilesInfo::restore_files_info file/file.proto
            102 hyperv::RestoreFilesInfo::hyperv_restore_files_info
            hyperv/hyperv.proto     103
            ===================================================================
            ==========
        restore_params (RestoreFilesParams): This message captures all the
            necessary arguments specified by the user to restore files to the
            source.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "restore_files_info":'restoreFilesInfo',
        "restore_params":'restoreParams'
    }

    def __init__(self,
                 restore_files_info=None,
                 restore_params=None):
        """Constructor for the RestoreFilesTaskStateProto class"""

        # Initialize members of the class
        self.restore_files_info = restore_files_info
        self.restore_params = restore_params


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
        restore_files_info = cohesity_management_sdk.models.restore_files_info_proto.RestoreFilesInfoProto.from_dictionary(dictionary.get('restoreFilesInfo')) if dictionary.get('restoreFilesInfo') else None
        restore_params = cohesity_management_sdk.models.restore_files_params.RestoreFilesParams.from_dictionary(dictionary.get('restoreParams')) if dictionary.get('restoreParams') else None

        # Return an object of this model
        return cls(restore_files_info,
                   restore_params)


