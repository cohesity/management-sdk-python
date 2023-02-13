# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.archival_external_target
import cohesity_management_sdk.models.cloud_deploy_target_details
import cohesity_management_sdk.models.universal_id
import cohesity_management_sdk.models.protection_source

class RestoreInfo(object):

    """Implementation of the 'RestoreInfo' model.

    Specifies the info regarding a full SQL snapshot.

    Attributes:
        archival_target (ArchivalExternalTarget): Specifies settings about the
            Archival External Target (such as Tape or AWS).
        attempt_number (int): Specifies the attempt number.
        cloud_deploy_target (CloudDeployTargetDetails): Message that specifies
            the details about CloudDeploy target where backup snapshots may be
            converted and stored.
        job_run_id (long|int): Specifies the id of the job run.
        job_uid (UniversalId): Specifies an id for an object that is unique
            across Cohesity Clusters. The id is composite of all the ids
            listed below.
        parent_source (ProtectionSource): Specifies a generic structure that
            represents a node in the Protection Source tree. Node details will
            depend on the environment of the Protection Source.
        restore_time_usecs (int): This field specifies the time in to which
            the object needs to be restored.
            This filed is only applicable when object is being backeup using
            CDP feature.
        snapshot_relative_dir_path (string): Specifies the relative path of
            the snapshot directory.
        source (ProtectionSource): Specifies a generic structure that
            represents a node in the Protection Source tree. Node details will
            depend on the environment of the Protection Source.
        start_time_usecs (long|int): Specifies the start time specified as a
            Unix epoch Timestamp (in microseconds).
        view_name (string): Specifies the name of the view.
        vm_had_independent_disks (bool): Specifies if the VM had independent
            disks.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "archival_target":'archivalTarget',
        "attempt_number":'attemptNumber',
        "cloud_deploy_target":'cloudDeployTarget',
        "job_run_id":'jobRunId',
        "job_uid":'jobUid',
        "parent_source":'parentSource',
        "restore_time_usecs":'restoreTimeUsecs',
        "snapshot_relative_dir_path":'snapshotRelativeDirPath',
        "source":'source',
        "start_time_usecs":'startTimeUsecs',
        "view_name":'viewName',
        "vm_had_independent_disks":'vmHadIndependentDisks'
    }

    def __init__(self,
                 archival_target=None,
                 attempt_number=None,
                 cloud_deploy_target=None,
                 job_run_id=None,
                 job_uid=None,
                 parent_source=None,
                 restore_time_usecs=None,
                 snapshot_relative_dir_path=None,
                 source=None,
                 start_time_usecs=None,
                 view_name=None,
                 vm_had_independent_disks=None):
        """Constructor for the RestoreInfo class"""

        # Initialize members of the class
        self.archival_target = archival_target
        self.attempt_number = attempt_number
        self.cloud_deploy_target = cloud_deploy_target
        self.job_run_id = job_run_id
        self.job_uid = job_uid
        self.parent_source = parent_source
        self.restore_time_usecs = restore_time_usecs
        self.snapshot_relative_dir_path = snapshot_relative_dir_path
        self.source = source
        self.start_time_usecs = start_time_usecs
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
        archival_target = cohesity_management_sdk.models.archival_external_target.ArchivalExternalTarget.from_dictionary(dictionary.get('archivalTarget')) if dictionary.get('archivalTarget') else None
        attempt_number = dictionary.get('attemptNumber')
        cloud_deploy_target = cohesity_management_sdk.models.cloud_deploy_target_details.CloudDeployTargetDetails.from_dictionary(dictionary.get('cloudDeployTarget')) if dictionary.get('cloudDeployTarget') else None
        job_run_id = dictionary.get('jobRunId')
        job_uid = cohesity_management_sdk.models.universal_id.UniversalId.from_dictionary(dictionary.get('jobUid')) if dictionary.get('jobUid') else None
        parent_source = cohesity_management_sdk.models.protection_source.ProtectionSource.from_dictionary(dictionary.get('parentSource')) if dictionary.get('parentSource') else None
        restore_time_usecs = dictionary.get('restoreTimeUsecs')
        snapshot_relative_dir_path = dictionary.get('snapshotRelativeDirPath')
        source = cohesity_management_sdk.models.protection_source.ProtectionSource.from_dictionary(dictionary.get('source')) if dictionary.get('source') else None
        start_time_usecs = dictionary.get('startTimeUsecs')
        view_name = dictionary.get('viewName')
        vm_had_independent_disks = dictionary.get('vmHadIndependentDisks')

        # Return an object of this model
        return cls(archival_target,
                   attempt_number,
                   cloud_deploy_target,
                   job_run_id,
                   job_uid,
                   parent_source,
                   restore_time_usecs,
                   snapshot_relative_dir_path,
                   source,
                   start_time_usecs,
                   view_name,
                   vm_had_independent_disks)


