# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class TenantDeletionInfo(object):

    """Implementation of the 'TenantDeletionInfo' model.

    TenantDeletionInfo captures the individual deletion state of a category
    of
    objects marked tagged with a tenant_id (which has been marked for
    deletion).

    Attributes:
        category (int): Specifies the category of objects whose deletion state
            is being captured.
        finished_at_time_msecs (long|int): Specifies the time when the process
            finished.
        processed_at_node (string): Specifies the node ip where the process
            ran. Typically this would be Iris Master.
        retry_count (long|int): Specifies the number of times this task has
            been retried.
        started_at_time_msecs (long|int): Specifies the time when the process
            started.
        state (int): Specifies the deletion completion state of the object
            category.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "category":'category',
        "finished_at_time_msecs":'finishedAtTimeMsecs',
        "processed_at_node":'processedAtNode',
        "retry_count":'retryCount',
        "started_at_time_msecs":'startedAtTimeMsecs',
        "state":'state'
    }

    def __init__(self,
                 category=None,
                 finished_at_time_msecs=None,
                 processed_at_node=None,
                 retry_count=None,
                 started_at_time_msecs=None,
                 state=None):
        """Constructor for the TenantDeletionInfo class"""

        # Initialize members of the class
        self.category = category
        self.finished_at_time_msecs = finished_at_time_msecs
        self.processed_at_node = processed_at_node
        self.retry_count = retry_count
        self.started_at_time_msecs = started_at_time_msecs
        self.state = state


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
        category = dictionary.get('category')
        finished_at_time_msecs = dictionary.get('finishedAtTimeMsecs')
        processed_at_node = dictionary.get('processedAtNode')
        retry_count = dictionary.get('retryCount')
        started_at_time_msecs = dictionary.get('startedAtTimeMsecs')
        state = dictionary.get('state')

        # Return an object of this model
        return cls(category,
                   finished_at_time_msecs,
                   processed_at_node,
                   retry_count,
                   started_at_time_msecs,
                   state)


