# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.remote_protection_job_run_information
import cohesity_management_sdk.models.universal_id

class RemoteVaultSearchJobResults(object):

    """Implementation of the 'RemoteVaultSearchJobResults' model.

    Specifies detailed information about Job Runs of Protection Jobs found
    by a search Job when searching a remote Vault for archived data.

    Attributes:
        cluster_count (int): Specifies number of Clusters that have archived
            to the remote Vault that match the criteria specified in the
            search Job, up to this point in the search. If the search is
            complete, the total number of Clusters that have archived to the
            remote Vault and that match the search criteria for the search
            Job, are reported. If the search was not complete, a partial
            number is reported.
        cluster_match_string (string): Specifies the value of the
            clusterMatchSting if it was set in the original search Job.
        cookie (string): Specifies an opaque string to pass to the next
            request to get the next set of search results. This is provided to
            support pagination. If null, this is the last set of search
            results.
        end_time_usecs (long|int): Specifies the value of endTimeUsecs if it
            was set in the original search Job. End time is recorded as a Unix
            epoch Timestamp (in microseconds).
        error (string): Specifies the error message if the search fails.
        job_count (int): Specifies number of Protection Jobs that have
            archived to the remote Vault that match the criteria specified in
            the search Job. If the search is complete, the total number of
            Protection Jobs that have archived to the remote Vault and match
            the search criteria for the search Job, are reported. If the
            search is not complete, a partial number is reported.
        job_match_string (string): Specifies the value of the jobMatchSting if
            it was set in the original search Job.
        protection_jobs (list of RemoteProtectionJobRunInformation): Array of
            Protection Jobs.  Specifies a list of Protection Jobs that have
            archived data to a remote Vault and that also match the filter
            criteria.
        search_job_status (SearchJobStatusRemoteVaultSearchJobResultsEnum):
            Specifies the status of the search Job. 'kJobRunning' indicates
            that the Job/task is currently running. 'kJobFinished' indicates
            that the Job/task completed and finished. 'kJobFailed' indicates
            that the Job/task failed and did not complete. 'kJobCanceled'
            indicates that the Job/task was canceled. 'kJobPaused' indicates
            the Job/task is paused.
        search_job_uid (UniversalId): Specifies the unique id of the search
            Job assigned by the Cluster.
        start_time_usecs (long|int): Specifies the value of startTimeUsecs if
            it was set in the original search Job. Start time is recorded as a
            Unix epoch Timestamp (in microseconds).
        vault_id (long|int): Specifies the id of the remote Vault that was
            searched.
        vault_name (string): Specifies the name of the remote Vault that was
            searched.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cluster_count":'clusterCount',
        "cluster_match_string":'clusterMatchString',
        "cookie":'cookie',
        "end_time_usecs":'endTimeUsecs',
        "error":'error',
        "job_count":'jobCount',
        "job_match_string":'jobMatchString',
        "protection_jobs":'protectionJobs',
        "search_job_status":'searchJobStatus',
        "search_job_uid":'searchJobUid',
        "start_time_usecs":'startTimeUsecs',
        "vault_id":'vaultId',
        "vault_name":'vaultName'
    }

    def __init__(self,
                 cluster_count=None,
                 cluster_match_string=None,
                 cookie=None,
                 end_time_usecs=None,
                 error=None,
                 job_count=None,
                 job_match_string=None,
                 protection_jobs=None,
                 search_job_status=None,
                 search_job_uid=None,
                 start_time_usecs=None,
                 vault_id=None,
                 vault_name=None):
        """Constructor for the RemoteVaultSearchJobResults class"""

        # Initialize members of the class
        self.cluster_count = cluster_count
        self.cluster_match_string = cluster_match_string
        self.cookie = cookie
        self.end_time_usecs = end_time_usecs
        self.error = error
        self.job_count = job_count
        self.job_match_string = job_match_string
        self.protection_jobs = protection_jobs
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
        cluster_match_string = dictionary.get('clusterMatchString')
        cookie = dictionary.get('cookie')
        end_time_usecs = dictionary.get('endTimeUsecs')
        error = dictionary.get('error')
        job_count = dictionary.get('jobCount')
        job_match_string = dictionary.get('jobMatchString')
        protection_jobs = None
        if dictionary.get('protectionJobs') != None:
            protection_jobs = list()
            for structure in dictionary.get('protectionJobs'):
                protection_jobs.append(cohesity_management_sdk.models.remote_protection_job_run_information.RemoteProtectionJobRunInformation.from_dictionary(structure))
        search_job_status = dictionary.get('searchJobStatus')
        search_job_uid = cohesity_management_sdk.models.universal_id.UniversalId.from_dictionary(dictionary.get('searchJobUid')) if dictionary.get('searchJobUid') else None
        start_time_usecs = dictionary.get('startTimeUsecs')
        vault_id = dictionary.get('vaultId')
        vault_name = dictionary.get('vaultName')

        # Return an object of this model
        return cls(cluster_count,
                   cluster_match_string,
                   cookie,
                   end_time_usecs,
                   error,
                   job_count,
                   job_match_string,
                   protection_jobs,
                   search_job_status,
                   search_job_uid,
                   start_time_usecs,
                   vault_id,
                   vault_name)


