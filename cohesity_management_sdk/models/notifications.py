# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.task_notification

class Notifications(object):

    """Implementation of the 'Notifications' model.

    All the Notification events generated for a given user. This is used for
    transferring notifications over wire.

    Attributes:
        count (long|int): Notification Count.
        notification_list (list of TaskNotification): Notification list.
        unread_count (long|int): Unread Notification Count.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "count":'count',
        "notification_list":'notificationList',
        "unread_count":'unreadCount'
    }

    def __init__(self,
                 count=None,
                 notification_list=None,
                 unread_count=None):
        """Constructor for the Notifications class"""

        # Initialize members of the class
        self.count = count
        self.notification_list = notification_list
        self.unread_count = unread_count


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
        count = dictionary.get('count')
        notification_list = None
        if dictionary.get('notificationList') != None:
            notification_list = list()
            for structure in dictionary.get('notificationList'):
                notification_list.append(cohesity_management_sdk.models.task_notification.TaskNotification.from_dictionary(structure))
        unread_count = dictionary.get('unreadCount')

        # Return an object of this model
        return cls(count,
                   notification_list,
                   unread_count)


