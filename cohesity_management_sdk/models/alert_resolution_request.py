# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.alert_resolution_info

class AlertResolutionRequest(object):

    """Implementation of the 'AlertResolutionRequest' model.

    Request that provides the details of a resolution and the list of
    Alert Ids to be marked resolved.

    Attributes:
        alert_id_list (list of string): Specifies list of alerts resolved by a
            Resolution, which are specified by Alert Ids.
        resolution_details (AlertResolutionInfo): Short description and
            detailed notes about the Resolution.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "alert_id_list":'alertIdList',
        "resolution_details":'resolutionDetails'
    }

    def __init__(self,
                 alert_id_list=None,
                 resolution_details=None):
        """Constructor for the AlertResolutionRequest class"""

        # Initialize members of the class
        self.alert_id_list = alert_id_list
        self.resolution_details = resolution_details


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
        alert_id_list = dictionary.get('alertIdList')
        resolution_details = cohesity_management_sdk.models.alert_resolution_info.AlertResolutionInfo.from_dictionary(dictionary.get('resolutionDetails')) if dictionary.get('resolutionDetails') else None

        # Return an object of this model
        return cls(alert_id_list,
                   resolution_details)


