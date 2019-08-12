# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.restore_files_preferences
import cohesity_management_sdk.models.restored_file_info
import cohesity_management_sdk.models.credentials

class RestoreFilesParams(object):

    """Implementation of the 'RestoreFilesParams' model.

    This message captures all the necessary arguments specified by the user
    to
    restore files to the source.

    Attributes:
        is_file_volume_restore (bool): Whether this is a file based volume
            restore.
        is_mount_based_flr (bool): Whether this is a mount based file restore
            operation
        nas_protocol_type_vec (list of int): The NAS protocol type(s) of this
            restore task. Currently we only support a single restore type.
            This field is only populated for NAS restore tasks.
        proxy_entity (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        proxy_entity_parent_source (EntityProto): Specifies the attributes and
            the latest statistics about an entity.
        restore_files_preferences (RestoreFilesPreferences): This message
            captures preferences from the user while restoring the files on
            the target.
        restored_file_info_vec (list of RestoredFileInfo): Information
            regarding files and directories.
        target_entity (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        target_entity_credentials (Credentials): Specifies credentials to
            access a target source.
        target_entity_parent_source (EntityProto): Specifies the attributes
            and the latest statistics about an entity.
        target_host_entity (EntityProto): Specifies the attributes and the
            latest statistics about an entity.
        target_host_type (int): The host environment type. This is set in
            VMware environment to indicate the OS type of the target entity.
            NOTE: This is expected to be set since magneto does not know the
            host type for VMware entities.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "is_file_volume_restore":'isFileVolumeRestore',
        "is_mount_based_flr":'isMountBasedFlr',
        "nas_protocol_type_vec":'nasProtocolTypeVec',
        "proxy_entity":'proxyEntity',
        "proxy_entity_parent_source":'proxyEntityParentSource',
        "restore_files_preferences":'restoreFilesPreferences',
        "restored_file_info_vec":'restoredFileInfoVec',
        "target_entity":'targetEntity',
        "target_entity_credentials":'targetEntityCredentials',
        "target_entity_parent_source":'targetEntityParentSource',
        "target_host_entity":'targetHostEntity',
        "target_host_type":'targetHostType'
    }

    def __init__(self,
                 is_file_volume_restore=None,
                 is_mount_based_flr=None,
                 nas_protocol_type_vec=None,
                 proxy_entity=None,
                 proxy_entity_parent_source=None,
                 restore_files_preferences=None,
                 restored_file_info_vec=None,
                 target_entity=None,
                 target_entity_credentials=None,
                 target_entity_parent_source=None,
                 target_host_entity=None,
                 target_host_type=None):
        """Constructor for the RestoreFilesParams class"""

        # Initialize members of the class
        self.is_file_volume_restore = is_file_volume_restore
        self.is_mount_based_flr = is_mount_based_flr
        self.nas_protocol_type_vec = nas_protocol_type_vec
        self.proxy_entity = proxy_entity
        self.proxy_entity_parent_source = proxy_entity_parent_source
        self.restore_files_preferences = restore_files_preferences
        self.restored_file_info_vec = restored_file_info_vec
        self.target_entity = target_entity
        self.target_entity_credentials = target_entity_credentials
        self.target_entity_parent_source = target_entity_parent_source
        self.target_host_entity = target_host_entity
        self.target_host_type = target_host_type


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
        is_file_volume_restore = dictionary.get('isFileVolumeRestore')
        is_mount_based_flr = dictionary.get('isMountBasedFlr')
        nas_protocol_type_vec = dictionary.get('nasProtocolTypeVec')
        proxy_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('proxyEntity')) if dictionary.get('proxyEntity') else None
        proxy_entity_parent_source = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('proxyEntityParentSource')) if dictionary.get('proxyEntityParentSource') else None
        restore_files_preferences = cohesity_management_sdk.models.restore_files_preferences.RestoreFilesPreferences.from_dictionary(dictionary.get('restoreFilesPreferences')) if dictionary.get('restoreFilesPreferences') else None
        restored_file_info_vec = None
        if dictionary.get('restoredFileInfoVec') != None:
            restored_file_info_vec = list()
            for structure in dictionary.get('restoredFileInfoVec'):
                restored_file_info_vec.append(cohesity_management_sdk.models.restored_file_info.RestoredFileInfo.from_dictionary(structure))
        target_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('targetEntity')) if dictionary.get('targetEntity') else None
        target_entity_credentials = cohesity_management_sdk.models.credentials.Credentials.from_dictionary(dictionary.get('targetEntityCredentials')) if dictionary.get('targetEntityCredentials') else None
        target_entity_parent_source = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('targetEntityParentSource')) if dictionary.get('targetEntityParentSource') else None
        target_host_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('targetHostEntity')) if dictionary.get('targetHostEntity') else None
        target_host_type = dictionary.get('targetHostType')

        # Return an object of this model
        return cls(is_file_volume_restore,
                   is_mount_based_flr,
                   nas_protocol_type_vec,
                   proxy_entity,
                   proxy_entity_parent_source,
                   restore_files_preferences,
                   restored_file_info_vec,
                   target_entity,
                   target_entity_credentials,
                   target_entity_parent_source,
                   target_host_entity,
                   target_host_type)


