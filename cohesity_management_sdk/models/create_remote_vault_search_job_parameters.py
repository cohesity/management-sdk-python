# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.vault_encryption_key


class CreateRemoteVaultSearchJobParameters(object):

    """Implementation of the 'CreateRemoteVaultSearchJobParameters' model.

    Specifies settings required to create a search of a remote Vault for data
    that has been archived from other Clusters.


    Attributes:

        job_uids (list of string): Filter by specifying a list of remote job
            uids in form of clusterId:clusterIncarnationId:jobId.
        cluster_id (long|int): Filter by specifying a Cluster id.
        cluster_match_string (string): Filter by specifying a Cluster name
            prefix string. Only Clusters with names that start with this prefix
            string are returned in the search result. If not set, all Clusters
            archiving data to the Vault are returned in the search results.
        encryption_keys (list of VaultEncryptionKey): Array of Encryption Keys.
             Specifies an optional list of encryption keys that may be needed
            to search and restore data that was archived to a remote Vault.
            Archived data cannot be searched or restored without the
            corresponding encryption key used by the original Cluster to
            archive the data. Encryption keys can be uploaded using the REST
            API public/remoteVaults/encryptionKeys operation. If the key is
            already uploaded, this field does not need to be specified.
        end_time_usecs (long|int): Filter by a end time specified as a Unix
            epoch Timestamp (in microseconds). Only Job Runs that completed
            before the specified end time are included in the search results.
        job_match_string (string): Filter by specifying a Protection Job name
            prefix string. Only Protection Jobs with names that start with this
            prefix string are returned in the search result. If not set, all
            Protection Jobs archiving data to the Vault are returned in the
            search results.
        search_job_name (string, required): Specifies the search Job name.
        start_time_usecs (long|int): Filter by a start time specified as a Unix
            epoch Timestamp (in microseconds). Only Job Runs that started after
            the specified time are included in the search results.
        vault_id (long|int, required): Specifies the id of the Vault to search.
            This id was assigned by the local Cohesity Cluster when Vault was
            registered as an External Target.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "job_uids":'JobUids',
        "cluster_id":'clusterId',
        "cluster_match_string":'clusterMatchString',
        "encryption_keys":'encryptionKeys',
        "end_time_usecs":'endTimeUsecs',
        "job_match_string":'jobMatchString',
        "search_job_name":'searchJobName',
        "start_time_usecs":'startTimeUsecs',
        "vault_id":'vaultId',
    }
    def __init__(self,
                 job_uids=None,
                 cluster_id=None,
                 cluster_match_string=None,
                 encryption_keys=None,
                 end_time_usecs=None,
                 job_match_string=None,
                 search_job_name=None,
                 start_time_usecs=None,
                 vault_id=None,
            ):

        """Constructor for the CreateRemoteVaultSearchJobParameters class"""

        # Initialize members of the class
        self.job_uids = job_uids
        self.cluster_id = cluster_id
        self.cluster_match_string = cluster_match_string
        self.encryption_keys = encryption_keys
        self.end_time_usecs = end_time_usecs
        self.job_match_string = job_match_string
        self.search_job_name = search_job_name
        self.start_time_usecs = start_time_usecs
        self.vault_id = vault_id

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
        job_uids = dictionary.get("JobUids")
        cluster_id = dictionary.get('clusterId')
        cluster_match_string = dictionary.get('clusterMatchString')
        encryption_keys = None
        if dictionary.get('encryptionKeys') != None:
            encryption_keys = list()
            for structure in dictionary.get('encryptionKeys'):
                encryption_keys.append(cohesity_management_sdk.models.vault_encryption_key.VaultEncryptionKey.from_dictionary(structure))
        end_time_usecs = dictionary.get('endTimeUsecs')
        job_match_string = dictionary.get('jobMatchString')
        search_job_name = dictionary.get('searchJobName')
        start_time_usecs = dictionary.get('startTimeUsecs')
        vault_id = dictionary.get('vaultId')

        # Return an object of this model
        return cls(
            job_uids,
            cluster_id,
            cluster_match_string,
            encryption_keys,
            end_time_usecs,
            job_match_string,
            search_job_name,
            start_time_usecs,
            vault_id
)