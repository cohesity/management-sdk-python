# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.universal_id_proto


class OracleArchiveLogInfo_OracleArchiveLogRange_RangeAttributes(object):

    """Implementation of the 'OracleArchiveLogInfo_OracleArchiveLogRange_RangeAttributes' model.

    Attributes related to each range. This is only used when we sending valid
    ranges to iris to fill the slider. While triggering restore this field can
    be skipped.


    Attributes:

        incarnation_id (long|int): Incarnation id associated with the range
            Only applicable for SCN and sequence type.
        job_uid (UniversalIdProto): jobs ID from which the snapshots were
            taken.
        reset_logs_id (long|int): Resetlogs identifier associated with the
            range. Only applicable for SCN and sequence type.
        thread_id (long|int): Thread id associated with the range. Only
            applicable for sequence type.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "incarnation_id":'incarnationId',
        "job_uid":'jobUid',
        "reset_logs_id":'resetLogsId',
        "thread_id":'threadId',
    }
    def __init__(self,
                 incarnation_id=None,
                 job_uid=None,
                 reset_logs_id=None,
                 thread_id=None,
            ):

        """Constructor for the OracleArchiveLogInfo_OracleArchiveLogRange_RangeAttributes class"""

        # Initialize members of the class
        self.incarnation_id = incarnation_id
        self.job_uid = job_uid
        self.reset_logs_id = reset_logs_id
        self.thread_id = thread_id

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
        incarnation_id = dictionary.get('incarnationId')
        job_uid = cohesity_management_sdk.models.universal_id_proto.UniversalIdProto.from_dictionary(dictionary.get('jobUid')) if dictionary.get('jobUid') else None
        reset_logs_id = dictionary.get('resetLogsId')
        thread_id = dictionary.get('threadId')

        # Return an object of this model
        return cls(
            incarnation_id,
            job_uid,
            reset_logs_id,
            thread_id
)