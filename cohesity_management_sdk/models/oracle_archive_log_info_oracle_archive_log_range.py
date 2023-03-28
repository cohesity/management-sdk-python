# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.oracle_archive_log_info_oracle_archive_log_range_range_attributes


class OracleArchiveLogInfo_OracleArchiveLogRange(object):

    """Implementation of the 'OracleArchiveLogInfo_OracleArchiveLogRange' model.

    TODO: type description here.


    Attributes:

        attributes
            (OracleArchiveLogInfo_OracleArchiveLogRange_RangeAttributes): TODO:
            Type description here.
        end_of_range (long|int): End value of the range
        range_type (int): Type of range provided.
        start_of_range (long|int): Start value of the range In case of time we
            store it as unix epoch format which can be easily stored in int64.
            Use www.epochconverter.com to convert to human readable date.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "attributes":'attributes',
        "end_of_range":'endOfRange',
        "range_type":'rangeType',
        "start_of_range":'startOfRange',
    }
    def __init__(self,
                 attributes=None,
                 end_of_range=None,
                 range_type=None,
                 start_of_range=None,
            ):

        """Constructor for the OracleArchiveLogInfo_OracleArchiveLogRange class"""

        # Initialize members of the class
        self.attributes = attributes
        self.end_of_range = end_of_range
        self.range_type = range_type
        self.start_of_range = start_of_range

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
        attributes = cohesity_management_sdk.models.oracle_archive_log_info_oracle_archive_log_range_range_attributes.OracleArchiveLogInfo_OracleArchiveLogRange_RangeAttributes.from_dictionary(dictionary.get('attributes')) if dictionary.get('attributes') else None
        end_of_range = dictionary.get('endOfRange')
        range_type = dictionary.get('rangeType')
        start_of_range = dictionary.get('startOfRange')

        # Return an object of this model
        return cls(
            attributes,
            end_of_range,
            range_type,
            start_of_range
)