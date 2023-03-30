# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.common_job_info
import cohesity_management_sdk.models.universal_id


class CloudDomainMigrationQueryResult(object):

    """Implementation of the 'CloudDomainMigrationQueryResult' model.

    CloudDomainMigrationQueryResult represents the info returned while querying
    cloud domain migration.


    Attributes:

        app_job_uid_list (list of UniversalId): Specifies the list of the
            application jobs discovered.
        cloud_domain_id (long|int): Specifies the Id of a specific cloud domain
            present inside the vault, that needs to be migrated. If not set,
            all cloud domains found in the vault or under the
            'domain_namespace' specified in CADConfig will be migrated.
        common_job_info (CommonJobInfo): Specifies the common job info.
        is_cad_mode (bool): Specifies if the migration mode is CAD or not.
        is_migration_ready (bool): Specifies whether the protection
            jobs/objects in the cloud domain are ready to be migrated. This is
            set after required snap trees have been downloaded and CM tables
            have been populated.
        num_of_bytes_downloaded (long|int): Specifies the Number of bytes
            downloaded by this job. The downloaded bytes are for reading
            metadata object, data objects and index files.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "app_job_uid_list":'appJobUidList',
        "cloud_domain_id":'cloudDomainId',
        "common_job_info":'commonJobInfo',
        "is_cad_mode":'isCadMode',
        "is_migration_ready":'isMigrationReady',
        "num_of_bytes_downloaded":'numOfBytesDownloaded',
    }
    def __init__(self,
                 app_job_uid_list=None,
                 cloud_domain_id=None,
                 common_job_info=None,
                 is_cad_mode=None,
                 is_migration_ready=None,
                 num_of_bytes_downloaded=None,
            ):

        """Constructor for the CloudDomainMigrationQueryResult class"""

        # Initialize members of the class
        self.app_job_uid_list = app_job_uid_list
        self.cloud_domain_id = cloud_domain_id
        self.common_job_info = common_job_info
        self.is_cad_mode = is_cad_mode
        self.is_migration_ready = is_migration_ready
        self.num_of_bytes_downloaded = num_of_bytes_downloaded

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
        app_job_uid_list = None
        if dictionary.get('appJobUidList') != None:
            app_job_uid_list = list()
            for structure in dictionary.get('appJobUidList'):
                app_job_uid_list.append(cohesity_management_sdk.models.universal_id.UniversalId.from_dictionary(structure))
        cloud_domain_id = dictionary.get('cloudDomainId')
        common_job_info = cohesity_management_sdk.models.common_job_info.CommonJobInfo.from_dictionary(dictionary.get('commonJobInfo')) if dictionary.get('commonJobInfo') else None
        is_cad_mode = dictionary.get('isCadMode')
        is_migration_ready = dictionary.get('isMigrationReady')
        num_of_bytes_downloaded = dictionary.get('numOfBytesDownloaded')

        # Return an object of this model
        return cls(
            app_job_uid_list,
            cloud_domain_id,
            common_job_info,
            is_cad_mode,
            is_migration_ready,
            num_of_bytes_downloaded
)