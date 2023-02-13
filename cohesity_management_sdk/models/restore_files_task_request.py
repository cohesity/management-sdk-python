# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.filter_ip_config
import cohesity_management_sdk.models.restored_file_info_list
import cohesity_management_sdk.models.restore_object_details

class RestoreFilesTaskRequest(object):

    """Implementation of the 'RestoreFilesTaskRequest' model.

    Specifies information about a Restore Task that recovers files and
    folders.

    Attributes:
        continue_on_error (bool): Specifies if the Restore Task should
            continue even if the copy operation of some files and folders
            fails. If true, the Cohesity Cluster ignores intermittent errors
            and recovers as many files and folders as possible. If false, the
            Restore Task stops recovering when a copy operation fails.
        file_recovery_method (FileRecoveryMethodEnum): Specifies the type of
            method to be used to perform file recovery.
            'kAutoDeploy' indicates that file restore operation will be
            performed using an ephemeral agent.
            'kUseExistingAgent' indicates that file restore operation will be
            performed using an persistent agent.
            'kUseHypervisorAPIs' indicates that file restore operation will be
            performed using an hypervisor API's.
        filenames (list of string): Array of Files or Folders.  Specifies the
            files and folders to recover from the snapshot.
        filter_ip_config (FilterIpConfig): Specifies the list of IP addresses
            that are allowed or denied during restore. Allowed IPs and Denied
            IPs cannot be used together.
        is_file_based_volume_restore (bool): Specifies whether this is a file
            based volume restore.
        mount_disks_on_vm (bool): Sepcifies whether this will attach disks or
            mount disks on the VM side OR use Storage Proxy RPCs to stream
            data
        name (string): Specifies the name of the Restore Task. This field must
            be set and must be a unique name.
        new_base_directory (string): Specifies an optional root folder where
            to recover the selected files and folders. By default, files and
            folders are restored to their original path.
        overwrite (bool): If true, any existing files and folders on the
            operating system are overwritten by the recovered files or
            folders. This is the default. If false, existing files and folders
            are not overwritten.
        password (string): Specifies password of the username to access the
            target source.
        preserve_attributes (bool): If true, the Restore Tasks preserves the
            original file and folder attributes. This is the default.
        restored_file_info_list (list of RestoredFileInfoList): Specifies
            information regarding files and directories.
        source_object_info (RestoreObjectDetails): Specifies information about
            the source object (such as a VM) that contains the files and
            folders to recover. In addition, it contains information about the
            Protection Job and Job Run that captured the snapshot to recover
            from. To specify a particular snapshot, you must specify a
            jobRunId and a startTimeUsecs. If jobRunId and startTimeUsecs are
            not specified, the last Job Run of the specified Job is used.
        target_host_type (TargetHostTypeEnum): Specifies the target host types
            to be restored. 'kLinux' indicates the Linux operating system.
            'kWindows' indicates the Microsoft Windows operating system.
            'kAix' indicates the IBM AIX operating system. 'kSolaris'
            indicates the Oracle Solaris operating system. 'kSapHana'
            indicates the Sap Hana database system developed by SAP SE.
            'kOther' indicates the other types of operating system.
        target_parent_source_id (long|int): Specifies the registered source
            (such as a vCenter Server) that contains the target protection
            source (such as a VM) where the files and folders are recovered
            to. This field is not required for a Physical Server.
        target_source_id (long|int): Specifies the id of the target protection
            source (such as a VM) where the files and folders are recovered
            to.
        use_existing_agent (bool): Specifies whether this will use an existing
            agent on the target vm to do restore. Following field is
            deprecated and shall not be used. Please refer to the
            FileRecoveryMethod field for more information.
        username (string): Specifies username to access the target source.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "continue_on_error":'continueOnError',
        "file_recovery_method":'fileRecoveryMethod',
        "filenames":'filenames',
        "filter_ip_config":'filterIpConfig',
        "is_file_based_volume_restore":'isFileBasedVolumeRestore',
        "mount_disks_on_vm":'mountDisksOnVm',
        "name":'name',
        "new_base_directory":'newBaseDirectory',
        "overwrite":'overwrite',
        "password":'password',
        "preserve_attributes":'preserveAttributes',
        "restored_file_info_list":'restoredFileInfoList',
        "source_object_info":'sourceObjectInfo',
        "target_host_type":'targetHostType',
        "target_parent_source_id":'targetParentSourceId',
        "target_source_id":'targetSourceId',
        "use_existing_agent":'useExistingAgent',
        "username":'username'
    }

    def __init__(self,
                 continue_on_error=None,
                 file_recovery_method=None,
                 filenames=None,
                 filter_ip_config=None,
                 is_file_based_volume_restore=None,
                 mount_disks_on_vm=None,
                 name=None,
                 new_base_directory=None,
                 overwrite=None,
                 password=None,
                 preserve_attributes=None,
                 restored_file_info_list=None,
                 source_object_info=None,
                 target_host_type=None,
                 target_parent_source_id=None,
                 target_source_id=None,
                 use_existing_agent=None,
                 username=None):
        """Constructor for the RestoreFilesTaskRequest class"""

        # Initialize members of the class
        self.continue_on_error = continue_on_error
        self.file_recovery_method = file_recovery_method
        self.filenames = filenames
        self.filter_ip_config = filter_ip_config
        self.is_file_based_volume_restore = is_file_based_volume_restore
        self.mount_disks_on_vm = mount_disks_on_vm
        self.name = name
        self.new_base_directory = new_base_directory
        self.overwrite = overwrite
        self.password = password
        self.preserve_attributes = preserve_attributes
        self.restored_file_info_list = restored_file_info_list
        self.source_object_info = source_object_info
        self.target_host_type = target_host_type
        self.target_parent_source_id = target_parent_source_id
        self.target_source_id = target_source_id
        self.use_existing_agent = use_existing_agent
        self.username = username


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
        continue_on_error = dictionary.get('continueOnError')
        filenames = dictionary.get('filenames')
        file_recovery_method = dictionary.get('fileRecoveryMethod')
        filter_ip_config = cohesity_management_sdk.models.filter_ip_config.FilterIpConfig.from_dictionary(dictionary.get('filterIpConfig')) if dictionary.get('filterIpConfig') else None
        is_file_based_volume_restore = dictionary.get('isFileBasedVolumeRestore')
        mount_disks_on_vm = dictionary.get('mountDisksOnVm')
        name = dictionary.get('name')
        new_base_directory = dictionary.get('newBaseDirectory')
        overwrite = dictionary.get('overwrite')
        password = dictionary.get('password')
        preserve_attributes = dictionary.get('preserveAttributes')
        restored_file_info_list = None
        if dictionary.get('restoredFileInfoList') != None:
            restored_file_info_list = list()
            for structure in dictionary.get('restoredFileInfoList'):
                restored_file_info_list.append(cohesity_management_sdk.models.restored_file_info_list.RestoredFileInfoList.from_dictionary(structure))
        source_object_info = cohesity_management_sdk.models.restore_object_details.RestoreObjectDetails.from_dictionary(dictionary.get('sourceObjectInfo')) if dictionary.get('sourceObjectInfo') else None
        target_host_type = dictionary.get('targetHostType')
        target_parent_source_id = dictionary.get('targetParentSourceId')
        target_source_id = dictionary.get('targetSourceId')
        use_existing_agent = dictionary.get('useExistingAgent')
        username = dictionary.get('username')

        # Return an object of this model
        return cls(continue_on_error,
                   file_recovery_method,
                   filenames,
                   filter_ip_config,
                   is_file_based_volume_restore,
                   mount_disks_on_vm,
                   name,
                   new_base_directory,
                   overwrite,
                   password,
                   preserve_attributes,
                   restored_file_info_list,
                   source_object_info,
                   target_host_type,
                   target_parent_source_id,
                   target_source_id,
                   use_existing_agent,
                   username)


