# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.aurora_cluster_info
import cohesity_management_sdk.models.object_level_params
import cohesity_management_sdk.models.registered_entity_sfdc_params
import cohesity_management_sdk.models.s3_bucket_info


class SfdcBackupJobParams(object):

    """Implementation of the 'SfdcBackupJobParams' model.

    Message to capture any additional backup params for Group within the Sfdc
    environment.


    Attributes:

        aurora_cluster_info (AuroraClusterInfo): Contains the information of
            the Aurora database cluster and Iam role info needed to access the
            Aurora cluster.
        aws_iam_role (string): IAM role used to get access to the Aurora
            cluster and S3 bucket.
        object_info_vec (list of ObjectLevelParams): List of details per Sfdc
            object.
        previous_run_sfdc_server_timestamp_usecs (long|int): Sfdc Server Time
            for the previous run
        registered_entity_sfdc_params (RegisteredEntitySfdcParams): Includes
            connection parameters and info saved during registration.
        s3_bucket_info (S3BucketInfo): Contains the information of the S3
            bucket used for uploading data.
        sfdc_object_metadata_proto_path (string): Path on snapfs where we
            persist the SfdcObjectMetadata.
        sfdc_server_timestamp_usecs (long|int): Sfdc Server Time This time is
            being used as a snapshot time for fetching only incremental records
            in the next incremental backup.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "aurora_cluster_info":'auroraClusterInfo',
        "aws_iam_role":'awsIamRole',
        "object_info_vec":'objectInfoVec',
        "previous_run_sfdc_server_timestamp_usecs":'previousRunSfdcServerTimestampUsecs',
        "registered_entity_sfdc_params":'registeredEntitySfdcParams',
        "s3_bucket_info":'s3BucketInfo',
        "sfdc_object_metadata_proto_path":'sfdcObjectMetadataProtoPath',
        "sfdc_server_timestamp_usecs":'sfdcServerTimestampUsecs',
    }
    def __init__(self,
                 aurora_cluster_info=None,
                 aws_iam_role=None,
                 object_info_vec=None,
                 previous_run_sfdc_server_timestamp_usecs=None,
                 registered_entity_sfdc_params=None,
                 s3_bucket_info=None,
                 sfdc_object_metadata_proto_path=None,
                 sfdc_server_timestamp_usecs=None,
            ):

        """Constructor for the SfdcBackupJobParams class"""

        # Initialize members of the class
        self.aurora_cluster_info = aurora_cluster_info
        self.aws_iam_role = aws_iam_role
        self.object_info_vec = object_info_vec
        self.previous_run_sfdc_server_timestamp_usecs = previous_run_sfdc_server_timestamp_usecs
        self.registered_entity_sfdc_params = registered_entity_sfdc_params
        self.s3_bucket_info = s3_bucket_info
        self.sfdc_object_metadata_proto_path = sfdc_object_metadata_proto_path
        self.sfdc_server_timestamp_usecs = sfdc_server_timestamp_usecs

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
        aurora_cluster_info = cohesity_management_sdk.models.aurora_cluster_info.AuroraClusterInfo.from_dictionary(dictionary.get('auroraClusterInfo')) if dictionary.get('auroraClusterInfo') else None
        aws_iam_role = dictionary.get('awsIamRole')
        object_info_vec = None
        if dictionary.get('objectInfoVec') != None:
            object_info_vec = list()
            for structure in dictionary.get('objectInfoVec'):
                object_info_vec.append(cohesity_management_sdk.models.object_level_params.ObjectLevelParams.from_dictionary(structure))
        previous_run_sfdc_server_timestamp_usecs = dictionary.get('previousRunSfdcServerTimestampUsecs')
        registered_entity_sfdc_params = cohesity_management_sdk.models.registered_entity_sfdc_params.RegisteredEntitySfdcParams.from_dictionary(dictionary.get('registeredEntitySfdcParams')) if dictionary.get('registeredEntitySfdcParams') else None
        s3_bucket_info = cohesity_management_sdk.models.s3_bucket_info.S3BucketInfo.from_dictionary(dictionary.get('s3BucketInfo')) if dictionary.get('s3BucketInfo') else None
        sfdc_object_metadata_proto_path = dictionary.get('sfdcObjectMetadataProtoPath')
        sfdc_server_timestamp_usecs = dictionary.get('sfdcServerTimestampUsecs')

        # Return an object of this model
        return cls(
            aurora_cluster_info,
            aws_iam_role,
            object_info_vec,
            previous_run_sfdc_server_timestamp_usecs,
            registered_entity_sfdc_params,
            s3_bucket_info,
            sfdc_object_metadata_proto_path,
            sfdc_server_timestamp_usecs
)