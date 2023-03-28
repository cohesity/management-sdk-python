# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.ebs_volume_exclusion_params_tag_params


class EBSVolumeExclusionParams(object):

    """Implementation of the 'EBSVolumeExclusionParams' model.

    Message defining the different criteria to exclude EBS volumes from backup.
    This is used to specify both object-level (BackupSourceParams) and
    job-level (EnvBackupParams) exclusion criteria. If a criterion is specified
    at both object-level and job-level, then job-level setting will be ignored.


    Attributes:

        device_name_vec (list of string): List of device names to exclude. Eg -
            /dev/sda1, /dev/xvdb.
        max_volume_size_bytes (long|int): Any volume larger than this size will
            be excluded.
        raw_query (string): Raw boolean query given as input by the user to
            exclude volume based on tags. In the current version, the query
            contains only tags. Example query 1: "K1" = "V1" AND "K2" IN ("V2",
            "V3") AND "K4" != "V4" Example query 2: "K1" != "V1" OR "K2" NOT IN
            ("V2", "V3") OR "K4" != "V4" All Keys and Values must be wrapped
            inside double quotes. Comparision Operators supported : =, !=, IN,
            NOT IN. Logical Operators supported : AND, OR. We cannot have AND,
            OR together in the query. Only one of them is allowed. The
            processed form for this query is stored in the above
            tag_params_vec.
        tag_params_vec (list of EBSVolumeExclusionParams_TagParams): List of
            Tag Params to exclude EBS volumes.
        volume_id_vec (list of string): List of volume IDs to exclude. This
            field is only for object-level exclusions.
        volume_type_vec (list of string): List of volume types to exclude. Eg -
            gp2, gp3, io1.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "device_name_vec":'deviceNameVec',
        "max_volume_size_bytes":'maxVolumeSizeBytes',
        "raw_query":'rawQuery',
        "tag_params_vec":'tagParamsVec',
        "volume_id_vec":'volumeIdVec',
        "volume_type_vec":'volumeTypeVec',
    }
    def __init__(self,
                 device_name_vec=None,
                 max_volume_size_bytes=None,
                 raw_query=None,
                 tag_params_vec=None,
                 volume_id_vec=None,
                 volume_type_vec=None,
            ):

        """Constructor for the EBSVolumeExclusionParams class"""

        # Initialize members of the class
        self.device_name_vec = device_name_vec
        self.max_volume_size_bytes = max_volume_size_bytes
        self.raw_query = raw_query
        self.tag_params_vec = tag_params_vec
        self.volume_id_vec = volume_id_vec
        self.volume_type_vec = volume_type_vec

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
        device_name_vec = dictionary.get("deviceNameVec")
        max_volume_size_bytes = dictionary.get('maxVolumeSizeBytes')
        raw_query = dictionary.get('rawQuery')
        tag_params_vec = None
        if dictionary.get('tagParamsVec') != None:
            tag_params_vec = list()
            for structure in dictionary.get('tagParamsVec'):
                tag_params_vec.append(cohesity_management_sdk.models.ebs_volume_exclusion_params_tag_params.EBSVolumeExclusionParams_TagParams.from_dictionary(structure))
        volume_id_vec = dictionary.get("volumeIdVec")
        volume_type_vec = dictionary.get("volumeTypeVec")

        # Return an object of this model
        return cls(
            device_name_vec,
            max_volume_size_bytes,
            raw_query,
            tag_params_vec,
            volume_id_vec,
            volume_type_vec
)