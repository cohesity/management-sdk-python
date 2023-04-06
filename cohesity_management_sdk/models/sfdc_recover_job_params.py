# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.aurora_cluster_info
import cohesity_management_sdk.models.s3_bucket_info
import cohesity_management_sdk.models.sfdc_recover_job_params_prev_full_sfdc_server_timestamp_usecs_map_entry


class SfdcRecoverJobParams(object):

    """Implementation of the 'SfdcRecoverJobParams' model.

    TODO: type description here.


    Attributes:

        aurora_cluster_info (AuroraClusterInfo): Contains the information of
            the Aurora database cluster.
        aws_iam_role (string): IAM role used to get access to the Aurora
            cluster and S3 bucket.
        overwrite (bool): Whether to overwrite or keep the object if the object
            being recovered already exists in the destination.
        prev_full_sfdc_server_timestamp_usecs_map (list of
            SfdcRecoverJobParams_PrevFullSfdcServerTimestampUsecsMapEntry): A
            map containing prev_full_sfdc_server_timestamp_usecs for the
            dependent objects.
        restore_childs_object_vec (list of string): TODO: Type description
            here.
        restore_parent_object_vec (list of string): List of parent/child
            objects that need to be restored.
        run_start_time_usecs (long|int): The time when the corresponding backup
            run was started.
        s3_bucket_info (S3BucketInfo): Contains the information of the S3
            bucket used for uploading data.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "aurora_cluster_info":'auroraClusterInfo',
        "aws_iam_role":'awsIamRole',
        "overwrite":'overwrite',
        "prev_full_sfdc_server_timestamp_usecs_map":'prevFullSfdcServerTimestampUsecsMap',
        "restore_childs_object_vec":'restoreChildsObjectVec',
        "restore_parent_object_vec":'restoreParentObjectVec',
        "run_start_time_usecs":'runStartTimeUsecs',
        "s3_bucket_info":'s3BucketInfo',
    }
    def __init__(self,
                 aurora_cluster_info=None,
                 aws_iam_role=None,
                 overwrite=None,
                 prev_full_sfdc_server_timestamp_usecs_map=None,
                 restore_childs_object_vec=None,
                 restore_parent_object_vec=None,
                 run_start_time_usecs=None,
                 s3_bucket_info=None,
            ):

        """Constructor for the SfdcRecoverJobParams class"""

        # Initialize members of the class
        self.aurora_cluster_info = aurora_cluster_info
        self.aws_iam_role = aws_iam_role
        self.overwrite = overwrite
        self.prev_full_sfdc_server_timestamp_usecs_map = prev_full_sfdc_server_timestamp_usecs_map
        self.restore_childs_object_vec = restore_childs_object_vec
        self.restore_parent_object_vec = restore_parent_object_vec
        self.run_start_time_usecs = run_start_time_usecs
        self.s3_bucket_info = s3_bucket_info

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
        overwrite = dictionary.get('overwrite')
        prev_full_sfdc_server_timestamp_usecs_map = None
        if dictionary.get('prevFullSfdcServerTimestampUsecsMap') != None:
            prev_full_sfdc_server_timestamp_usecs_map = list()
            for structure in dictionary.get('prevFullSfdcServerTimestampUsecsMap'):
                prev_full_sfdc_server_timestamp_usecs_map.append(cohesity_management_sdk.models.sfdc_recover_job_params_prev_full_sfdc_server_timestamp_usecs_map_entry.SfdcRecoverJobParams_PrevFullSfdcServerTimestampUsecsMapEntry.from_dictionary(structure))
        restore_childs_object_vec = dictionary.get("restoreChildsObjectVec")
        restore_parent_object_vec = dictionary.get("restoreParentObjectVec")
        run_start_time_usecs = dictionary.get('runStartTimeUsecs')
        s3_bucket_info = cohesity_management_sdk.models.s3_bucket_info.S3BucketInfo.from_dictionary(dictionary.get('s3BucketInfo')) if dictionary.get('s3BucketInfo') else None

        # Return an object of this model
        return cls(
            aurora_cluster_info,
            aws_iam_role,
            overwrite,
            prev_full_sfdc_server_timestamp_usecs_map,
            restore_childs_object_vec,
            restore_parent_object_vec,
            run_start_time_usecs,
            s3_bucket_info
)