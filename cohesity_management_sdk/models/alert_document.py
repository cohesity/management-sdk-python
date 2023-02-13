# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class AlertDocument(object):

    """Implementation of the 'AlertDocument' model.

    Specifies documentation about the Alert such as name, description, cause
    and how to resolve the Alert.

    Attributes:
        alert_cause (string): Specifies cause of the Alert that is included in
            the body of the email or any other type of notification.
        alert_description (string): Specifies brief description about the
            Alert that is used in the subject line when sending a notification
            email for an Alert.
        alert_help_text (string): Specifies instructions describing how to
            resolve the Alert that is included in the body of the email or any
            other type of notification.
        alert_name (string): Specifies short name that describes the Alert
            type such as DiskBad, HighCpuUsage, FrequentProcessRestarts, etc.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "alert_cause":'alertCause',
        "alert_description":'alertDescription',
        "alert_help_text":'alertHelpText',
        "alert_name":'alertName'
    }

    def __init__(self,
                 alert_cause=None,
                 alert_description=None,
                 alert_help_text=None,
                 alert_name=None):
        """Constructor for the AlertDocument class"""

        # Initialize members of the class
        self.alert_cause = alert_cause
        self.alert_description = alert_description
        self.alert_help_text = alert_help_text
        self.alert_name = alert_name


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
        alert_cause = dictionary.get('alertCause')
        alert_description = dictionary.get('alertDescription')
        alert_help_text = dictionary.get('alertHelpText')
        alert_name = dictionary.get('alertName')

        # Return an object of this model
        return cls(alert_cause,
                   alert_description,
                   alert_help_text,
                   alert_name)


