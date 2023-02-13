# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class AlertResolutionDetails(object):

    """Implementation of the 'AlertResolutionDetails' model.

    Specifies information about the Alert Resolution such as a summary,
    id assigned by the Cohesity Cluster, user who resolved the Alerts, etc.

    Attributes:
        resolution_details (string): Specifies detailed notes about the
            Resolution.
        resolution_id (long|int): Specifies Unique id assigned by the Cohesity
            Cluster for this Resolution.
        resolution_summary (string): Specifies short description about the
            Resolution.
        timestamp_usecs (long|int): Specifies unix epoch timestamp (in
            microseconds) when the Alerts were resolved.
        user_name (string): Specifies name of the Cohesity Cluster user who
            resolved the Alerts.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "resolution_details":'resolutionDetails',
        "resolution_id":'resolutionId',
        "resolution_summary":'resolutionSummary',
        "timestamp_usecs":'timestampUsecs',
        "user_name":'userName'
    }

    def __init__(self,
                 resolution_details=None,
                 resolution_id=None,
                 resolution_summary=None,
                 timestamp_usecs=None,
                 user_name=None):
        """Constructor for the AlertResolutionDetails class"""

        # Initialize members of the class
        self.resolution_details = resolution_details
        self.resolution_id = resolution_id
        self.resolution_summary = resolution_summary
        self.timestamp_usecs = timestamp_usecs
        self.user_name = user_name


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
        resolution_id = dictionary.get('resolutionId')
        resolution_summary = dictionary.get('resolutionSummary')
        timestamp_usecs = dictionary.get('timestampUsecs')
        user_name = dictionary.get('userName')

        # Return an object of this model
        return cls(resolution_details,
                   resolution_id,
                   resolution_summary,
                   timestamp_usecs,
                   user_name)


