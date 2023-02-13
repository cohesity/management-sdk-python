# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.task_attribute
import cohesity_management_sdk.models.task_event

class Task(object):

    """Implementation of the 'Task' model.

    Specifies one task.

    Attributes:
        attributes (list of TaskAttribute): The latest attributes reported for
            this task.
        end_time_seconds (long|int): Specifies the end time of the task.
        error_message (string): Specifies an optional error message for this
            task.
        events (list of TaskEvent): Specifies the events reported for this
            task.
        expected_end_time_seconds (long|int): Specifies the estimated end time
            of the task.
        expected_seconds_remaining (long|int): Specifies the expected
            remaining time for this task in seconds.
        expected_total_work_count (long|int): The expected raw count of the
            total work remaining. This is the highest work count value
            reported by the client. This field can be set to let pulse compute
            percentFinished by looking at the currently reported
            remainingWorkCount and the expectedTotalWorkCount.
        last_update_time_seconds (long|int): Specifies the timestamp when the
            last progress was reported.
        percent_finished (float): Specifies the reported progress on the
            task.
        start_time_seconds (long|int): Specifies the start time of the task.
        status (StatusTaskEnum): Specifies the status of the task being
            queried. 'kActive' indicates that the task is still active.
            'kFinished' indicates that the task has finished without any
            errors. 'kFinishedWithError' indicates that the task has finished,
            but that there was an errror of some kind. 'kCancelled' indicates
            that the task was cancelled. 'kFinishedGarbageCollected' inidcates
            that the task was garbage collected due to its subtasks not
            finishing within the allotted time.
        sub_tasks (list of object): Specifies a list of subtasks belonging to
            this task.
        task_path (string): Specifes the path of this task.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "attributes":'attributes',
        "end_time_seconds":'endTimeSeconds',
        "error_message":'errorMessage',
        "events":'events',
        "expected_end_time_seconds":'expectedEndTimeSeconds',
        "expected_seconds_remaining":'expectedSecondsRemaining',
        "expected_total_work_count":'expectedTotalWorkCount',
        "last_update_time_seconds":'lastUpdateTimeSeconds',
        "percent_finished":'percentFinished',
        "start_time_seconds":'startTimeSeconds',
        "status":'status',
        "sub_tasks":'subTasks',
        "task_path":'taskPath'
    }

    def __init__(self,
                 attributes=None,
                 end_time_seconds=None,
                 error_message=None,
                 events=None,
                 expected_end_time_seconds=None,
                 expected_seconds_remaining=None,
                 expected_total_work_count=None,
                 last_update_time_seconds=None,
                 percent_finished=None,
                 start_time_seconds=None,
                 status=None,
                 sub_tasks=None,
                 task_path=None):
        """Constructor for the Task class"""

        # Initialize members of the class
        self.attributes = attributes
        self.end_time_seconds = end_time_seconds
        self.error_message = error_message
        self.events = events
        self.expected_end_time_seconds = expected_end_time_seconds
        self.expected_seconds_remaining = expected_seconds_remaining
        self.expected_total_work_count = expected_total_work_count
        self.last_update_time_seconds = last_update_time_seconds
        self.percent_finished = percent_finished
        self.start_time_seconds = start_time_seconds
        self.status = status
        self.sub_tasks = sub_tasks
        self.task_path = task_path


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
        attributes = None
        if dictionary.get('attributes') != None:
            attributes = list()
            for structure in dictionary.get('attributes'):
                attributes.append(cohesity_management_sdk.models.task_attribute.TaskAttribute.from_dictionary(structure))
        end_time_seconds = dictionary.get('endTimeSeconds')
        error_message = dictionary.get('errorMessage')
        events = None
        if dictionary.get('events') != None:
            events = list()
            for structure in dictionary.get('events'):
                events.append(cohesity_management_sdk.models.task_event.TaskEvent.from_dictionary(structure))
        expected_end_time_seconds = dictionary.get('expectedEndTimeSeconds')
        expected_seconds_remaining = dictionary.get('expectedSecondsRemaining')
        expected_total_work_count = dictionary.get('expectedTotalWorkCount')
        last_update_time_seconds = dictionary.get('lastUpdateTimeSeconds')
        percent_finished = dictionary.get('percentFinished')
        start_time_seconds = dictionary.get('startTimeSeconds')
        status = dictionary.get('status')
        sub_tasks = dictionary.get('subTasks')
        task_path = dictionary.get('taskPath')

        # Return an object of this model
        return cls(attributes,
                   end_time_seconds,
                   error_message,
                   events,
                   expected_end_time_seconds,
                   expected_seconds_remaining,
                   expected_total_work_count,
                   last_update_time_seconds,
                   percent_finished,
                   start_time_seconds,
                   status,
                   sub_tasks,
                   task_path)


