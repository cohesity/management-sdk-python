# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.scheduling_policy_proto_continuous_schedule
import cohesity_management_sdk.models.scheduling_policy_proto_daily_schedule
import cohesity_management_sdk.models.scheduling_policy_proto_monthly_schedule
import cohesity_management_sdk.models.scheduling_policy_proto_rpo_schedule

class SchedulingPolicyProto(object):

    """Implementation of the 'SchedulingPolicyProto' model.

    TODO: type model description here.

    Attributes:
        continuous_schedule (SchedulingPolicyProtoContinuousSchedule):  Set if
            periodicity is kContinuous.
        daily_schedule (SchedulingPolicyProtoDailySchedule): Set if
            periodicity is kDaily.
        monthly_schedule (SchedulingPolicyProtoMonthlySchedule): Set if
            periodicity is kMonthly.
        periodicity (int): Determines how often the job should be run.
        rpo_schedule (SchedulingPolicyProtoRPOSchedule):  Set if periodicity
            is kContinuousRPO.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "continuous_schedule":'continuousSchedule',
        "daily_schedule":'dailySchedule',
        "monthly_schedule":'monthlySchedule',
        "periodicity":'periodicity',
        "rpo_schedule":'rpoSchedule'
    }

    def __init__(self,
                 continuous_schedule=None,
                 daily_schedule=None,
                 monthly_schedule=None,
                 periodicity=None,
                 rpo_schedule=None):
        """Constructor for the SchedulingPolicyProto class"""

        # Initialize members of the class
        self.continuous_schedule = continuous_schedule
        self.daily_schedule = daily_schedule
        self.monthly_schedule = monthly_schedule
        self.periodicity = periodicity
        self.rpo_schedule = rpo_schedule


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
        continuous_schedule = cohesity_management_sdk.models.scheduling_policy_proto_continuous_schedule.SchedulingPolicyProtoContinuousSchedule.from_dictionary(dictionary.get('continuousSchedule')) if dictionary.get('continuousSchedule') else None
        daily_schedule = cohesity_management_sdk.models.scheduling_policy_proto_daily_schedule.SchedulingPolicyProtoDailySchedule.from_dictionary(dictionary.get('dailySchedule')) if dictionary.get('dailySchedule') else None
        monthly_schedule = cohesity_management_sdk.models.scheduling_policy_proto_monthly_schedule.SchedulingPolicyProtoMonthlySchedule.from_dictionary(dictionary.get('monthlySchedule')) if dictionary.get('monthlySchedule') else None
        periodicity = dictionary.get('periodicity')
        rpo_schedule = cohesity_management_sdk.models.scheduling_policy_proto_rpo_schedule.SchedulingPolicyProtoRPOSchedule.from_dictionary(dictionary.get('rpoSchedule')) if dictionary.get('rpoSchedule') else None

        # Return an object of this model
        return cls(continuous_schedule,
                   daily_schedule,
                   monthly_schedule,
                   periodicity,
                   rpo_schedule)


