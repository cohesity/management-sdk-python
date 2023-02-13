# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.scheduler_proto_scheduler_job_schedule_job_parameters
import cohesity_management_sdk.models.scheduler_proto_scheduler_job_schedule

class SchedulerProto_SchedulerJob(object):

    """Implementation of the 'SchedulerProto_SchedulerJob' model.

    Specifies the structure of the scheduler job along with its attributes.

    Attributes:
        enable_recurring_email (bool): The boolean which specifies if this
            job is to be scheduled or not.
        id (int|long): The unique id for the scheduled job assigned by the cluster.
        name (string): The name of the scheduled job given by the user.
        schedule_job_parameters (
            SchedulerProto_SchedulerJob_ScheduleJobParameters): TODO: Type
            description here.
        schedules (list of SchedulerProtoSchedulerJobSchedule): TODO: Type
            description here.
        tenant_id (string): Specifies id of tenant who created the scheduler
            job.
        mtype (TypeSchedulerProtoSchedulerJobEnum): Specifies the type of the
            job. The enum which defines the Job type of the job.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enable_recurring_email": 'enableRecurringEmail',
        "id": 'id',
        "name": 'name',
        "schedule_job_parameters": 'scheduleJobParameters',
        "schedules":'schedules',
        "tenant_id":'tenantId',
        "mtype":'type'
    }

    def __init__(self,
                 enable_recurring_email=None,
                 id=None,
                 name=None,
                 schedule_job_parameters=None,
                 schedules=None,
                 tenant_id=None,
                 mtype=None):
        """Constructor for the SchedulerProto_SchedulerJob class"""

        # Initialize members of the class
        self.enable_recurring_email = enable_recurring_email
        self.id = id
        self.name = name
        self.schedule_job_parameters = schedule_job_parameters
        self.schedules = schedules
        self.tenant_id = tenant_id
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
        enable_recurring_email = dictionary.get('enableRecurringEmail')
        id = dictionary.get('id')
        name = dictionary.get('name')
        schedule_job_parameters = cohesity_management_sdk.models.scheduler_proto_scheduler_job_schedule_job_parameters.SchedulerProto_SchedulerJob_ScheduleJobParameters.from_dictionary(dictionary.get('scheduleJobParameters')) if dictionary.get('scheduleJobParameters') else None
        schedules = None
        if dictionary.get('schedules') != None:
            schedules = list()
            for structure in dictionary.get('schedules'):
                schedules.append(cohesity_management_sdk.models.scheduler_proto_scheduler_job_schedule.SchedulerProtoSchedulerJobSchedule.from_dictionary(structure))
        tenant_id = dictionary.get('tenantId')
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(enable_recurring_email,
                   id,
                   name,
                   schedule_job_parameters,
                   schedules,
                   mtype)


