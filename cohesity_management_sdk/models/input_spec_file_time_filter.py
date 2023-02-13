# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class InputSpec_FileTimeFilter(object):

    """Implementation of the 'InputSpec_FileTimeFilter' model.

    File time filter to filter files based on their last change time. All
    files whose change time is in the range [change_time_range_start_secs,
    change_time_range_end_secs) will be processed. Both values are time
    duration in seconds w.r.t. to current time and not absolute points in
    time.

    Attributes:
        change_time_range_end_secs (long|int):  End of file's change time
            range.
        change_time_range_start_secs (long|int): Start of file's change time
            range.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "change_time_range_end_secs": 'changeTimeRangeEndSecs',
        "change_time_range_start_secs": 'changeTimeRangeStartSecs'
    }

    def __init__(self,
                 change_time_range_end_secs=None,
                 change_time_range_start_secs=None):
        """Constructor for the InputSpec_FileTimeFilter class"""

        # Initialize members of the class
        self.change_time_range_end_secs = change_time_range_end_secs
        self.change_time_range_start_secs = change_time_range_start_secs


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
        change_time_range_end_secs = dictionary.get('changeTimeRangeEndSecs', None)
        change_time_range_start_secs = dictionary.get('changeTimeRangeStartSecs', None)

        # Return an object of this model
        return cls(change_time_range_end_secs,
                   change_time_range_start_secs)


