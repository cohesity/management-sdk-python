# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class UpdateNotifications(object):

    """Implementation of the 'UpdateNotifications' model.

    Specifies the list of notificationIds and the operation to be performed.

    Attributes:
        action (string): Specifies the operation to be performed on the
            resource. Eg. "action":"dismiss"
        notification_ids (list of string): Specifies the list of
            NotificationIds to be operated upon.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "action":'action',
        "notification_ids":'notificationIds'
    }

    def __init__(self,
                 action=None,
                 notification_ids=None):
        """Constructor for the UpdateNotifications class"""

        # Initialize members of the class
        self.action = action
        self.notification_ids = notification_ids


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
        action = dictionary.get('action')
        notification_ids = dictionary.get('notificationIds')

        # Return an object of this model
        return cls(action,
                   notification_ids)


