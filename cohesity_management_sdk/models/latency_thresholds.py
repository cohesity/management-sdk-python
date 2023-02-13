# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class LatencyThresholds(object):

    """Implementation of the 'LatencyThresholds' model.

    Specifies latency thresholds that trigger throttling for all datastores
    found in the registered Protection Source or specific to one datastore.

    Attributes:
        active_task_msecs (long|int): If the latency of a datastore is above
            this value, existing backup tasks using the datastore are
            throttled.
        new_task_msecs (long|int): If the latency of a datastore is above this
            value, then new backup tasks using the datastore will not be
            started.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "active_task_msecs":'activeTaskMsecs',
        "new_task_msecs":'newTaskMsecs'
    }

    def __init__(self,
                 active_task_msecs=None,
                 new_task_msecs=None):
        """Constructor for the LatencyThresholds class"""

        # Initialize members of the class
        self.active_task_msecs = active_task_msecs
        self.new_task_msecs = new_task_msecs


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
        active_task_msecs = dictionary.get('activeTaskMsecs')
        new_task_msecs = dictionary.get('newTaskMsecs')

        # Return an object of this model
        return cls(active_task_msecs,
                   new_task_msecs)


