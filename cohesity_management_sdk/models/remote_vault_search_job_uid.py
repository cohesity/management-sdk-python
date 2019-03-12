# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.unique_global_id

class RemoteVaultSearchJobUid(object):

    """Implementation of the 'Remote Vault Search Job Uid.' model.

    Specifies the Uid of the Job created to search the
    remote vault.

    Attributes:
        search_job_uid (UniqueGlobalId): Specifies the unique id assigned for
            the search Job on the Cluster.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "search_job_uid":'searchJobUid'
    }

    def __init__(self,
                 search_job_uid=None):
        """Constructor for the RemoteVaultSearchJobUid class"""

        # Initialize members of the class
        self.search_job_uid = search_job_uid


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
        search_job_uid = cohesity_management_sdk.models.unique_global_id.UniqueGlobalId.from_dictionary(dictionary.get('searchJobUid')) if dictionary.get('searchJobUid') else None

        # Return an object of this model
        return cls(search_job_uid)


