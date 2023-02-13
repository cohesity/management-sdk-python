# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class GetMapReduceAppRunsParams(object):

    """Implementation of the 'GetMapReduceAppRunsParams' model.

    GetMapReduceAppRunsParams specifies the input params to fetch the map
    reduce
    application runs.

    Attributes:
        app_id (int): ApplicationId is the Id of the map reduce application.
        app_instance_id (int): ApplicationInstanceId is the Id of the map
            reduce application instance.
        include_details (bool): If this flag is true, then send details of
            instance, else send only RunInfo.
        last_num_instances (long|int): Give last N instance of an app based on
            end time.
        max_run_end_time_in_secs (long|int): MaxRunEndTimestampInSecs
            specifies the maximum job run end timestamp in seconds. App run
            instances with end time less than equal to
            MaxRunEndTimestampInSecs will be selected. Default is LONG_MAX
            (inf).
        max_run_start_time_in_secs (int|long): MaxRunStartTimestampInSecs
            specifies the maximum job run start timestamp in seconds. App run
            instances with start time less than equal to
            MaxRunStartTimestampInSecs will be selected. Default is LONG_MAX
            (inf).
        min_run_end_time_in_secs (long|int): MinRunEndTimestampInSecs
            specifies the minimum job run end timestamp in seconds. App run
            instances with end time greater than equal to
            MinRunEndTimestampInSecs will be selected. Default is 0, i.e.
            beginning of time.
        min_run_start_time_in_secs (int|long): MinRunStartTimestampInSecs
            specifies the minimum job run start timestamp in seconds. App run
            instances with start time greater than equal to
            MinRunStartTimestampInSecs will be selected. Default is 0, i.e.
            beginning of time.
        page_size (int|long): Number of results to be displayed on a page.
        run_status (string): Filter instances based on the map reduce
            application run status.
        start_offset (int): Start offset for pagination from where
            result needs to be fetched.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "app_id":'appId',
        "app_instance_id":'appInstanceId',
        "include_details":'includeDetails',
        "last_num_instances":'lastNumInstances',
        "max_run_end_time_in_secs":'maxRunEndTimeInSecs',
        "max_run_start_time_in_secs":'maxRunStartTimeInSecs',
        "min_run_end_time_in_secs":'minRunEndTimeInSecs',
        "min_run_start_time_in_secs":'minRunStartTimeInSecs',
        "page_size":'pageSize',
        "run_status":'runStatus',
        "start_offset":'startOffset'
    }

    def __init__(self,
                 app_id=None,
                 app_instance_id=None,
                 include_details=None,
                 last_num_instances=None,
                 max_run_end_time_in_secs=None,
                 max_run_start_time_in_secs=None,
                 min_run_end_time_in_secs=None,
                 min_run_start_time_in_secs=None,
                 page_size=None,
                 run_status=None,
                 start_offset=None):
        """Constructor for the GetMapReduceAppRunsParams class"""

        # Initialize members of the class
        self.app_id = app_id
        self.app_instance_id = app_instance_id
        self.include_details = include_details
        self.last_num_instances = last_num_instances
        self.max_run_end_time_in_secs = max_run_end_time_in_secs
        self.max_run_start_time_in_secs = max_run_start_time_in_secs
        self.min_run_end_time_in_secs = min_run_end_time_in_secs
        self.min_run_start_time_in_secs = min_run_start_time_in_secs
        self.page_size = page_size
        self.run_status = run_status
        self.start_offset = start_offset


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
        app_id = dictionary.get('appId')
        app_instance_id = dictionary.get('appInstanceId')
        include_details = dictionary.get('includeDetails')
        last_num_instances = dictionary.get('lastNumInstances')
        max_run_end_time_in_secs = dictionary.get('maxRunEndTimeInSecs')
        max_run_start_time_in_secs = dictionary.get('maxRunStartTimeInSecs')
        min_run_end_time_in_secs = dictionary.get('minRunEndTimeInSecs')
        min_run_start_time_in_secs = dictionary.get('minRunStartTimeInSecs')
        page_size = dictionary.get('pageSize')
        run_status = dictionary.get('runStatus')
        start_offset = dictionary.get('startOffset')

        # Return an object of this model
        return cls(app_id,
                   app_instance_id,
                   include_details,
                   last_num_instances,
                   max_run_end_time_in_secs,
                   max_run_start_time_in_secs,
                   min_run_end_time_in_secs,
                   min_run_start_time_in_secs,
                   page_size,
                   run_status,
                   start_offset)


