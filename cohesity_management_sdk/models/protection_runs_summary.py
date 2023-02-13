# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ProtectionRunsSummary(object):

    """Implementation of the 'ProtectionRunsSummary' model.

    ProtectionRunsSummary is the summary of the all the Protection Runs for
    the
    Protection Jobs using the Specified Protection Policy.

    Attributes:
        number_of_archival_runs (long|int): Specifies the total number of
            Archival Runs using the current Protection Policy.
        number_of_protection_runs (long|int): Specifies the total number of
            Protection Runs by the given Protection Policy.
        number_of_replication_runs (long|int): Specifies the total number of
            Replication Runs using the current Protection Policy.
        number_of_successful_archival_runs (long|int): Specifies the number of
            total successful Archival Runs using the current Protection
            Policy.
        number_of_successful_protection_runs (long|int): Specifies the number
            of successful Protection Runs using the current Protection
            Policy.
        number_of_successful_replication_runs (long|int): Specifies the number
            of total successful Replication Runs using the current Protection
            Policy.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "number_of_archival_runs":'numberOfArchivalRuns',
        "number_of_protection_runs":'numberOfProtectionRuns',
        "number_of_replication_runs":'numberOfReplicationRuns',
        "number_of_successful_archival_runs":'numberOfSuccessfulArchivalRuns',
        "number_of_successful_protection_runs":'numberOfSuccessfulProtectionRuns',
        "number_of_successful_replication_runs":'numberOfSuccessfulReplicationRuns'
    }

    def __init__(self,
                 number_of_archival_runs=None,
                 number_of_protection_runs=None,
                 number_of_replication_runs=None,
                 number_of_successful_archival_runs=None,
                 number_of_successful_protection_runs=None,
                 number_of_successful_replication_runs=None):
        """Constructor for the ProtectionRunsSummary class"""

        # Initialize members of the class
        self.number_of_archival_runs = number_of_archival_runs
        self.number_of_protection_runs = number_of_protection_runs
        self.number_of_replication_runs = number_of_replication_runs
        self.number_of_successful_archival_runs = number_of_successful_archival_runs
        self.number_of_successful_protection_runs = number_of_successful_protection_runs
        self.number_of_successful_replication_runs = number_of_successful_replication_runs


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
        number_of_archival_runs = dictionary.get('numberOfArchivalRuns')
        number_of_protection_runs = dictionary.get('numberOfProtectionRuns')
        number_of_replication_runs = dictionary.get('numberOfReplicationRuns')
        number_of_successful_archival_runs = dictionary.get('numberOfSuccessfulArchivalRuns')
        number_of_successful_protection_runs = dictionary.get('numberOfSuccessfulProtectionRuns')
        number_of_successful_replication_runs = dictionary.get('numberOfSuccessfulReplicationRuns')

        # Return an object of this model
        return cls(number_of_archival_runs,
                   number_of_protection_runs,
                   number_of_replication_runs,
                   number_of_successful_archival_runs,
                   number_of_successful_protection_runs,
                   number_of_successful_replication_runs)


