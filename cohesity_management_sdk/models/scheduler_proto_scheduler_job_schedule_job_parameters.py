# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.scheduler_proto_scheduler_job_schedule__parameter

class SchedulerProto_SchedulerJob_ScheduleJobParameters(object):

    """Implementation of the
    'SchedulerProto_SchedulerJob_ScheduleJobParameters' model.

    Specifies the Scheduled Job parameters.

    Attributes:
    report_job_parameter (
        SchedulerProto_SchedulerJob_ScheduleJobParameters_ReportJobParameter):
        TODO: Type description here.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "report_job_parameter":'reportJobParameter'
    }

    def __init__(self,
                 report_job_parameter=None):
        """Constructor for the
        SchedulerProto_SchedulerJob_ScheduleJobParameters class"""

        # Initialize members of the class
        self.report_job_parameter = report_job_parameter


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
        report_job_parameter = cohesity_management_sdk.models.scheduler_proto_scheduler_job_schedule__parameter.SchedulerProto_SchedulerJob_ScheduleJobParameters_ReportJobParameter.from_dictionary(dictionary.get('reportJobParameter')) if dictionary.get('reportJobParameter') else None

        # Return an object of this model
        return cls(report_job_parameter)


