# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.nas_analysis_job_params_access_time_bucket
import cohesity_management_sdk.models.nas_analysis_job_params_file_size_bucket
import cohesity_management_sdk.models.nas_analysis_job_params_file_type_bucket
import cohesity_management_sdk.models.nas_analysis_job_params_mod_time_bucket

class NasAnalysisJobParams(object):

    """Implementation of the 'NasAnalysisJobParams' model.

    Message to capture additional NAS analysis job params.

    Attributes:
        access_time_buckets (list of NasAnalysisJobParams_AccessTimeBucket):
            File access time buckets.
        file_size_buckets (list of NasAnalysisJobParams_FileSizeBucket): File
            size buckets.
        file_type_buckets (list of NasAnalysisJobParams_FileTypeBucket): File
            type buckets.
        mod_time_buckets (list of NasAnalysisJobParams_ModTimeBucket): File
            modification time buckets.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "access_time_buckets":'accessTimeBuckets',
        "file_size_buckets":'fileSizeBuckets',
        "file_type_buckets":'fileTypeBuckets',
        "mod_time_buckets":'modTimeBuckets'
    }

    def __init__(self,
                 access_time_buckets=None,
                 file_size_buckets=None,
                 file_type_buckets=None,
                 mod_time_buckets=None):
        """Constructor for the NasAnalysisJobParams class"""

        # Initialize members of the class
        self.access_time_buckets = access_time_buckets
        self.file_size_buckets = file_size_buckets
        self.file_type_buckets = file_type_buckets
        self.mod_time_buckets = mod_time_buckets


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
        access_time_buckets = None
        if dictionary.get('accessTimeBuckets') != None:
            access_time_buckets = list()
            for structure in dictionary.get('accessTimeBuckets'):
                access_time_buckets.append(cohesity_management_sdk.models.nas_analysis_job_params_access_time_bucket.NasAnalysisJobParams_AccessTimeBucket.from_dictionary(structure))
        file_size_buckets = None
        if dictionary.get('fileSizeBuckets') != None:
            file_size_buckets = list()
            for structure in dictionary.get('fileSizeBuckets'):
                file_size_buckets.append(cohesity_management_sdk.models.nas_analysis_job_params_file_size_bucket.NasAnalysisJobParams_FileSizeBucket.from_dictionary(structure))
        file_type_buckets = None
        if dictionary.get('fileTypeBuckets') != None:
            file_type_buckets = list()
            for structure in dictionary.get('fileTypeBuckets'):
                file_type_buckets.append(cohesity_management_sdk.models.nas_analysis_job_params_file_type_bucket.NasAnalysisJobParams_FileTypeBucket.from_dictionary(structure))
        mod_time_buckets = None
        if dictionary.get('modTimeBuckets') != None:
            mod_time_buckets = list()
            for structure in dictionary.get('modTimeBuckets'):
                mod_time_buckets.append(cohesity_management_sdk.models.nas_analysis_job_params_mod_time_bucket.NasAnalysisJobParams_ModTimeBucket.from_dictionary(structure))

        # Return an object of this model
        return cls(access_time_buckets,
                   file_size_buckets,
                   file_type_buckets,
                   mod_time_buckets)


