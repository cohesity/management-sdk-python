# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.continuous_schedule
import cohesity_management_sdk.models.daily_schedule
import cohesity_management_sdk.models.monthly_schedule
import cohesity_management_sdk.models.rpo_schedule

class SchedulingPolicy(object):

    """Implementation of the 'SchedulingPolicy' model.

    Specifies settings that define a backup schedule for a Protection Job.

    Attributes:
        continuous_schedule (ContinuousSchedule): Specifies the time interval
            between two Job Runs of a continuous backup schedule and any
            blackout periods when new Job Runs should NOT be started. Set if
            periodicity is kContinuous.
        daily_schedule (DailySchedule): Specifies a daily or weekly backup
            schedule. Set if periodicity is kDaily.
        monthly_schedule (MonthlySchedule): Specifies a monthly backup
            schedule. Set if periodicity is kMonthly.
        periodicity (PeriodicityEnum): Specifies how often to start new Job
            Runs of a Protection Job. 'kDaily' means new Job Runs start daily.
            'kMonthly' means new Job Runs start monthly. 'kContinuous' means
            new Job Runs repetitively start at the beginning of the specified
            time interval (in hours or minutes). 'kContinuousRPO' means this
            is an RPO schedule. 'kCDP' means this is a continuous data
            protection policy.
        rpo_schedule (RpoSchedule): Specifies an RPO backup schedule. Set if
            periodicity is kContinuousRPO.

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
        """Constructor for the SchedulingPolicy class"""

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
        continuous_schedule = cohesity_management_sdk.models.continuous_schedule.ContinuousSchedule.from_dictionary(dictionary.get('continuousSchedule')) if dictionary.get('continuousSchedule') else None
        daily_schedule = cohesity_management_sdk.models.daily_schedule.DailySchedule.from_dictionary(dictionary.get('dailySchedule')) if dictionary.get('dailySchedule') else None
        monthly_schedule = cohesity_management_sdk.models.monthly_schedule.MonthlySchedule.from_dictionary(dictionary.get('monthlySchedule')) if dictionary.get('monthlySchedule') else None
        periodicity = dictionary.get('periodicity')
        rpo_schedule = cohesity_management_sdk.models.rpo_schedule.RpoSchedule.from_dictionary(dictionary.get('rpoSchedule')) if dictionary.get('rpoSchedule') else None

        # Return an object of this model
        return cls(continuous_schedule,
                   daily_schedule,
                   monthly_schedule,
                   periodicity,
                   rpo_schedule)


