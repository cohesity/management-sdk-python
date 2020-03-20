# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.backup_task_info
import cohesity_management_sdk.models.clone_task_info
import cohesity_management_sdk.models.basic_task_info
import cohesity_management_sdk.models.recovery_task_info

class TaskNotification(object):

    """Implementation of the 'TaskNotification' model.

    Structure that captures Task Notifications for a user.

    Attributes:
        backup_task (BackupTaskInfo): TODO: type description here.
        clone_task (CloneTaskInfo): Parameters for a clone op.
        created_time_secs (long|int): Timestamp at which the notification was
            created.
        description (string): Description holds the actual notification text
            generated for the event.
        dismissed (bool): Dismissed keeps track of whether a notification has
            been seen or not. User may choose to dismiss individual event or
            all notifications at once. Nil or 0 value represents false.
        dismissed_time_secs (long|int): Timestamp at which user dismissed this
            notification event.
        field_message_task (BasicTaskInfo): TODO: type description here.
        id (string): id identifies a user notification event uniquely. This
            can also be used to dismiss individual notifications.
        recovery_task (RecoveryTaskInfo): Parameters for a recovery op.
        status (StatusTaskNotificationEnum): Status of the task. Status of the
            task. 'kSuccess' indicates that task completed successfully.
            'kError' indicates that task encountered errors.
        task_type (TaskTypeEnum): Task type denotes which type of task this
            notification is for. This param is used to reflect the taskType.
            'Restore' notification type is generated upon completion of
            Restore tasks. 'Clone' notification type is generated upon
            completion of Clone tasks. 'BackupNow' notification type is
            generated upon completion of Backup tasks. 'FieldMessage'
            notification type is generated when field message from Cohesity
            support is created.
        visited (bool): Visited keeps track of whether a notification has been
            seen or not.
        visited_time_secs (long|int): Timestamp at which user visited this
            notification event.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "backup_task":'backupTask',
        "clone_task":'cloneTask',
        "created_time_secs":'createdTimeSecs',
        "description":'description',
        "dismissed":'dismissed',
        "dismissed_time_secs":'dismissedTimeSecs',
        "field_message_task":'fieldMessageTask',
        "id":'id',
        "recovery_task":'recoveryTask',
        "status":'status',
        "task_type":'taskType',
        "visited":'visited',
        "visited_time_secs":'visitedTimeSecs'
    }

    def __init__(self,
                 backup_task=None,
                 clone_task=None,
                 created_time_secs=None,
                 description=None,
                 dismissed=None,
                 dismissed_time_secs=None,
                 field_message_task=None,
                 id=None,
                 recovery_task=None,
                 status=None,
                 task_type=None,
                 visited=None,
                 visited_time_secs=None):
        """Constructor for the TaskNotification class"""

        # Initialize members of the class
        self.backup_task = backup_task
        self.clone_task = clone_task
        self.created_time_secs = created_time_secs
        self.description = description
        self.dismissed = dismissed
        self.dismissed_time_secs = dismissed_time_secs
        self.field_message_task = field_message_task
        self.id = id
        self.recovery_task = recovery_task
        self.status = status
        self.task_type = task_type
        self.visited = visited
        self.visited_time_secs = visited_time_secs


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
        backup_task = cohesity_management_sdk.models.backup_task_info.BackupTaskInfo.from_dictionary(dictionary.get('backupTask')) if dictionary.get('backupTask') else None
        clone_task = cohesity_management_sdk.models.clone_task_info.CloneTaskInfo.from_dictionary(dictionary.get('cloneTask')) if dictionary.get('cloneTask') else None
        created_time_secs = dictionary.get('createdTimeSecs')
        description = dictionary.get('description')
        dismissed = dictionary.get('dismissed')
        dismissed_time_secs = dictionary.get('dismissedTimeSecs')
        field_message_task = cohesity_management_sdk.models.basic_task_info.BasicTaskInfo.from_dictionary(dictionary.get('fieldMessageTask')) if dictionary.get('fieldMessageTask') else None
        id = dictionary.get('id')
        recovery_task = cohesity_management_sdk.models.recovery_task_info.RecoveryTaskInfo.from_dictionary(dictionary.get('recoveryTask')) if dictionary.get('recoveryTask') else None
        status = dictionary.get('status')
        task_type = dictionary.get('taskType')
        visited = dictionary.get('visited')
        visited_time_secs = dictionary.get('visitedTimeSecs')

        # Return an object of this model
        return cls(backup_task,
                   clone_task,
                   created_time_secs,
                   description,
                   dismissed,
                   dismissed_time_secs,
                   field_message_task,
                   id,
                   recovery_task,
                   status,
                   task_type,
                   visited,
                   visited_time_secs)


