# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

import cohesity_management_sdk.models.sequencer

class NoSqlLogData(object):

    """Implementation of the 'NoSqlLogData' model.

    Attributes:
        end_seq_number (Sequencer): End sequence number in the log file till
            which the data needs to be applied. If this not populated,
            hydration_time_usecs must be used for determining the point till
            which the log needs to be applied for hydration.
        log_file_name (string): Full path + name of the log file that needs to
            be processed.
        log_rollover (bool): Specifies the subnet mask for the IPMI
            network.
        start_seq_number (Sequencer): Start sequence number in the log file
            from which the data needs to be applied for hydration.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "end_seq_number":'endSeqNumber',
        "log_file_name":'logFileName',
        "log_rollover":'logRollover',
        "start_seq_number":'startSeqNumber'
    }

    def __init__(self,
                 end_seq_number=None,
                 log_file_name=None,
                 log_rollover=None,
                 start_seq_number=None):
        """Constructor for the NoSqlLogData class"""

        # Initialize members of the class
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
        end_seq_number = cohesity_management_sdk.models.sequencer.Sequencer.from_dictionary(dictionary.get('endSeqNumber')) if dictionary.get('endSeqNumber') else None
        log_file_name = dictionary.get('logFileName')
        log_rollover = dictionary.get('logRollover')
        start_seq_number = cohesity_management_sdk.models.sequencer.Sequencer.from_dictionary(dictionary.get('startSeqNumber')) if dictionary.get('startSeqNumber') else None

        # Return an object of this model
        return cls(end_seq_number,
                   log_file_name,
                   log_rollover,
                   start_seq_number)


