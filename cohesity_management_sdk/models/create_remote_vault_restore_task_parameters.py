# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.index_and_snapshots
import cohesity_management_sdk.models.universal_id

class CreateRemoteVaultRestoreTaskParameters(object):

    """Implementation of the 'CreateRemoteVaultRestoreTaskParameters' model.

    Specifies settings required to create a task that restores the
    index and/or the Snapshots of a Protection Job from a remote Vault
    to the current Cluster.

    Attributes:
        glacier_retrieval_type (GlacierRetrievalTypeEnum): Specifies the way
            data needs to be retrieved from the external target. This
            information will be filled in by Iris and Magneto will pass it
            along to the Icebox as it is to support bulk retrieval from
            Glacier. Specifies the type of Restore Task.  'kStandard'
            specifies retrievals that allow to access any of your archives
            within several hours. Standard retrievals typically complete
            within 3–5 hours.This is the default option for retrieval requests
            that do not specify the retrieval option. 'kBulk' specifies
            retrievals that are Glacier’s lowest-cost retrieval option, which
            can be use to retrieve large amounts, even petabytes, of data
            inexpensively in a day. Bulk retrieval typically complete within
            5–12 hours. 'kExpedited' specifies retrievals that allows to
            quickly access your data when occasional urgent requests for a
            subset of archives are required. For all but the largest archives
            (250 MB+), data accessed using Expedited retrievals are typically
            made available within 1–5 minutes.
        restore_objects (list of IndexAndSnapshots): Array of Restore Objects.
            Specifies the list of Snapshots and the index to be restored from
            the remote Vault. The data on the remote Vault may have been
            originally archived from multiple remote Clusters.
        search_job_uid (UniversalId): Specifies the unique id of the remote
            Vault search Job.
        task_name (string): Specifies a name of the restore task.
        vault_id (long|int): Specifies the id of the Vault that contains the
            index and Snapshots to restore to the current Cluster. This is the
            id assigned by the Cohesity Cluster when Vault was registered as
            an External Target.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "search_job_uid":'searchJobUid',
        "task_name":'taskName',
        "vault_id":'vaultId',
        "glacier_retrieval_type":'glacierRetrievalType',
        "restore_objects":'restoreObjects'
    }

    def __init__(self,
                 search_job_uid=None,
                 task_name=None,
                 vault_id=None,
                 glacier_retrieval_type=None,
                 restore_objects=None):
        """Constructor for the CreateRemoteVaultRestoreTaskParameters class"""

        # Initialize members of the class
        self.glacier_retrieval_type = glacier_retrieval_type
        self.restore_objects = restore_objects
        self.search_job_uid = search_job_uid
        self.task_name = task_name
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
        search_job_uid = cohesity_management_sdk.models.universal_id.UniversalId.from_dictionary(dictionary.get('searchJobUid')) if dictionary.get('searchJobUid') else None
        task_name = dictionary.get('taskName')
        vault_id = dictionary.get('vaultId')
        glacier_retrieval_type = dictionary.get('glacierRetrievalType')
        restore_objects = None
        if dictionary.get('restoreObjects') != None:
            restore_objects = list()
            for structure in dictionary.get('restoreObjects'):
                restore_objects.append(cohesity_management_sdk.models.index_and_snapshots.IndexAndSnapshots.from_dictionary(structure))

        # Return an object of this model
        return cls(search_job_uid,
                   task_name,
                   vault_id,
                   glacier_retrieval_type,
                   restore_objects)


