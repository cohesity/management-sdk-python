# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.protection_job_summary
import cohesity_management_sdk.models.protection_source
import cohesity_management_sdk.models.protection_source_uid

class ProtectionSourceResponse(object):

    """Implementation of the 'ProtectionSourceResponse' model.

    Specifies the information about the individual object from search api
    response.

    Attributes:
        jobs (list of ProtectionJobSummary): Specifies the list of Protection
            Jobs that protect the object.
        logical_size_in_bytes (long|int): Specifies the logical size of
            Protection Source in bytes.
        parent_source (ProtectionSource): Specifies a generic structure that
            represents a node in the Protection Source tree. Node details will
            depend on the environment of the Protection Source.
        protection_source_uid_list (list of ProtectionSourceUid): Specifies
            the list of universal ids of the Protection Source.
        source (ProtectionSource): Specifies a generic structure that
            represents a node in the Protection Source tree. Node details will
            depend on the environment of the Protection Source.
        uuid (string): Specifies the unique id of the Protection Source.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "jobs":'jobs',
        "logical_size_in_bytes":'logicalSizeInBytes',
        "parent_source":'parentSource',
        "protection_source_uid_list":'protectionSourceUidList',
        "source":'source',
        "uuid":'uuid'
    }

    def __init__(self,
                 jobs=None,
                 logical_size_in_bytes=None,
                 parent_source=None,
                 protection_source_uid_list=None,
                 source=None,
                 uuid=None):
        """Constructor for the ProtectionSourceResponse class"""

        # Initialize members of the class
        self.jobs = jobs
        self.logical_size_in_bytes = logical_size_in_bytes
        self.parent_source = parent_source
        self.protection_source_uid_list = protection_source_uid_list
        self.source = source
        self.uuid = uuid


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
        jobs = None
        if dictionary.get('jobs') != None:
            jobs = list()
            for structure in dictionary.get('jobs'):
                jobs.append(cohesity_management_sdk.models.protection_job_summary.ProtectionJobSummary.from_dictionary(structure))
        logical_size_in_bytes = dictionary.get('logicalSizeInBytes')
        parent_source = cohesity_management_sdk.models.protection_source.ProtectionSource.from_dictionary(dictionary.get('parentSource')) if dictionary.get('parentSource') else None
        protection_source_uid_list = None
        if dictionary.get('protectionSourceUidList') != None:
            protection_source_uid_list = list()
            for structure in dictionary.get('protectionSourceUidList'):
                protection_source_uid_list.append(cohesity_management_sdk.models.protection_source_uid.ProtectionSourceUid.from_dictionary(structure))
        source = cohesity_management_sdk.models.protection_source.ProtectionSource.from_dictionary(dictionary.get('source')) if dictionary.get('source') else None
        uuid = dictionary.get('uuid')

        # Return an object of this model
        return cls(jobs,
                   logical_size_in_bytes,
                   parent_source,
                   protection_source_uid_list,
                   source,
                   uuid)


