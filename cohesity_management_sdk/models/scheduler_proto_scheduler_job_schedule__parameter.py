# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.scheduler_proto_scheduler_job_schedule__report

class SchedulerProto_SchedulerJob_ScheduleJobParameters_ReportJobParameter(object):

    """Implementation of the 'SchedulerProto_SchedulerJob_ScheduleJobParameters_ReportJobParameter' model.

    Specifies the Report Job Parameters structure.

    Attributes:
        receiver_emails (list of string): Specifies the list of receiver email
            addresses.
        reports (list of
            SchedulerProto_SchedulerJob_ScheduleJobParameters_ReportJobParameter_Report):
            The list of reports to be sent in the mail.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "receiver_emails": 'receiverEmails',
        "reports": 'reports'
    }

    def __init__(self,
                 receiver_emails=None,
                 reports=None):
        """Constructor for the SchedulerProto_SchedulerJob_ScheduleJobParameters_ReportJobParameter class"""

        # Initialize members of the class
        self.receiver_emails = receiver_emails
        self.reports = reports


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
        receiver_emails = dictionary.get('receiverEmails', None)
        reports = None
        if dictionary.get('reports') != None:
            reports = list()
            for structure in dictionary.get('reports'):
                reports.append(cohesity_management_sdk.models.scheduler_proto_scheduler_job_schedule__report.SchedulerProto_SchedulerJob_ScheduleJobParameters_ReportJobParameter_Report.from_dictionary(structure))

        # Return an object of this model
        return cls(receiver_emails,
                   reports)


