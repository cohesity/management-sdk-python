# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.universal_id

class RemoteVaultSearchJobInformation(object):

    """Implementation of the 'RemoteVaultSearchJobInformation' model.

    Specifies information about a search of a remote Vault.

    Attributes:
        cluster_count (int): Specifies number of Clusters that have archived
            to the remote Vault and match the search criteria for this job, up
            to this point in the search. If the search is complete, the total
            number of Clusters that have archived to the remote Vault and that
            match the search criteria for this search Job, are reported. If
            the search is not complete, a partial number is reported.
        end_time_usecs (long|int): Specifies the end time of the search as a
            Unix epoch Timestamp (in microseconds) if the search Job has
            completed.
        error (string): Specifies the error message reported when a search
            fails.
        job_count (int): Specifies number of Protection Jobs that have
            archived to the remote Vault and match the search criteria for
            this search Job, up to this point in the search. If the search is
            complete, the total number of Protection Jobs that have archived
            to the remote Vault and that match the search criteria for this
            search Job, are reported. If the search is not complete, a partial
            number is reported.
        name (string): Specifies the name of the search Job.
        search_job_status (SearchJobStatusEnum): Specifies the status of the
            search. 'kJobRunning' indicates that the Job/task is currently
            running. 'kJobFinished' indicates that the Job/task completed and
            finished. 'kJobFailed' indicates that the Job/task failed and did
            not complete. 'kJobCanceled' indicates that the Job/task was
            canceled. 'kJobPaused' indicates the Job/task is paused.
        search_job_uid (UniversalId): Specifies the unique id assigned to the
            search Job by the Cluster.
        start_time_usecs (long|int): Specifies the start time of the search as
            a Unix epoch Timestamp (in microseconds).
        vault_id (long|int): Specifies the id of the remote Vault (External
            Target) that was searched.
        vault_name (string): Specifies the name of the remote Vault (External
            Target) that was searched.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cluster_count":'clusterCount',
        "end_time_usecs":'endTimeUsecs',
        "error":'error',
        "job_count":'jobCount',
        "name":'name',
        "search_job_status":'searchJobStatus',
        "search_job_uid":'searchJobUid',
        "start_time_usecs":'startTimeUsecs',
        "vault_id":'vaultId',
        "vault_name":'vaultName'
    }

    def __init__(self,
                 cluster_count=None,
                 end_time_usecs=None,
                 error=None,
                 job_count=None,
                 name=None,
                 search_job_status=None,
                 search_job_uid=None,
                 start_time_usecs=None,
                 vault_id=None,
                 vault_name=None):
        """Constructor for the RemoteVaultSearchJobInformation class"""

        # Initialize members of the class
        self.cluster_count = cluster_count
        self.end_time_usecs = end_time_usecs
        self.error = error
        self.job_count = job_count
        self.name = name
        self.search_job_status = search_job_status
        self.search_job_uid = search_job_uid
        self.start_time_usecs = start_time_usecs
        self.vault_id = vault_id
        self.vault_name = vault_name


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
        cluster_count = dictionary.get('clusterCount')
        end_time_usecs = dictionary.get('endTimeUsecs')
        error = dictionary.get('error')
        job_count = dictionary.get('jobCount')
        name = dictionary.get('name')
        search_job_status = dictionary.get('searchJobStatus')
        search_job_uid = cohesity_management_sdk.models.universal_id.UniversalId.from_dictionary(dictionary.get('searchJobUid')) if dictionary.get('searchJobUid') else None
        start_time_usecs = dictionary.get('startTimeUsecs')
        vault_id = dictionary.get('vaultId')
        vault_name = dictionary.get('vaultName')

        # Return an object of this model
        return cls(cluster_count,
                   end_time_usecs,
                   error,
                   job_count,
                   name,
                   search_job_status,
                   search_job_uid,
                   start_time_usecs,
                   vault_id,
                   vault_name)


