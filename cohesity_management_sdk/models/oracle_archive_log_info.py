# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.oracle_archive_log_info_oracle_archive_log_range


class OracleArchiveLogInfo(object):

    """Implementation of the 'OracleArchiveLogInfo' model.

    TODO: type description here.


    Attributes:

        oracle_archive_log_range_vec (list of
            OracleArchiveLogInfo_OracleArchiveLogRange): Specifies the range in
            either SCN, sequence number or time for which archive logs are to
            be restored or for which archive logs is to be shown on the slider.
            In case of restore we only support 1 range i.e vector size will be
            1.
        oracle_archive_log_restore_dest (string): Destination where we need to
            restore archive logs. Used only when trigerring archive log
            restore. This field is left empty while returning ranges to the
            sliders.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "oracle_archive_log_range_vec":'oracleArchiveLogRangeVec',
        "oracle_archive_log_restore_dest":'oracleArchiveLogRestoreDest',
    }
    def __init__(self,
                 oracle_archive_log_range_vec=None,
                 oracle_archive_log_restore_dest=None,
            ):

        """Constructor for the OracleArchiveLogInfo class"""

        # Initialize members of the class
        self.oracle_archive_log_range_vec = oracle_archive_log_range_vec
        self.oracle_archive_log_restore_dest = oracle_archive_log_restore_dest

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
        oracle_archive_log_range_vec = None
        if dictionary.get('oracleArchiveLogRangeVec') != None:
            oracle_archive_log_range_vec = list()
            for structure in dictionary.get('oracleArchiveLogRangeVec'):
                oracle_archive_log_range_vec.append(cohesity_management_sdk.models.oracle_archive_log_info_oracle_archive_log_range.OracleArchiveLogInfo_OracleArchiveLogRange.from_dictionary(structure))
        oracle_archive_log_restore_dest = dictionary.get('oracleArchiveLogRestoreDest')

        # Return an object of this model
        return cls(
            oracle_archive_log_range_vec,
            oracle_archive_log_restore_dest
)