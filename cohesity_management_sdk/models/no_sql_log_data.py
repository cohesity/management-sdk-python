# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.sequencer


class NoSqlLogData(object):

    """Implementation of the 'NoSqlLogData' model.

    Proto that contains the information about a log file containing MongoDB cdp
    logs pertaining to an entity. This is populated from the data events
    written to scribe for corresponding entity. The start and end sequence
    numbers correspond to the range of logs inside this file which need to be
    applied for hydration. We also mark if a file has recorded an oplog
    rollover and if it contains at least 1 change event.


    Attributes:

        contains_change_event (bool): True if this file contains at least 1
            change event.
        end_seq_number (Sequencer): End sequence number in the log file till
            which the data needs to be applied. If this not populated,
            hydration_time_usecs must be used for determining the point till
            which the log needs to be applied for hydration.
        log_file_name (string): Name of the log file that needs to be
            processed.
        log_rollover (bool): True if log rollover has happened.
        start_seq_number (Sequencer): Start sequence number in the log file
            from which the data needs to be applied for hydration.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "contains_change_event":'containsChangeEvent',
        "end_seq_number":'endSeqNumber',
        "log_file_name":'logFileName',
        "log_rollover":'logRollover',
        "start_seq_number":'startSeqNumber',
    }
    def __init__(self,
                 contains_change_event=None,
                 end_seq_number=None,
                 log_file_name=None,
                 log_rollover=None,
                 start_seq_number=None,
            ):

        """Constructor for the NoSqlLogData class"""

        # Initialize members of the class
        self.contains_change_event = contains_change_event
        self.end_seq_number = end_seq_number
        self.log_file_name = log_file_name
        self.log_rollover = log_rollover
        self.start_seq_number = start_seq_number

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
        contains_change_event = dictionary.get('containsChangeEvent')
        end_seq_number = cohesity_management_sdk.models.sequencer.Sequencer.from_dictionary(dictionary.get('endSeqNumber')) if dictionary.get('endSeqNumber') else None
        log_file_name = dictionary.get('logFileName')
        log_rollover = dictionary.get('logRollover')
        start_seq_number = cohesity_management_sdk.models.sequencer.Sequencer.from_dictionary(dictionary.get('startSeqNumber')) if dictionary.get('startSeqNumber') else None

        # Return an object of this model
        return cls(
            contains_change_event,
            end_seq_number,
            log_file_name,
            log_rollover,
            start_seq_number
)