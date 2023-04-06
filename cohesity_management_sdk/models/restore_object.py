# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.archival_target
import cohesity_management_sdk.models.cloud_deploy_target
import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.no_sql_recover_params
import cohesity_management_sdk.models.restore_acropolis_vm_param
import cohesity_management_sdk.models.restore_exchange_params
import cohesity_management_sdk.models.restore_vapp_info
import cohesity_management_sdk.models.sfdc_recover_params
import cohesity_management_sdk.models.uda_recover_params
import cohesity_management_sdk.models.universal_id_proto


class RestoreObject(object):

    """Implementation of the 'RestoreObject' model.

    TODO: type description here.


    Attributes:

        archival_target (ArchivalTarget): This field must be set if the object
            is to be restored/retrieved from an archive.
        attempt_num (int): The attempt number of the job run to restore from.
        backup_type (int): Backup type of corresponding backup run. Currently,
            this is only populated for restore tasks.
        cloud_deploy_target (CloudDeployTarget): This field must be set if the
            restore type is kDeployVMs and the object is to be deployed to
            cloud using a previously converted image.
        cloud_replication_target (CloudDeployTarget): This field must be set if
            the restore type is kReplicateSnapshots and the snapshots need to
            be repliated accross regions in the Cloud.
        entity (EntityProto): The entity to restore. If this is not specified,
            all entities from job id will be restored (from the latest
            snapshot). If specified, this can only have leaf-level entities.
            Notes: This must be specified for RestoreFiles task. Disable object
            rewriting in the outgoing API path. This is needed to preserve the
            content of objects().entity() as it must reflect the Entity object
            as it was at the point the restore task was submitted.
        hydration_time_usecs (long|int): The time to which CDP logs hydrated.
            This field is currently only applicable to MongoDb. This field is
            used during restore as the 'start time' for copying the remaining
            cdp logs that are yet to be hydrated by agent.
        job_id (long|int): The job id from which to restore. This is used while
            communicating with yoda.
        job_instance_id (long|int): Id identifying a specific run to restore
            from. If this is not specified, and we need to restore from a run,
            the latest run is used. NOTE: This must be specified for
            RestoreFiles, RecoverDisks and GetVirtualDisks APIs.
        job_uid (UniversalIdProto): The universal id of the job from which to
            restore. Caller can set this as local, remote or primary job_uid.
            Magneto will will look for this UID across all local/remote/primary
            jobs. See ENG-231303 for more context.
        nosql_recover_params (NoSqlRecoverParams): This field contains params
            specific to the restore of a nosql entity.
        parent_source (EntityProto): The registered source that was managing
            the entity being restored.
        pit_preferred_archival_target (ArchivalTarget): Preferred archival
            target for the point in time restore.
        point_in_time_restore_time_usecs (long|int): The time to which the
            object needs to be restored. If this is not set, then the object
            will be restored to the full/incremental snapshot. This is
            applicable only if the object is protected using CDP.
        recover_from_standby (bool): This field indicates if the object should
            be recovered from standby if it is enabled.
        restore_acropolis_vm_param (RestoreAcropolisVMParam): This field
            contains params specific to the restore of an Acropolis VM.
        restore_exchange_params (RestoreExchangeParams): This field contains
            params specific to the restore of a Exchange entities.
        restore_vapp_info (RestoreVappInfo): This field contains params
            specific to restore of VCD vApp entity.
        sfdc_recover_params (SfdcRecoverParams): This field contains params
            specific to the restore of a Sfdc entities.
        snapshot_relative_dir_path (string): The relative path to the directory
            containing the entity's snapshot.
        start_time_usecs (long|int): The start time of the specific job run.
            Iff 'job_instance_id' is set, this field must be set. In-memory
            indices on the Magneto master are laid-out by the start time of the
            job, and this is how the master pulls up a specific run. NOTE: This
            must be specified for RestoreFiles, RecoverDisks and
            GetVirtualDisks APIs
        uda_recover_params (UdaRecoverParams): This field contains params
            specific to the restore of a Uda entities.
        view_name (string): The name of the view where the object's snapshot is
            located.
        vm_had_independent_disks (bool): This is applicable only to VMs and is
            set to true when the VM being recovered or cloned contained
            independent disks when it was backed up.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "archival_target":'archivalTarget',
        "attempt_num":'attemptNum',
        "backup_type":'backupType',
        "cloud_deploy_target":'cloudDeployTarget',
        "cloud_replication_target":'cloudReplicationTarget',
        "entity":'entity',
        "hydration_time_usecs":'hydrationTimeUsecs',
        "job_id":'jobId',
        "job_instance_id":'jobInstanceId',
        "job_uid":'jobUid',
        "nosql_recover_params":'nosqlRecoverParams',
        "parent_source":'parentSource',
        "pit_preferred_archival_target":'pitPreferredArchivalTarget',
        "point_in_time_restore_time_usecs":'pointInTimeRestoreTimeUsecs',
        "recover_from_standby":'recoverFromStandby',
        "restore_acropolis_vm_param":'restoreAcropolisVmParam',
        "restore_exchange_params":'restoreExchangeParams',
        "restore_vapp_info":'restoreVappInfo',
        "sfdc_recover_params":'sfdcRecoverParams',
        "snapshot_relative_dir_path":'snapshotRelativeDirPath',
        "start_time_usecs":'startTimeUsecs',
        "uda_recover_params":'udaRecoverParams',
        "view_name":'viewName',
        "vm_had_independent_disks":'vmHadIndependentDisks',
    }
    def __init__(self,
                 archival_target=None,
                 attempt_num=None,
                 backup_type=None,
                 cloud_deploy_target=None,
                 cloud_replication_target=None,
                 entity=None,
                 hydration_time_usecs=None,
                 job_id=None,
                 job_instance_id=None,
                 job_uid=None,
                 nosql_recover_params=None,
                 parent_source=None,
                 pit_preferred_archival_target=None,
                 point_in_time_restore_time_usecs=None,
                 recover_from_standby=None,
                 restore_acropolis_vm_param=None,
                 restore_exchange_params=None,
                 restore_vapp_info=None,
                 sfdc_recover_params=None,
                 snapshot_relative_dir_path=None,
                 start_time_usecs=None,
                 uda_recover_params=None,
                 view_name=None,
                 vm_had_independent_disks=None,
            ):

        """Constructor for the RestoreObject class"""

        # Initialize members of the class
        self.archival_target = archival_target
        self.attempt_num = attempt_num
        self.backup_type = backup_type
        self.cloud_deploy_target = cloud_deploy_target
        self.cloud_replication_target = cloud_replication_target
        self.entity = entity
        self.hydration_time_usecs = hydration_time_usecs
        self.job_id = job_id
        self.job_instance_id = job_instance_id
        self.job_uid = job_uid
        self.nosql_recover_params = nosql_recover_params
        self.parent_source = parent_source
        self.pit_preferred_archival_target = pit_preferred_archival_target
        self.point_in_time_restore_time_usecs = point_in_time_restore_time_usecs
        self.recover_from_standby = recover_from_standby
        self.restore_acropolis_vm_param = restore_acropolis_vm_param
        self.restore_exchange_params = restore_exchange_params
        self.restore_vapp_info = restore_vapp_info
        self.sfdc_recover_params = sfdc_recover_params
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
        backup_type = dictionary.get('backupType')
        cloud_deploy_target = cohesity_management_sdk.models.cloud_deploy_target.CloudDeployTarget.from_dictionary(dictionary.get('cloudDeployTarget')) if dictionary.get('cloudDeployTarget') else None
        cloud_replication_target = cohesity_management_sdk.models.cloud_deploy_target.CloudDeployTarget.from_dictionary(dictionary.get('cloudReplicationTarget')) if dictionary.get('cloudReplicationTarget') else None
        entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('entity')) if dictionary.get('entity') else None
        hydration_time_usecs = dictionary.get('hydrationTimeUsecs')
        job_id = dictionary.get('jobId')
        job_instance_id = dictionary.get('jobInstanceId')
        job_uid = cohesity_management_sdk.models.universal_id_proto.UniversalIdProto.from_dictionary(dictionary.get('jobUid')) if dictionary.get('jobUid') else None
        nosql_recover_params = cohesity_management_sdk.models.no_sql_recover_params.NoSqlRecoverParams.from_dictionary(dictionary.get('nosqlRecoverParams')) if dictionary.get('nosqlRecoverParams') else None
        parent_source = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('parentSource')) if dictionary.get('parentSource') else None
        pit_preferred_archival_target = cohesity_management_sdk.models.archival_target.ArchivalTarget.from_dictionary(dictionary.get('pitPreferredArchivalTarget')) if dictionary.get('pitPreferredArchivalTarget') else None
        point_in_time_restore_time_usecs = dictionary.get('pointInTimeRestoreTimeUsecs')
        recover_from_standby = dictionary.get('recoverFromStandby')
        restore_acropolis_vm_param = cohesity_management_sdk.models.restore_acropolis_vm_param.RestoreAcropolisVMParam.from_dictionary(dictionary.get('restoreAcropolisVmParam')) if dictionary.get('restoreAcropolisVmParam') else None
        restore_exchange_params = cohesity_management_sdk.models.restore_exchange_params.RestoreExchangeParams.from_dictionary(dictionary.get('restoreExchangeParams')) if dictionary.get('restoreExchangeParams') else None
        restore_vapp_info = cohesity_management_sdk.models.restore_vapp_info.RestoreVappInfo.from_dictionary(dictionary.get('restoreVappInfo')) if dictionary.get('restoreVappInfo') else None
        sfdc_recover_params = cohesity_management_sdk.models.sfdc_recover_params.SfdcRecoverParams.from_dictionary(dictionary.get('sfdcRecoverParams')) if dictionary.get('sfdcRecoverParams') else None
        snapshot_relative_dir_path = dictionary.get('snapshotRelativeDirPath')
        start_time_usecs = dictionary.get('startTimeUsecs')
        uda_recover_params = cohesity_management_sdk.models.uda_recover_params.UdaRecoverParams.from_dictionary(dictionary.get('udaRecoverParams')) if dictionary.get('udaRecoverParams') else None
        view_name = dictionary.get('viewName')
        vm_had_independent_disks = dictionary.get('vmHadIndependentDisks')

        # Return an object of this model
        return cls(
            archival_target,
            attempt_num,
            backup_type,
            cloud_deploy_target,
            cloud_replication_target,
            entity,
            hydration_time_usecs,
            job_id,
            job_instance_id,
            job_uid,
            nosql_recover_params,
            parent_source,
            pit_preferred_archival_target,
            point_in_time_restore_time_usecs,
            recover_from_standby,
            restore_acropolis_vm_param,
            restore_exchange_params,
            restore_vapp_info,
            sfdc_recover_params,
            snapshot_relative_dir_path,
            start_time_usecs,
            uda_recover_params,
            view_name,
            vm_had_independent_disks
)