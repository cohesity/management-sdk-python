# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ViewPinningConfig(object):

    """Implementation of the 'ViewPinningConfig' model.

    TODO: type description here.


    Attributes:

        enabled (bool, required): Specifies if view pinning is enabled. If set
            to true, view will be pinned to SSD.
        last_updated_timestamp_secs (long|int): Specifies the timestamp when
            view pinning config is last updated.
        pinned_time_secs (long|int): Specifies the time to pin files after last
            access.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "enabled":'enabled',
        "last_updated_timestamp_secs":'lastUpdatedTimestampSecs',
        "pinned_time_secs":'pinnedTimeSecs',
    }
    def __init__(self,
                 enabled=None,
                 last_updated_timestamp_secs=None,
                 pinned_time_secs=None,
            ):

        """Constructor for the ViewPinningConfig class"""

        # Initialize members of the class
        self.enabled = enabled
        self.last_updated_timestamp_secs = last_updated_timestamp_secs
        self.pinned_time_secs = pinned_time_secs

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
        enabled = dictionary.get('enabled')
        last_updated_timestamp_secs = dictionary.get('lastUpdatedTimestampSecs')
        pinned_time_secs = dictionary.get('pinnedTimeSecs')

        # Return an object of this model
        return cls(
            enabled,
            last_updated_timestamp_secs,
            pinned_time_secs
)