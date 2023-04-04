# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.uda_recover_job_params_restore_job_arguments_map_entry
import cohesity_management_sdk.models.uda_recover_job_params_source_arguments_map_entry
import cohesity_management_sdk.models.uda_s_3_view_backup_properties
import cohesity_management_sdk.models.uda_source_capabilities


class UdaRecoverJobParams(object):

    """Implementation of the 'UdaRecoverJobParams' model.

    TODO: type description here.


    Attributes:

        capabilities (UdaSourceCapabilities): Types of backups supported.
        concurrency (int): Number of parallel streams to use for the restore.
        host_type (int): The agent host environment type.
        hosts (list of string): List of hosts forming the UDA cluster.
        local_mount_dir (string): Directory on the host where views will be
            mounted. (This is deprecated now and the value is derived from a
            gflag in agent.)
        mount_view (bool): Whether to mount a view during restore.
        mounts (int): Max number of view mounts to use for the restore.
        preferred_control_nodes (list of string): Control nodes to connect for
            control path ops.
        restore_args (string): Custom arguments which are applicable to the
            objects to be restored.
        restore_job_arguments_map (list of
            UdaRecoverJobParams_RestoreJobArgumentsMapEntry): Map to store
            custom arguments which will be provided to the recovery job
            scripts.
        run_start_time_usecs (long|int): The time when the corresponding backup
            run was started.
        script_dir (string): Path where the source scripts will be located.
        source_args (string): Custom arguments which will be provided to the
            source registration scripts.
        source_arguments_map (list of
            UdaRecoverJobParams_SourceArgumentsMapEntry): Map to store custom
            arguments which will be provided to the source registration
            scripts.
        source_type (string): Universal Data Adapter source type for which
            recovery is being performed.
        uda_s_3_view_backup_properties (UdaS3ViewBackupProperties): This
            message captures all the details needed by UDA Restore to clone S3
            views and access the S3 bucket.
        use_s_3_view (bool): Whether S3 views should be used for restore.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "capabilities":'capabilities',
        "concurrency":'concurrency',
        "host_type":'hostType',
        "hosts":'hosts',
        "local_mount_dir":'localMountDir',
        "mount_view":'mountView',
        "mounts":'mounts',
        "preferred_control_nodes":'preferredControlNodes',
        "restore_args":'restoreArgs',
        "restore_job_arguments_map":'restoreJobArgumentsMap',
        "run_start_time_usecs":'runStartTimeUsecs',
        "script_dir":'scriptDir',
        "source_args":'sourceArgs',
        "source_arguments_map":'sourceArgumentsMap',
        "source_type":'sourceType',
        "uda_s_3_view_backup_properties":'udaS3ViewBackupProperties',
        "use_s_3_view":'useS3View',
    }
    def __init__(self,
                 capabilities=None,
                 concurrency=None,
                 host_type=None,
                 hosts=None,
                 local_mount_dir=None,
                 mount_view=None,
                 mounts=None,
                 preferred_control_nodes=None,
                 restore_args=None,
                 restore_job_arguments_map=None,
                 run_start_time_usecs=None,
                 script_dir=None,
                 source_args=None,
                 source_arguments_map=None,
                 source_type=None,
                 uda_s_3_view_backup_properties=None,
                 use_s_3_view=None,
            ):

        """Constructor for the UdaRecoverJobParams class"""

        # Initialize members of the class
        self.capabilities = capabilities
        self.concurrency = concurrency
        self.host_type = host_type
        self.hosts = hosts
        self.local_mount_dir = local_mount_dir
        self.mount_view = mount_view
        self.mounts = mounts
        self.preferred_control_nodes = preferred_control_nodes
        self.restore_args = restore_args
        self.restore_job_arguments_map = restore_job_arguments_map
        self.run_start_time_usecs = run_start_time_usecs
        self.script_dir = script_dir
        self.source_args = source_args
        self.source_arguments_map = source_arguments_map
        self.source_type = source_type
        self.uda_s_3_view_backup_properties = uda_s_3_view_backup_properties
        self.use_s_3_view = use_s_3_view

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
        capabilities = cohesity_management_sdk.models.uda_source_capabilities.UdaSourceCapabilities.from_dictionary(dictionary.get('capabilities')) if dictionary.get('capabilities') else None
        concurrency = dictionary.get('concurrency')
        host_type = dictionary.get('hostType')
        hosts = dictionary.get("hosts")
        local_mount_dir = dictionary.get('localMountDir')
        mount_view = dictionary.get('mountView')
        mounts = dictionary.get('mounts')
        preferred_control_nodes = dictionary.get("preferredControlNodes")
        restore_args = dictionary.get('restoreArgs')
        restore_job_arguments_map = None
        if dictionary.get('restoreJobArgumentsMap') != None:
            restore_job_arguments_map = list()
            for structure in dictionary.get('restoreJobArgumentsMap'):
                restore_job_arguments_map.append(cohesity_management_sdk.models.uda_recover_job_params_restore_job_arguments_map_entry.UdaRecoverJobParams_RestoreJobArgumentsMapEntry.from_dictionary(structure))
        run_start_time_usecs = dictionary.get('runStartTimeUsecs')
        script_dir = dictionary.get('scriptDir')
        source_args = dictionary.get('sourceArgs')
        source_arguments_map = None
        if dictionary.get('sourceArgumentsMap') != None:
            source_arguments_map = list()
            for structure in dictionary.get('sourceArgumentsMap'):
                source_arguments_map.append(cohesity_management_sdk.models.uda_recover_job_params_source_arguments_map_entry.UdaRecoverJobParams_SourceArgumentsMapEntry.from_dictionary(structure))
        source_type = dictionary.get('sourceType')
        uda_s_3_view_backup_properties = cohesity_management_sdk.models.uda_s_3_view_backup_properties.UdaS3ViewBackupProperties.from_dictionary(dictionary.get('udaS3ViewBackupProperties')) if dictionary.get('udaS3ViewBackupProperties') else None
        use_s_3_view = dictionary.get('useS3View')

        # Return an object of this model
        return cls(
            capabilities,
            concurrency,
            host_type,
            hosts,
            local_mount_dir,
            mount_view,
            mounts,
            preferred_control_nodes,
            restore_args,
            restore_job_arguments_map,
            run_start_time_usecs,
            script_dir,
            source_args,
            source_arguments_map,
            source_type,
            uda_s_3_view_backup_properties,
            use_s_3_view
)