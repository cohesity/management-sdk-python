# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.backup_run
import cohesity_management_sdk.models.copy_run
import cohesity_management_sdk.models.universal_id

class ProtectionRunInstance(object):

    """Implementation of the 'ProtectionRunInstance' model.

    Specifies the status of one Job Run.
    A Job Run can have one Backup Run and zero or more Copy Runs.

    Attributes:
        backup_run (BackupRun): Specifies details about the Backup task for a
            Job Run. A Backup task captures the original backup snapshots for
            each Protection Source in the Job.
        copy_run (list of CopyRun): Array of Copy Run Tasks.  Specifies
            details about the Copy tasks of this Job Run. A Copy task copies
            the captured snapshots to an external target or a Remote Cohesity
            Cluster.
        job_id (long|int): Specifies the id of the Protection Job that was
            run.
        job_name (string): Specifies the name of the Protection Job name that
            was run.
        job_uid (UniversalId): Specifies the globally unique id of the
            Protection Job that was run.
        protection_shell_info (ProtectionShellInfo): Specifies the shell
            information about the protection run. This will only be populated
            if OnlyReturnShellInfo is sent as true.
        view_box_id (long|int): Specifies the Storage Domain (View Box) to
            store the backed up data. Specify the id of the Storage Domain
            (View Box).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "backup_run":'backupRun',
        "copy_run":'copyRun',
        "job_id":'jobId',
        "job_name":'jobName',
        "job_uid":'jobUid',
        "view_box_id":'viewBoxId'
    }

    def __init__(self,
                 backup_run=None,
                 copy_run=None,
                 job_id=None,
                 job_name=None,
                 job_uid=None,
                 view_box_id=None):
        """Constructor for the ProtectionRunInstance class"""

        # Initialize members of the class
        self.backup_run = backup_run
        self.copy_run = copy_run
        self.job_id = job_id
        self.job_name = job_name
        self.job_uid = job_uid
        self.view_box_id = view_box_id


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
        backup_run = cohesity_management_sdk.models.backup_run.BackupRun.from_dictionary(dictionary.get('backupRun')) if dictionary.get('backupRun') else None
        copy_run = None
        if dictionary.get('copyRun') != None:
            copy_run = list()
            for structure in dictionary.get('copyRun'):
                copy_run.append(cohesity_management_sdk.models.copy_run.CopyRun.from_dictionary(structure))
        job_id = dictionary.get('jobId')
        job_name = dictionary.get('jobName')
        job_uid = cohesity_management_sdk.models.universal_id.UniversalId.from_dictionary(dictionary.get('jobUid')) if dictionary.get('jobUid') else None
        view_box_id = dictionary.get('viewBoxId')

        # Return an object of this model
        return cls(backup_run,
                   copy_run,
                   job_id,
                   job_name,
                   job_uid,
                   view_box_id)


