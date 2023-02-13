# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class AlertResolutionInfo(object):

    """Implementation of the 'AlertResolutionInfo' model.

    Short description and detailed notes about the Resolution.

    Attributes:
        resolution_details (string): Specifies detailed notes about the
            Resolution.
        resolution_summary (string): Specifies short description about the
            Resolution.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "resolution_details":'resolutionDetails',
        "resolution_summary":'resolutionSummary'
    }

    def __init__(self,
                 resolution_details=None,
                 resolution_summary=None):
        """Constructor for the AlertResolutionInfo class"""

        # Initialize members of the class
        self.resolution_details = resolution_details
        self.resolution_summary = resolution_summary


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
        resolution_details = dictionary.get('resolutionDetails')
        resolution_summary = dictionary.get('resolutionSummary')

        # Return an object of this model
        return cls(resolution_details,
                   resolution_summary)


