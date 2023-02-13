# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class EBSVolumeExclusionParams(object):

    """Implementation of the 'EBSVolumeExclusionParams' model.

    Message defining the different criteria to exclude EBS volumes from
    backup. This is used to specify both object-level (BackupSourceParams) and
    job-level (EnvBackupParams) exclusion criteria.
    If a criterion is specified at both object-level and job-level, then
    job-level setting will be ignored.

    Attributes:
        device_name_vec (list of string): List of device names to exclude.
            Eg - /dev/sda1, /dev/xvdb.
        max_volume_size_bytes (long|int): Any volume larger than this size
            will be excluded.
        volume_id_vec (list of string): List of volume IDs to exclude.
            This field is only for object-level exclusions.
        volume_type_vec (list of string): List of volume types to exclude.
            Eg - gp2, gp3, io1.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "device_name_vec":'deviceNameVec',
        "max_volume_size_bytes":'maxVolumeSizeBytes',
        "volume_id_vec":'volumeIdVec',
        "volume_type_vec":'volumeTypeVec'
    }

    def __init__(self,
                 device_name_vec=None,
                 max_volume_size_bytes=None,
                 volume_id_vec=None,
                 volume_type_vec=None):
        """Constructor for the EBSVolumeExclusionParams class"""

        # Initialize members of the class
        self.device_name_vec = device_name_vec
        self.max_volume_size_bytes = max_volume_size_bytes
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
        device_name_vec = dictionary.get('deviceNameVec')
        max_volume_size_bytes = dictionary.get('maxVolumeSizeBytes')
        volume_id_vec = dictionary.get('volumeIdVec')
        volume_type_vec = dictionary.get('volumeTypeVec')

        # Return an object of this model
        return cls(device_name_vec,
                   max_volume_size_bytes,
                   volume_id_vec,
                   volume_type_vec)


