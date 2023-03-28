# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.aurora_cluster_info
import cohesity_management_sdk.models.object_level_params


class SfdcBackupSourceParamsProto(object):

    """Implementation of the 'SfdcBackupSourceParamsProto' model.

    Message to capture additional backup params for an Sfdc source.  This proto
    is used in object based protection of Sfdc source.


    Attributes:

        aurora_cluster_info (AuroraClusterInfo): Details about the
            AuroraCluster to be used for this object protection.
        aws_iam_role (string): IAM role used to get access to the Aurora
            cluster and S3 bucket.
        excluded_object_ids_vec (list of long|int): List of entity ids of the
            Sfdc objects that are excluded by the user in object protection.
        object_level_params_vec (list of ObjectLevelParams): This list is a
            mapping between an Sfdc object's entity Id and the list of field
            names that user has specified to exclude from this object's backup.
        s3_bucket_prefix (string): S3 bucket prefix to be used while uploading
            the data to Aurora-postgres.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "aurora_cluster_info":'auroraClusterInfo',
        "aws_iam_role":'awsIamRole',
        "excluded_object_ids_vec":'excludedObjectIdsVec',
        "object_level_params_vec":'objectLevelParamsVec',
        "s3_bucket_prefix":'s3BucketPrefix',
    }
    def __init__(self,
                 aurora_cluster_info=None,
                 aws_iam_role=None,
                 excluded_object_ids_vec=None,
                 object_level_params_vec=None,
                 s3_bucket_prefix=None,
            ):

        """Constructor for the SfdcBackupSourceParamsProto class"""

        # Initialize members of the class
        self.aurora_cluster_info = aurora_cluster_info
        self.aws_iam_role = aws_iam_role
        self.excluded_object_ids_vec = excluded_object_ids_vec
        self.object_level_params_vec = object_level_params_vec
        self.s3_bucket_prefix = s3_bucket_prefix

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
        excluded_object_ids_vec = dictionary.get("excludedObjectIdsVec")
        object_level_params_vec = None
        if dictionary.get('objectLevelParamsVec') != None:
            object_level_params_vec = list()
            for structure in dictionary.get('objectLevelParamsVec'):
                object_level_params_vec.append(cohesity_management_sdk.models.object_level_params.ObjectLevelParams.from_dictionary(structure))
        s3_bucket_prefix = dictionary.get('s3BucketPrefix')

        # Return an object of this model
        return cls(
            aurora_cluster_info,
            aws_iam_role,
            excluded_object_ids_vec,
            object_level_params_vec,
            s3_bucket_prefix
)