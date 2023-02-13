# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.restore_count_by_object_type

class RecoveriesTile(object):

    """Implementation of the 'RecoveriesTile' model.

    Recoveries information.

    Attributes:
        last_month_num_recoveries (int): Number of Recoveries in the last 30
            days.
        last_month_recoveries_by_type (list of RestoreCountByObjectType):
            Recoveries by Type in the last month.
        last_month_recovery_size_bytes (long|int): Bytes recovered in the last
            30 days.
        recovery_num_running (int): Number of recoveries that are currently
            running.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "last_month_num_recoveries":'lastMonthNumRecoveries',
        "last_month_recoveries_by_type":'lastMonthRecoveriesByType',
        "last_month_recovery_size_bytes":'lastMonthRecoverySizeBytes',
        "recovery_num_running":'recoveryNumRunning'
    }

    def __init__(self,
                 last_month_num_recoveries=None,
                 last_month_recoveries_by_type=None,
                 last_month_recovery_size_bytes=None,
                 recovery_num_running=None):
        """Constructor for the RecoveriesTile class"""

        # Initialize members of the class
        self.last_month_num_recoveries = last_month_num_recoveries
        self.last_month_recoveries_by_type = last_month_recoveries_by_type
        self.last_month_recovery_size_bytes = last_month_recovery_size_bytes
        self.recovery_num_running = recovery_num_running


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
        last_month_num_recoveries = dictionary.get('lastMonthNumRecoveries')
        last_month_recoveries_by_type = None
        if dictionary.get('lastMonthRecoveriesByType') != None:
            last_month_recoveries_by_type = list()
            for structure in dictionary.get('lastMonthRecoveriesByType'):
                last_month_recoveries_by_type.append(cohesity_management_sdk.models.restore_count_by_object_type.RestoreCountByObjectType.from_dictionary(structure))
        last_month_recovery_size_bytes = dictionary.get('lastMonthRecoverySizeBytes')
        recovery_num_running = dictionary.get('recoveryNumRunning')

        # Return an object of this model
        return cls(last_month_num_recoveries,
                   last_month_recoveries_by_type,
                   last_month_recovery_size_bytes,
                   recovery_num_running)


