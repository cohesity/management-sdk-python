# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.scheduling_policy_proto_continuous_schedule
import cohesity_management_sdk.models.scheduling_policy_proto_daily_schedule
import cohesity_management_sdk.models.scheduling_policy_proto_date_schedule
import cohesity_management_sdk.models.scheduling_policy_proto_monthly_schedule
import cohesity_management_sdk.models.scheduling_policy_proto_rposchedule
import cohesity_management_sdk.models.scheduling_policy_proto_yearly_schedule


class SchedulingPolicyProto(object):

    """Implementation of the 'SchedulingPolicyProto' model.

    TODO: type description here.


    Attributes:

        continuous_schedule (SchedulingPolicyProto_ContinuousSchedule): Set if
            periodicity is kContinuous.
        daily_schedule (SchedulingPolicyProto_DailySchedule): Set if
            periodicity is kDaily.
        date_schedule (SchedulingPolicyProto_DateSchedule): Set if periodicity
            is kDate.
        monthly_schedule (SchedulingPolicyProto_MonthlySchedule): Set if
            periodicity is kMonthly.
        periodicity (int): Determines how often the job should be run.
        rpo_schedule (SchedulingPolicyProto_RPOSchedule): Set if periodicity is
            kContinuousRPO.
        yearly_schedule (SchedulingPolicyProto_YearlySchedule): Set if
            periodicity is kYearly.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "continuous_schedule":'continuousSchedule',
        "daily_schedule":'dailySchedule',
        "date_schedule":'dateSchedule',
        "monthly_schedule":'monthlySchedule',
        "periodicity":'periodicity',
        "rpo_schedule":'rpoSchedule',
        "yearly_schedule":'yearlySchedule',
    }
    def __init__(self,
                 continuous_schedule=None,
                 daily_schedule=None,
                 date_schedule=None,
                 monthly_schedule=None,
                 periodicity=None,
                 rpo_schedule=None,
                 yearly_schedule=None,
            ):

        """Constructor for the SchedulingPolicyProto class"""

        # Initialize members of the class
        self.continuous_schedule = continuous_schedule
        self.daily_schedule = daily_schedule
        self.date_schedule = date_schedule
        self.monthly_schedule = monthly_schedule
        self.periodicity = periodicity
        self.rpo_schedule = rpo_schedule
        self.yearly_schedule = yearly_schedule

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
        continuous_schedule = cohesity_management_sdk.models.scheduling_policy_proto_continuous_schedule.SchedulingPolicyProto_ContinuousSchedule.from_dictionary(dictionary.get('continuousSchedule')) if dictionary.get('continuousSchedule') else None
        daily_schedule = cohesity_management_sdk.models.scheduling_policy_proto_daily_schedule.SchedulingPolicyProto_DailySchedule.from_dictionary(dictionary.get('dailySchedule')) if dictionary.get('dailySchedule') else None
        date_schedule = cohesity_management_sdk.models.scheduling_policy_proto_date_schedule.SchedulingPolicyProto_DateSchedule.from_dictionary(dictionary.get('dateSchedule')) if dictionary.get('dateSchedule') else None
        monthly_schedule = cohesity_management_sdk.models.scheduling_policy_proto_monthly_schedule.SchedulingPolicyProto_MonthlySchedule.from_dictionary(dictionary.get('monthlySchedule')) if dictionary.get('monthlySchedule') else None
        periodicity = dictionary.get('periodicity')
        rpo_schedule = cohesity_management_sdk.models.scheduling_policy_proto_rposchedule.SchedulingPolicyProto_RPOSchedule.from_dictionary(dictionary.get('rpoSchedule')) if dictionary.get('rpoSchedule') else None
        yearly_schedule = cohesity_management_sdk.models.scheduling_policy_proto_yearly_schedule.SchedulingPolicyProto_YearlySchedule.from_dictionary(dictionary.get('yearlySchedule')) if dictionary.get('yearlySchedule') else None

        # Return an object of this model
        return cls(
            continuous_schedule,
            daily_schedule,
            date_schedule,
            monthly_schedule,
            periodicity,
            rpo_schedule,
            yearly_schedule
)