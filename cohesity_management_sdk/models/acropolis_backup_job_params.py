# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.acropolis_disk_filter_proto


class AcropolisBackupJobParams(object):

    """Implementation of the 'AcropolisBackupJobParams' model.

    Message to capture any additional backup params for Acropolis environment.


    Attributes:

        acropolis_disk_exclusion_info (list of AcropolisDiskFilterProto): List
            of Virtual Disk(s) to be excluded from the backup job. These disks
            will be excluded for all VMs in this environment unless overriden
            by the disk exclusion/inclusion list from
            BackupSourceParams.AcropolisBackupSourceParams.
        acropolis_disk_inclusion_info (list of AcropolisDiskFilterProto): List
            of Virtual Disk(s) to be included from the backup job. These disks
            will be included for all VMs in this environment and all other
            disks will be excluded. It can be overriden by the disk
            exclusion/inclusion list from
            BackupSourceParams.AcropolisBackupSourceParams.
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

        """Constructor for the AcropolisBackupJobParams class"""

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