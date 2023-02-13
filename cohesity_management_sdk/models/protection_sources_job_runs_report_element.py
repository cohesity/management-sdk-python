# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.protection_source
import cohesity_management_sdk.models.protection_source_snapshot_information

class ProtectionSourcesJobRunsReportElement(object):

    """Implementation of the 'ProtectionSourcesJobRunsReportElement' model.

    Specifies a Protection Source and the Snapshots that back it up.

    Attributes:
        protection_source (ProtectionSource): Specifies the leaf Protection
            Source Object such as a VM.
        snapshots_info (array of ProtectionSourceSnapshotInformation): Array
            of Snapshots Specifies the Snapshots that contain backups of the
            Protection Source Object.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "protection_source": 'protectionSource',
        "snapshots_info": 'snapshotsInfo'
    }

    def __init__(self,
                 protection_source=None,
                 snapshots_info=None):
        """Constructor for the ProtectionSourcesJobRunsReportElement class"""

        # Initialize members of the class
        self.protection_source = protection_source
        self.snapshots_info = snapshots_info


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
        protection_source = cohesity_management_sdk.models.protection_source.ProtectionSource.from_dictionary(dictionary.get('protectionSource')) if dictionary.get('protectionSource') else None
        snapshots_info = None
        if dictionary.get('snapshotsInfo') != None:
            snapshots_info = list()
            for structure in dictionary.get('snapshotsInfo'):
                snapshots_info.append(cohesity_management_sdk.models.protection_source_snapshot_information.ProtectionSourceSnapshotInformation.from_dictionary(structure))

        # Return an object of this model
        return cls(protection_source,
                   snapshots_info)


