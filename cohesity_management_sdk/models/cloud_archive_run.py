# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.cloud_archival_info

class CloudArchiveRun(object):

    """Implementation of the 'CloudArchiveRun' model.

    Specifies the info about cloud archive run.

    Attributes:
        archival_info (list of CloudArchivalInfo): Notification list.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "archival_info":'archivalInfo'
    }

    def __init__(self,
                 archival_info=None):
        """Constructor for the CloudArchiveRun class"""

        # Initialize members of the class
        self.archival_info = archival_info


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
        archival_info = None
        if dictionary.get('archivalInfo') != None:
            archival_info = list()
            for structure in dictionary.get('archivalInfo'):
                archival_info.append(cohesity_management_sdk.models.cloud_archival_info.CloudArchivalInfo.from_dictionary(structure))

        # Return an object of this model
        return cls(archival_info)


