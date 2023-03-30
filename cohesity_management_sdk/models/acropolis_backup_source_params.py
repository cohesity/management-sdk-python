# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.acropolis_disk_filter_proto


class AcropolisBackupSourceParams(object):

    """Implementation of the 'AcropolisBackupSourceParams' model.

    Message to capture additional backup params for a Acropolis type source.


    Attributes:

        acropolis_disk_exclusion_info (list of AcropolisDiskFilterProto): List
            of Virtual Disk(s) to be excluded from the from the backup job for
            the source. Overrides the exclusion list requested (if any) through
            EnvBackupParams.AcropolisBackupEnvParams.
        acropolis_disk_inclusion_info (list of AcropolisDiskFilterProto): List
            of Virtual Disk(s) to be included from the from the backup job for
            the source. These disks will be only included for the source and
            all other disks will be excluded. Overrides the disk
            exclusion/inclusion list from
            EnvBackupParams.AcropolisBackupEnvParams.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "acropolis_disk_exclusion_info":'acropolisDiskExclusionInfo',
        "acropolis_disk_inclusion_info":'acropolisDiskInclusionInfo',
    }
    def __init__(self,
                 acropolis_disk_exclusion_info=None,
                 acropolis_disk_inclusion_info=None,
            ):

        """Constructor for the AcropolisBackupSourceParams class"""

        # Initialize members of the class
        self.acropolis_disk_exclusion_info = acropolis_disk_exclusion_info
        self.acropolis_disk_inclusion_info = acropolis_disk_inclusion_info

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
        acropolis_disk_exclusion_info = None
        if dictionary.get('acropolisDiskExclusionInfo') != None:
            acropolis_disk_exclusion_info = list()
            for structure in dictionary.get('acropolisDiskExclusionInfo'):
                acropolis_disk_exclusion_info.append(cohesity_management_sdk.models.acropolis_disk_filter_proto.AcropolisDiskFilterProto.from_dictionary(structure))
        acropolis_disk_inclusion_info = None
        if dictionary.get('acropolisDiskInclusionInfo') != None:
            acropolis_disk_inclusion_info = list()
            for structure in dictionary.get('acropolisDiskInclusionInfo'):
                acropolis_disk_inclusion_info.append(cohesity_management_sdk.models.acropolis_disk_filter_proto.AcropolisDiskFilterProto.from_dictionary(structure))

        # Return an object of this model
        return cls(
            acropolis_disk_exclusion_info,
            acropolis_disk_inclusion_info
)