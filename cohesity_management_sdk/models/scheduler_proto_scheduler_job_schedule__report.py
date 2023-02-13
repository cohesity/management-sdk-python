# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.scheduler_proto_scheduler_job_schedule__report_parameters

class SchedulerProto_SchedulerJob_ScheduleJobParameters_ReportJobParameter_Report(object):

    """Implementation of the 'SchedulerProto_SchedulerJob_ScheduleJobParameters_ReportJobParameter_Report' model.

    Specifies the type and parameters of a report.

    Attributes:
        name (string): Specifies the report name.
        output_format (string): Specifies the output format of the report.
        parameters (
            SchedulerProto_SchedulerJob_ScheduleJobParameters_ReportJobParameter_Report_Parameters):
            TODO: Type description here.
        subject_line (string): Specifies the subject line for report.
        mtype (int): Specifies the report type.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "output_format": 'outputFormat',
        "parameters": 'parameters',
        "subject_line": 'subjectLine',
        "mtype":'type'
    }

    def __init__(self,
                 name=None,
                 output_format=None,
                 parameters=None,
                 subject_line=None,
                 mtype=None):
        """Constructor for the SchedulerProto_SchedulerJob_ScheduleJobParameters_ReportJobParameter_Report class"""

        # Initialize members of the class
        self.name = name
        self.output_format = output_format
        self.parameters = parameters
        self.subject_line = subject_line
        self.mtype = mtype

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
        name = dictionary.get('name')
        output_format = dictionary.get('outputFormat')
        parameters = cohesity_management_sdk.models.scheduler_proto_scheduler_job_schedule__report_parameters.SchedulerProto_SchedulerJob_ScheduleJobParameters_ReportJobParameter_Report_Parameters.from_dictionary(dictionary.get('parameters')) if dictionary.get('parameters') else None
        subject_line = dictionary.get('subjectLine')
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(name,
                   output_format,
                   parameters,
                   subject_line,
                   mtype)


