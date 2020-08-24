# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.restore_files_params_directory_name_security_style_map_entry
import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.file_uptiering_params
import cohesity_management_sdk.models.restore_files_preferences
import cohesity_management_sdk.models.restored_file_info
import cohesity_management_sdk.models.credentials
import cohesity_management_sdk.models.nas_backup_params

class RestoreFilesParams(object):

    """Implementation of the 'RestoreFilesParams' model.

    This message captures all the necessary arguments specified by the user
    to
    restore files to the source.

    Attributes:
        blacklisted_ip_addrs (list of string): A list of target IP addresses
            that should not be used.
        directory_name_security_style_map (list of
            RestoreFilesParamsDirectoryNameSecurityStyleMapEntry): Directory
            name security style map contains mapping of the directory name to
            security style it supports.  This is needed to restore the same
            permission for the given directory for Qtrees.
        is_archive_flr (bool): Whether this is a file restore operation from
            an archive.
        is_file_volume_restore (bool): Whether this will use an existing agent
            on the target VM to do the restore.
            This field is deprecated. restore_method should be used for populating
            use of existing agent.
        is_mount_based_flr (bool): Whether this is a mount based file restore
            operation
        mount_disks_on_vm (bool): Whether this will attach disks or mount
            disks on the VM side OR use Storage Proxy RPCs to stream data.
        nas_backup_params (NasBackupParams): Used to determining
            filtering_policy for NAS Migration uptier operation. Currently
            this is set only if this is NAS Migration uptier operation.
        nas_protocol_type_vec (list of int): The NAS protocol type(s) of this
            restore task. Currently we only support a single restore type.
            This field is only populated for NAS restore tasks.
        physical_flr_parallel_restore (bool): If enabled, magneto physical
            file restore will be enabled via job framework
        proxy_entity (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        proxy_entity_parent_source (EntityProto): Specifies the attributes and
            the latest statistics about an entity.
        restore_files_preferences (RestoreFilesPreferences): This message
            captures preferences from the user while restoring the files on
            the target.
        restore_method (int): Determines the type of method to be used to
            perform FLR.
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
        uptier_params (FileUptieringParams): Set if this is NAS Migration
            uptier operation.
        vpc_connector_entity (EntityProto): Specifies the attributes and the
            latest statistics about an entity.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "blacklisted_ip_addrs":'blacklistedIpAddrs',
        "directory_name_security_style_map":'directoryNameSecurityStyleMap',
        "is_archive_flr":'isArchiveFlr',
        "is_file_volume_restore":'isFileVolumeRestore',
        "is_mount_based_flr":'isMountBasedFlr',
        "mount_disks_on_vm":'mountDisksOnVm',
        "nas_backup_params":'nasBackupParams',
        "nas_protocol_type_vec":'nasProtocolTypeVec',
        "physical_flr_parallel_restore":'physicalFlrParallelRestore',
        "proxy_entity":'proxyEntity',
        "proxy_entity_parent_source":'proxyEntityParentSource',
        "restore_files_preferences":'restoreFilesPreferences',
        "restore_method":'restoreMethod',
        "restored_file_info_vec":'restoredFileInfoVec',
        "target_entity":'targetEntity',
        "target_entity_credentials":'targetEntityCredentials',
        "target_entity_parent_source":'targetEntityParentSource',
        "target_host_entity":'targetHostEntity',
        "target_host_type":'targetHostType',
        "uptier_params":'uptierParams',
        "vpc_connector_entity":'vpcConnectorEntity'
    }

    def __init__(self,
                 blacklisted_ip_addrs=None,
                 directory_name_security_style_map=None,
                 is_archive_flr=None,
                 is_file_volume_restore=None,
                 is_mount_based_flr=None,
                 mount_disks_on_vm=None,
                 nas_backup_params=None,
                 nas_protocol_type_vec=None,
                 physical_flr_parallel_restore=None,
                 proxy_entity=None,
                 proxy_entity_parent_source=None,
                 restore_files_preferences=None,
                 restore_method=None,
                 restored_file_info_vec=None,
                 target_entity=None,
                 target_entity_credentials=None,
                 target_entity_parent_source=None,
                 target_host_entity=None,
                 target_host_type=None,
                 uptier_params=None,
                 vpc_connector_entity=None):
        """Constructor for the RestoreFilesParams class"""

        # Initialize members of the class
        self.blacklisted_ip_addrs = blacklisted_ip_addrs
        self.directory_name_security_style_map = directory_name_security_style_map
        self.is_archive_flr = is_archive_flr
        self.is_file_volume_restore = is_file_volume_restore
        self.is_mount_based_flr = is_mount_based_flr
        self.mount_disks_on_vm = mount_disks_on_vm
        self.nas_backup_params = nas_backup_params
        self.nas_protocol_type_vec = nas_protocol_type_vec
        self.physical_flr_parallel_restore = physical_flr_parallel_restore
        self.proxy_entity = proxy_entity
        self.proxy_entity_parent_source = proxy_entity_parent_source
        self.restore_files_preferences = restore_files_preferences
        self.restore_method  = restore_method
        self.restored_file_info_vec = restored_file_info_vec
        self.target_entity = target_entity
        self.target_entity_credentials = target_entity_credentials
        self.target_entity_parent_source = target_entity_parent_source
        self.target_host_entity = target_host_entity
        self.target_host_type = target_host_type
        self.uptier_params = uptier_params
        self.vpc_connector_entity = vpc_connector_entity


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
        blacklisted_ip_addrs = dictionary.get('blacklistedIpAddrs')
        directory_name_security_style_map = None
        if dictionary.get('directoryNameSecurityStyleMap') != None:
            directory_name_security_style_map = list()
            for structure in dictionary.get('directoryNameSecurityStyleMap'):
                directory_name_security_style_map.append(cohesity_management_sdk.models.restore_files_params_directory_name_security_style_map_entry.RestoreFilesParamsDirectoryNameSecurityStyleMapEntry.from_dictionary(structure))
        is_archive_flr = dictionary.get('isArchiveFlr')
        is_file_volume_restore = dictionary.get('isFileVolumeRestore')
        is_mount_based_flr = dictionary.get('isMountBasedFlr')
        mount_disks_on_vm = dictionary.get('mountDisksOnVm')
        nas_backup_params = cohesity_management_sdk.models.nas_backup_params.NasBackupParams.from_dictionary(dictionary.get('nasBackupParams')) if dictionary.get('nasBackupParams') else None
        nas_protocol_type_vec = dictionary.get('nasProtocolTypeVec')
        physical_flr_parallel_restore = dictionary.get('physicalFlrParallelRestore')
        proxy_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('proxyEntity')) if dictionary.get('proxyEntity') else None
        proxy_entity_parent_source = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('proxyEntityParentSource')) if dictionary.get('proxyEntityParentSource') else None
        restore_files_preferences = cohesity_management_sdk.models.restore_files_preferences.RestoreFilesPreferences.from_dictionary(dictionary.get('restoreFilesPreferences')) if dictionary.get('restoreFilesPreferences') else None
        restore_method = dictionary.get('restoreMethod')
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
        uptier_params = cohesity_management_sdk.models.file_uptiering_params.FileUptieringParams.from_dictionary(dictionary.get('uptierParams')) if dictionary.get('uptierParams') else None
        vpc_connector_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('vpcConnectorEntity')) if dictionary.get('vpcConnectorEntity') else None

        # Return an object of this model
        return cls(blacklisted_ip_addrs,
                   directory_name_security_style_map,
                   is_archive_flr,
                   is_file_volume_restore,
                   is_mount_based_flr,
                   mount_disks_on_vm,
                   nas_backup_params,
                   nas_protocol_type_vec,
                   physical_flr_parallel_restore,
                   proxy_entity,
                   proxy_entity_parent_source,
                   restore_files_preferences,
                   restore_method,
                   restored_file_info_vec,
                   target_entity,
                   target_entity_credentials,
                   target_entity_parent_source,
                   target_host_entity,
                   target_host_type,
                   uptier_params,
                   vpc_connector_entity)


