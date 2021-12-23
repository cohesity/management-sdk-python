# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

import cohesity_management_sdk.models.archival_target
import cohesity_management_sdk.models.cloud_deploy_target
import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.universal_id_proto
import cohesity_management_sdk.models.restore_acropolis_vm_param
import cohesity_management_sdk.models.no_sql_recover_params
import cohesity_management_sdk.models.uda_recover_params

class RestoreObject(object):

    """Implementation of the 'RestoreObject' model.

    TODO: type model description here.

    Attributes:
        archival_target (ArchivalTarget): Message that specifies the details
            about an archival target (such as cloud or tape) where backup
            snapshots may be archived to.
        attempt_num (int): The attempt number of the job run to restore from.
        cloud_deploy_target (CloudDeployTarget): Message that specifies the
            details about CloudDeploy target where backup snapshots may be
            converted and stored.
        cloud_replication_target (CloudDeployTarget): Message that specifies
            the details about CloudDeploy target where backup snapshots may be
            converted and stored.
        entity (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        hydration_time_usecs (long|int): The time to which CDP logs hydrated.
            This field is currently only applicable to MongoDb. This field is
            used during restore as the 'start time' for copying the
            remaining cdp logs that are yet to be hydrated by agent.
        job_id (long|int): The job id from which to restore. This is used
            while communicating with yoda.
        job_instance_id (long|int): Id identifying a specific run to restore
            from. If this is not specified, and we need to restore from a run,
            the latest run is used. NOTE: This must be specified for
            RestoreFiles, RecoverDisks and GetVirtualDisks APIs.
        job_uid (UniversalIdProto): TODO: type description here.
        nosql_recover_params (NoSqlRecoverParams): This field contains params
            specific to the restore of a nosql entity.
        parent_source (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        point_in_time_restore_time_usecs (int): The time to which the object
            needs to be restored. If this is not set, then the object will be
            restored to the full/incremental snapshot. This is applicable only
            if the object is protected using CDP.
        recover_from_standby (bool): This field indicates if the object should
            be recovered from standby if it is enabled.
        restore_acropolis_vm_param (RestoreAcropolisVMParam): TODO: type
            description here.
        snapshot_relative_dir_path (string): The relative path to the
            directory containing the entity's snapshot.
        start_time_usecs (long|int): The start time of the specific job run.
            Iff 'job_instance_id' is set, this field must be set. In-memory
            indices on the Magneto master are laid-out by the start time of
            the job, and this is how the master pulls up a specific run. NOTE:
            This must be specified for RestoreFiles, RecoverDisks and
            GetVirtualDisks APIs
        uda_recover_params (UdaRecoverParams): This field contains params
            specific to the restore of a Uda entities.
        view_name (string): The name of the view where the object's snapshot
            is located.
        vm_had_independent_disks (bool): This is applicable only to VMs and is
            set to true when the VM being recovered or cloned contained
            independent disks when it was backed up.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "archival_target":'archivalTarget',
        "attempt_num":'attemptNum',
        "cloud_deploy_target":'cloudDeployTarget',
        "cloud_replication_target":'cloudReplicationTarget',
        "entity":'entity',
        "hydration_time_usecs":'hydrationTimeUsecs',
        "job_id":'jobId',
        "job_instance_id":'jobInstanceId',
        "job_uid":'jobUid',
        "nosql_recover_params":'nosqlRecoverParams',
        "parent_source":'parentSource',
        "point_in_time_restore_time_usecs":'pointInTimeRestoreTimeUsecs',
        "recover_from_standby":'recoverFromStandby',
        "restore_acropolis_vm_param":'restoreAcropolisVmParam',
        "snapshot_relative_dir_path":'snapshotRelativeDirPath',
        "start_time_usecs":'startTimeUsecs',
        "uda_recover_params":'udaRecoverParams',
        "view_name":'viewName',
        "vm_had_independent_disks":'vmHadIndependentDisks'
    }

    def __init__(self,
                 archival_target=None,
                 attempt_num=None,
                 cloud_deploy_target=None,
                 cloud_replication_target=None,
                 entity=None,
                 hydration_time_usecs=None,
                 job_id=None,
                 job_instance_id=None,
                 job_uid=None,
                 nosql_recover_params=None,
                 parent_source=None,
                 point_in_time_restore_time_usecs=None,
                 recover_from_standby=None,
                 restore_acropolis_vm_param=None,
                 snapshot_relative_dir_path=None,
                 start_time_usecs=None,
                 uda_recover_params=None,
                 view_name=None,
                 vm_had_independent_disks=None):
        """Constructor for the RestoreObject class"""

        # Initialize members of the class
        self.archival_target = archival_target
        self.attempt_num = attempt_num
        self.cloud_deploy_target = cloud_deploy_target
        self.cloud_replication_target = cloud_replication_target
        self.entity = entity
        self.hydration_time_usecs = hydration_time_usecs
        self.job_id = job_id
        self.job_instance_id = job_instance_id
        self.job_uid = job_uid
        self.nosql_recover_params = nosql_recover_params
        self.parent_source = parent_source
        self.point_in_time_restore_time_usecs = point_in_time_restore_time_usecs
        self.recover_from_standby = recover_from_standby
        self.restore_acropolis_vm_param = restore_acropolis_vm_param
        self.snapshot_relative_dir_path = snapshot_relative_dir_path
        self.start_time_usecs = start_time_usecs
        self.uda_recover_params = uda_recover_params
        self.view_name = view_name
        self.vm_had_independent_disks = vm_had_independent_disks


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
        attempt_num = dictionary.get('attemptNum')
        cloud_deploy_target = cohesity_management_sdk.models.cloud_deploy_target.CloudDeployTarget.from_dictionary(dictionary.get('cloudDeployTarget')) if dictionary.get('cloudDeployTarget') else None
        cloud_replication_target = cohesity_management_sdk.models.cloud_deploy_target.CloudDeployTarget.from_dictionary(dictionary.get('cloudReplicationTarget')) if dictionary.get('cloudReplicationTarget') else None
        entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('entity')) if dictionary.get('entity') else None
        hydration_time_usecs = dict.get('hydrationTimeUsecs')
        job_id = dictionary.get('jobId')
        job_instance_id = dictionary.get('jobInstanceId')
        job_uid = cohesity_management_sdk.models.universal_id_proto.UniversalIdProto.from_dictionary(dictionary.get('jobUid')) if dictionary.get('jobUid') else None
        nosql_recover_params = cohesity_management_sdk.models.no_sql_recover_params.NoSqlRecoverParams.from_dictionary(dictionary.get('nosqlRecoverParams')) if dictionary.get('nosqlRecoverParams') else None
        parent_source = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('parentSource')) if dictionary.get('parentSource') else None
        point_in_time_restore_time_usecs = dictionary.get('pointInTimeRestoreTimeUsecs')
        recover_from_standby = dictionary.get('recoverFromStandby')
        restore_acropolis_vm_param = cohesity_management_sdk.models.restore_acropolis_vm_param.RestoreAcropolisVMParam.from_dictionary(dictionary.get('restoreAcropolisVmParam')) if dictionary.get('restoreAcropolisVmParam') else None
        snapshot_relative_dir_path = dictionary.get('snapshotRelativeDirPath')
        start_time_usecs = dictionary.get('startTimeUsecs')
        uda_recover_params = cohesity_management_sdk.models.uda_recover_params.UdaRecoverParams.from_dictionary(dictionary.get('udaRecoverParams')) if dictionary.get('udaRecoverParams') else None
        view_name = dictionary.get('viewName')
        vm_had_independent_disks = dictionary.get('vmHadIndependentDisks')

        # Return an object of this model
        return cls(archival_target,
                   attempt_num,
                   cloud_deploy_target,
                   cloud_replication_target,
                   entity,
                   hydration_time_usecs,
                   job_id,
                   job_instance_id,
                   job_uid,
                   nosql_recover_params,
                   parent_source,
                   point_in_time_restore_time_usecs,
                   recover_from_standby,
                   restore_acropolis_vm_param,
                   snapshot_relative_dir_path,
                   start_time_usecs,
                   uda_recover_params,
                   view_name,
                   vm_had_independent_disks)


