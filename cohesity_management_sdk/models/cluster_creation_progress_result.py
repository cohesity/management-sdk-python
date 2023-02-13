# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ClusterCreationProgressResult(object):

    """Implementation of the 'ClusterCreationProgressResult' model.

    Specifies the values returned after a successful request to get the
    Cluster creation progress.

    Attributes:
        completion_percentage (int): Specifies an approximate completion
            percentage for the Cluster creation process.
        error_message (string): Specifies a description of an error if any
            error was encountered during Cluster creation.
        events (list of string): Specifies a list of events that took place
            during Cluster creation.
        in_progress (bool): Specifies whether or not the Cluster is still in
            the process of being created. Once the creation process is
            complete, this will be set to false and then, shortly afterward,
            all Cluster services will restart. The Cluster will be unreachable
            for about a minute while the services are being restarted.
        message (string): Specifies an optional message describing the current
            state of the creation progress operation.
        seconds_remaining (long|int): Specifies an estimated number of seconds
            until the Cluster creation process is complete.
        warnings_found (bool): Specifies whether or not any warnings were
            encountered during Cluster creation.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "completion_percentage":'completionPercentage',
        "error_message":'errorMessage',
        "events":'events',
        "in_progress":'inProgress',
        "message":'message',
        "seconds_remaining":'secondsRemaining',
        "warnings_found":'warningsFound'
    }

    def __init__(self,
                 completion_percentage=None,
                 error_message=None,
                 events=None,
                 in_progress=None,
                 message=None,
                 seconds_remaining=None,
                 warnings_found=None):
        """Constructor for the ClusterCreationProgressResult class"""

        # Initialize members of the class
        self.completion_percentage = completion_percentage
        self.error_message = error_message
        self.events = events
        self.in_progress = in_progress
        self.message = message
        self.seconds_remaining = seconds_remaining
        self.warnings_found = warnings_found


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
        completion_percentage = dictionary.get('completionPercentage')
        error_message = dictionary.get('errorMessage')
        events = dictionary.get('events')
        in_progress = dictionary.get('inProgress')
        message = dictionary.get('message')
        seconds_remaining = dictionary.get('secondsRemaining')
        warnings_found = dictionary.get('warningsFound')

        # Return an object of this model
        return cls(completion_percentage,
                   error_message,
                   events,
                   in_progress,
                   message,
                   seconds_remaining,
                   warnings_found)


